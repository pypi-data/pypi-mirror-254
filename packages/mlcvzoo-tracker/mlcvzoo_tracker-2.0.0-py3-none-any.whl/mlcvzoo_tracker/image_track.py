# Copyright Open Logistics Foundation
#
# Licensed under the Open Logistics Foundation License 1.3.
# For details on the licensing terms, see the LICENSE file.
# SPDX-License-Identifier: OLFL-1.3

"""
Module for encapsulating the history of an object tracked over time, estimating its
current state even in case of missing updates and managing its lifecycle
"""

from __future__ import annotations

import logging
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional

import numpy as np
from filterpy.kalman import KalmanFilter
from mlcvzoo_base.api.data.bounding_box import BoundingBox
from mlcvzoo_base.api.data.box import Box, compute_iou, euclidean_distance
from mlcvzoo_base.api.data.class_identifier import ClassIdentifier

from mlcvzoo_tracker.configuration import KalmanFilterConfig, TrackerConfig
from mlcvzoo_tracker.sized_dict import SizedDict
from mlcvzoo_tracker.types import FrameShape, ImageType

logger = logging.getLogger(__name__)


class TrackerState(str, Enum):
    """
    A Track has three states:

        1. INITIATED: When an ImageTrack is instantiated
        2. ACTIVE: ImageTrack got enough sensor updates
        3. OCCLUDED: The track is occluded by another object and therefore currently
                     not visible. In this state, the bounding-box of the last update
                     before the occlusion will be used, until it is not occluded / gets
                     a sensor update.
        4. DEAD: If a ImageTrack does not get sensor updates for the configured period
                 of frames
        MERGED: (WIP) Special state that is currently not managed by the tracker
    """

    INITIATED = "INITIATED"
    ACTIVE = "ACTIVE"
    OCCLUDED = "OCCLUDED"
    MERGED = "MERGED"
    DEAD = "DEAD"

    def __repr__(self):  # type: ignore[no-untyped-def]
        return str.__repr__(self)

    def __str__(self):  # type: ignore[no-untyped-def]
        return str.__str__(self)


@dataclass
class SensorUpdate:
    """
    Dataclass for storing one Sensor Update
    """

    bounding_box: BoundingBox
    frame_id: int


@dataclass
class TrackEvent:
    """
    Class for storing all tracking information related to a single bounding box at the time of a specific frame.
    """

    bounding_box: BoundingBox
    timestamp: datetime
    state: TrackerState
    frame_id: int
    track_id: int
    speed: float

    __timestamp_format: str = "%Y-%m-%d_%H-%M-%S"

    def __repr__(self) -> str:
        return (
            f"TrackEvent: "
            f"timestamp: {self.timestamp.strftime(self.__timestamp_format)}, "
            f"state: {self.state}, "
            f"frame_id: {self.frame_id}, "
            f"track_id: {self.track_id}, "
            f"speed: {self.speed}, "
            f"bounding_box: {self.bounding_box}"
        )

    def __eq__(self, other: TrackEvent) -> bool:  # type: ignore[override]
        return (
            self.bounding_box == other.bounding_box
            and self.timestamp == other.timestamp
            and self.state == other.state
            and self.frame_id == other.frame_id
            and self.track_id == other.track_id
            and self.speed == other.speed
        )

    def to_dict(self, raw_type: bool = False, reduced: bool = False) -> Dict[str, Any]:
        """
        Args:
            raw_type: Whether to return the class identifier and timestamp as object or in its representation
                      as dictionary
            reduced: Whether to return the full or a reduced representation of each bounding box

        Returns:
            A dictionary representations of the track event
        """

        return {
            "bounding_box": self.bounding_box.to_dict(
                raw_type=raw_type, reduced=reduced
            ),
            "timestamp": self.timestamp
            if raw_type
            else self.timestamp.strftime(self.__timestamp_format),
            "state": self.state,
            "frame_id": self.frame_id,
            "track_id": self.track_id,
            "speed": self.speed,
        }

    @staticmethod
    def from_dict(input_dict: Dict[str, Any], reduced: bool = False) -> TrackEvent:
        """
        Creates a new TrackEvent object from the dictionary representation.

        Args:
            input_dict: The dictionary to create the TrackEvent from
            reduced: Whether the input_dict stores a reduced version of information

        Raises:
            ValueError: When the given 'state' is the input_dict is not valid

        Returns:
            The TrackEvent created from the input_dict
        """

        return TrackEvent(
            bounding_box=BoundingBox.from_dict(
                input_dict=input_dict["bounding_box"], reduced=reduced
            ),
            timestamp=datetime.strptime(
                input_dict["timestamp"], TrackEvent.__timestamp_format
            ),
            state=TrackerState(input_dict["state"]),
            frame_id=int(input_dict["frame_id"]),
            track_id=input_dict["track_id"],
            speed=input_dict["speed"],
        )


class ImageTrack:
    """
    Class using Kalman filter to track a single object represented by its bounding box, storing its
    history as a list of TrackEvents and managing the lifecycle of the track.
    """

    def __init__(
        self,
        configuration: TrackerConfig,
        track_id: int,
        initial_frame_id: int,
        initial_bbox: BoundingBox,
        initial_color_hist: Optional[ImageType] = None,
        meta_info: Optional[Dict[str, Any]] = None,
        update_speed: bool = False,
    ) -> None:
        """
        Initialize object.

        Args:
            initial_frame_id: The time stamp to start with.
            initial_bbox: First detection.
            configuration: Tracker configuration for this ImageTrack object
            initial_color_hist: Color history of the initial box. Can be None if not used.
            meta_info: Dictionary providing meta information for this ImageTrack object
        """

        # ========================================================
        # Static information

        self.configuration = configuration

        # The tracks class-identifier is defined by its initial bounding-box
        self.class_identifier: ClassIdentifier = initial_bbox.class_identifier

        # Dictionary that can be filled with meta information about this ImageTrack
        self.meta_info: Optional[Dict[str, Any]] = meta_info

        self._start_time: datetime = datetime.utcnow()

        # Flag that indicates that the ImageTrack has been in the TrackingState.ACTIVE for at least one frame
        self.was_active: bool = False

        # ========================================================
        # Dynamic information for the main tracking functionality.
        # This attributes change over time of the ImageTrack

        # A track becomes the "active" status, once it got enough
        # sensor updates in form of bounding-boxes. The threshold
        # is defined via configuration.min_detections_active
        self._sensor_update_counter: int = 1

        # Current TrackEvent
        self._current_track_event: TrackEvent = TrackEvent(
            bounding_box=initial_bbox,
            timestamp=datetime.utcnow(),
            state=TrackerState.INITIATED,
            frame_id=initial_frame_id,
            track_id=track_id,
            speed=0.0,
        )
        if self.configuration.min_detections_active == 0:
            self.current_state = TrackerState.ACTIVE
            self.was_active = True

        # Current sensor update used to update the kalman filter
        self._current_sensor_update: SensorUpdate = SensorUpdate(
            bounding_box=deepcopy(initial_bbox),
            frame_id=self.current_frame_id,
        )

        self._kf: KalmanFilter = ImageTrack.create_kalman_filter(
            kalman_filter_config=self.configuration.kalman_filter_config,
            initial_bbox=initial_bbox,
        )

        # ========================================================
        # Secondary data

        # The current color histogram of this ImageTrack
        # TODO: Merge into TrackEvent?
        self.current_color_hist: Optional[ImageType] = initial_color_hist

        # Will only be updated to measure the speed between two consecutive frames
        self._last_track_event: Optional[TrackEvent] = None

        # If configured in configuration.max_number_track_events, store the history of TrackEvents
        self.__track_events: Optional[
            SizedDict[int, TrackEvent]
        ] = self.__init_track_events()

        # Whether to update the speed attribute of self._current_track_event
        self._update_speed: bool = update_speed

    @property
    def track_events(self) -> Optional[SizedDict[int, TrackEvent]]:
        """
        Returns:
            (Optional) The current TrackEvent dictionary (if configured), containing:
            - Key: Frame-IDs
            - Value: Corresponding list of TrackEvents.The indices of this list represent the Track-ID.
        """
        return self.__track_events

    @property
    def track_id(self) -> int:
        """
        Returns:
            The track-id associated with this ImageTrack
        """
        return self._current_track_event.track_id

    @property
    def current_frame_id(self) -> int:
        """
        Returns:
            The current frame-id of the ImageTrack (will be counted up for each frame)
        """
        return self._current_track_event.frame_id

    @property
    def current_speed(self) -> float:
        """
        The speed is defined as the distance of pixels that
        the track has traveled between two consecutive frames

        Returns:
            Current speed for this ImageTrack
        """
        return self._current_track_event.speed

    @property
    def current_bounding_box(self) -> BoundingBox:
        """
        Returns:
            Current bounding box of this ImageTrack
        """
        return self._current_track_event.bounding_box

    @property
    def start_time(self) -> datetime:
        """
        Returns:
            The start time when the ImageTrack was instantiated
        """
        return self._start_time

    @property
    def current_state(self) -> TrackerState:
        """
        Returns:
            The current state of the ImageTrack
        """
        return self._current_track_event.state

    @current_state.setter
    def current_state(self, value: TrackerState) -> None:
        self._current_track_event.state = value

    def age(self) -> int:
        """
        Returns:
            The age as the number of frames the ImageTrack got no sensor updates
        """
        return self.current_frame_id - self.last_sensor_update_frame_id()

    def get_current_track_event(self) -> TrackEvent:
        """
        Returns:
            The current TrackEvent of a ImageTrack
        """
        return self._current_track_event

    def __repr__(self) -> str:
        return (
            f"ImageTrack: class-identifier={self.class_identifier}, "
            f"len: {len(self.__track_events) if self.__track_events is not None else 0}, "
            f"current_track_event: {self.get_current_track_event()}"
        )

    def to_dict(self, raw_type: bool = False, reduced: bool = False) -> Dict[str, Any]:
        """
        Args:
            raw_type: Whether to store classes as dictionary or real objects
            reduced: Whether to include all objects or a reduced (functional) set

        Returns:
            Dictionary representation of a ImageTrack
        """
        return self.get_current_track_event().to_dict(
            raw_type=raw_type, reduced=reduced
        )

    def to_json(self) -> Any:
        """
        Returns:
            json conform dictionary representation of a ImageTrack
        """
        return self.to_dict(raw_type=False)

    def __init_track_events(self) -> Optional[SizedDict[int, TrackEvent]]:
        track_events: Optional[SizedDict[int, TrackEvent]] = None
        if self.configuration.max_number_track_events is not None:
            if self.configuration.max_number_track_events == float("inf"):
                track_events = SizedDict()
            else:
                track_events = SizedDict(
                    max_size=int(self.configuration.max_number_track_events)
                )
            track_events[self.current_frame_id] = deepcopy(self._current_track_event)
        return track_events

    @staticmethod
    def create_kalman_filter(
        kalman_filter_config: KalmanFilterConfig, initial_bbox: BoundingBox
    ) -> KalmanFilter:
        """
        Create a KalmanFilter object from the given configuration
        and initial bounding box.

        State is position and speed for x and y and together with
        the width and height of a box. The unit is pixel and
        pixel per frame so this is independent of fps. The (x, y)
        position is the center of the box that will be tracked with
        the kalman filter.

        State transition matrix F:
         x      1 1 0 0 0 0
        dx  =   0 1 0 0 0 0
         y      0 0 1 1 0 0
        dy      0 0 0 1 0 0
         w      0 0 0 0 1 0
         h      0 0 0 0 0 1

        Measurement matrix H:
         x      1 0 0 0
        dx  =   0 0 0 0
         y      0 1 0 0
        dy      0 0 0 0
         w      0 0 1 0
         h      0 0 0 1

        Args:
            kalman_filter_config: The KalmanFilterConfig defining the relevant parameter
            initial_bbox: The bounding-box for initializing the KalmanFilter

        Returns:
            The created KalmanFilter object
        """

        # [x_center, dx, y_center, dy, w, h]
        kalman_filter: KalmanFilter = KalmanFilter(dim_x=6, dim_z=4)

        kalman_filter.x = np.array(
            [
                [initial_bbox.box.center()[0]],
                [0],
                [initial_bbox.box.center()[1]],
                [0],
                [initial_bbox.box.width],
                [initial_bbox.box.height],
            ]
        )

        kalman_filter.H = np.array(
            [
                [1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
            ]
        )

        kalman_filter.F = np.array(
            [
                [1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
            ]
        )

        kalman_filter.R = np.array(
            [
                [kalman_filter_config.R, 0, 0, 0],
                [0, kalman_filter_config.R, 0, 0],
                [0, 0, kalman_filter_config.R, 0],
                [0, 0, 0, kalman_filter_config.R],
            ]
        )

        kalman_filter.P *= kalman_filter_config.P

        # self.kf.Q = Q_discrete_white_noise(dim=4, dt=1, var=0.1)

        return kalman_filter

    def get_start_time(self) -> datetime:
        """
        Returns:
            The datetime object when the track was initially started
        """
        return self._start_time

    def get_alive_time(self) -> timedelta:
        """
        Returns:
            The datetime object when the track was initially started
        """
        return datetime.utcnow() - self.get_start_time()

    def get_stop_time(
        self,
    ) -> Optional[datetime]:
        """
        Get the stop time of this ImageTrack. When the ImageTrack is still active,
        then it returns None.

        Returns:
            The datetime object when the track was stopped / was not active anymore
        """
        if not self.is_active():
            return self._current_track_event.timestamp

        return None

    def is_valid(self) -> bool:
        """
        An ImageTrack is valid when it was active for at least one frame

        Returns:
            Whether the ImageTrack is valid
        """
        return self.was_active

    def is_alive(self) -> bool:
        """
        An ImageTrack is alive when it is not in the TrackerState.DEAD state

        Returns:
            Whether a track is alive
        """
        return self.current_state is not TrackerState.DEAD

    def is_active(self) -> bool:
        """
        Determines if a track is still active, based on:

        Returns:
            Whether the track is counted as active based on the described conditions
        """
        return (
            self.current_state is TrackerState.ACTIVE
            or self.current_state is TrackerState.OCCLUDED
        )

    def last_sensor_update_frame_id(self) -> int:
        """
        Determines the last frame ID where a detection was added.
        Can be used to determine how long an object was not detected.

        Returns:
            The frame ID
        """
        return self._current_sensor_update.frame_id

    def set_color_histogram(self, color_hist: Optional[ImageType]) -> None:
        """
        Sets the current color histogram for this track

        Args:
            color_hist: The color histogram to set

        Returns:
            None
        """
        alpha = self.configuration.assignment_cost_config.color_cost.color_filter_alpha
        if self.current_color_hist is not None and alpha < 1:
            self.current_color_hist = (1 - alpha) * self.current_color_hist + alpha * color_hist  # type: ignore
        else:
            self.current_color_hist = color_hist

    def get_redetect_radius(self) -> float:
        """
        Based on the motion model of objects, this determines a radius where the object could
        have been moved to, while it was not detected / got no sensor updates. Note that the
        kalman filter only gives the estimated position based on the last speed. A kalman filter
        does not include such a motion model as applied here.

        The radius is determined by the uniform motion of the object:
        s = v*t + s0

        v:= pixel speed per frame (take into account that this could be different for different images sizes
        s0:= constant pixel distance an object can travel

        The speed is the pixel distance between the centers of two consecutive track bounding boxes

        v and s0 are taken from the tracker configuration

        Returns:
            The possible (maximum) radius in pixel where the object could have been moved
        """

        return (
            (self.age() - 1)
            * self.configuration.assignment_cost_config.distance_cost.obj_speed.v
            + self.configuration.assignment_cost_config.distance_cost.obj_speed.s_0
        )

    def __predict_bounding_box(self) -> None:
        """
        Use the bounding-boxes for <kalman_delay> frames as tracker positions
        instead of the position from the filter.
        Reason: We need some detections to be able to estimate a good speed.

        Returns:
            None
        """
        if (
            self._sensor_update_counter
            <= self.configuration.kalman_filter_config.kalman_delay
        ):
            self._current_track_event.bounding_box = (
                self._current_sensor_update.bounding_box
            )
        else:
            x_center = self._kf.x[0]
            y_center = self._kf.x[2]
            width = self._kf.x[4]
            height = self._kf.x[5]

            self._current_track_event.bounding_box = BoundingBox(
                box=Box(
                    xmin=int(x_center - width / 2),
                    ymin=int(y_center - height / 2),
                    xmax=int(x_center + width / 2),
                    ymax=int(y_center + height / 2),
                ),
                class_identifier=self._current_track_event.bounding_box.class_identifier,
                score=self._current_track_event.bounding_box.score,
                difficult=False,
                occluded=False,
                content="",
                model_class_identifier=self._current_track_event.bounding_box.model_class_identifier,
            )

    def __is_valid_bounding_box(self, frame_shape: FrameShape) -> bool:
        """
        Checks whether the current bounding box of this track is still
        inside the borders of the frame. If not one can not be sure that
        a re-entering track is an old or new track. Therefore, once the
        bounding box of a track is completely outside an image its status
        changes to DEAD.

        Returns:
            None
        """
        return not (
            # Upper image border
            self._current_track_event.bounding_box.box.ymax < 0
            # Right image border
            or self._current_track_event.bounding_box.box.xmin >= frame_shape.width
            # Lower image border
            or self._current_track_event.bounding_box.box.ymin >= frame_shape.height
            # Left image border
            or self._current_track_event.bounding_box.box.xmax < 0
        )

    def __update_speed(self, last_box: Box) -> None:
        self._current_track_event.speed = euclidean_distance(
            box_1=self.current_bounding_box.box,
            box_2=last_box,
        )

    def predict(
        self,
        occlusion_bounding_boxes: Optional[List[BoundingBox]] = None,
        frame_shape: Optional[FrameShape] = None,
    ) -> None:
        """
        Update the internal Kalman filter (prediction step) and the state of this ImageTrack.
        It does not have an effect if the ImageTrack is in the TrackerState.DEAD state.

        Must be called for every frame in the following order:
        predict(...) --> (Optional) update(...)

        The frame-shape is used to determine whether a track is outside the image borders.

        The occlusion boxes are used to check whether a box is prune to be occluded by other
        objects due to the 2D perspective.

        Args:
            frame_shape: The shape of the frame
            occlusion_bounding_boxes: Potential bounding boxes of object that might occlude
                                      this track, respectively the current bounding box of
                                      this track

        Returns:
            None
        """

        if self.current_state is TrackerState.DEAD:
            return

        # Check if ImageTrack got to old and therefore is DEAD now
        if self.age() > self.configuration.max_age:
            self.current_state = TrackerState.DEAD
            if self.__track_events is not None:
                self.__track_events[self.current_frame_id].state = TrackerState.DEAD

            # return prematurely because the image track is DEAD now
            return

        # Predict next state
        if self._update_speed:
            self._last_track_event = deepcopy(self._current_track_event)

        self._current_track_event.frame_id += 1
        self._kf.predict()
        self.__predict_bounding_box()

        # Check for valid box
        if frame_shape is not None and not self.__is_valid_bounding_box(
            frame_shape=frame_shape
        ):
            self.current_state = TrackerState.DEAD
            if self.__track_events is not None:
                self.__track_events[self.current_frame_id] = deepcopy(
                    self._current_track_event
                )
            # return prematurely because the image track is DEAD now
            return

        # Update speed
        if self._last_track_event is not None:
            self.__update_speed(last_box=self._last_track_event.bounding_box.box)

        # Check occlusion
        if (
            occlusion_bounding_boxes is not None
            and self.current_state is TrackerState.ACTIVE
        ):
            for occlusion_bounding_box in occlusion_bounding_boxes:
                # TODO: Check if this could trigger to much computing time
                if (
                    compute_iou(
                        box_1=occlusion_bounding_box.box,
                        box_2=self.current_bounding_box.box,
                    )
                    > 0.0
                ):
                    # Assume that the bounding box has not changed during the time
                    # the object was occluded
                    self.current_state = TrackerState.OCCLUDED
                    break

        # Save current track event
        if self.__track_events is not None:
            self.__track_events[self.current_frame_id] = deepcopy(
                self._current_track_event
            )

    def update(
        self,
        bounding_box: BoundingBox,
        frame_shape: Optional[FrameShape] = None,
    ) -> None:
        """
        Perform a sensor update of the internal kalman filter for this
        ImageTrack using the given bounding-box. It does not have an effect
        if the ImageTrack is in the TrackerState.DEAD state

        Should be called once within a step in the following order:
        predict(...) --> (Optional) update(...)

        The frame-shape is used to determine whether a track is outside the image borders.

        Args:
            bounding_box: The bounding box that should be used as sensor update
            frame_shape: The shape of the frame

        Returns:
            None
        """

        if self.current_state is TrackerState.DEAD:
            return

        self._sensor_update_counter += 1

        if self.current_state is TrackerState.OCCLUDED:
            self.current_state = TrackerState.ACTIVE

        self._current_sensor_update = SensorUpdate(
            bounding_box=deepcopy(bounding_box), frame_id=self.current_frame_id
        )
        x_center, y_center = self._current_sensor_update.bounding_box.box.center()
        self._kf.update(
            [
                x_center,
                y_center,
                self._current_sensor_update.bounding_box.box.width,
                self._current_sensor_update.bounding_box.box.height,
            ]
        )
        self.__predict_bounding_box()

        if frame_shape is not None and not self.__is_valid_bounding_box(
            frame_shape=frame_shape
        ):
            self.current_state = TrackerState.DEAD
            if self.__track_events is not None:
                self.__track_events[self.current_frame_id] = deepcopy(
                    self._current_track_event
                )
            # return prematurely because the image track is DEAD now
            return

        if self._last_track_event is not None:
            self.__update_speed(last_box=self._last_track_event.bounding_box.box)

        # Switch to state ACTIVE when the ImageTrack got enough sensor updates
        if (
            self.current_state is TrackerState.INITIATED
            and self._sensor_update_counter >= self.configuration.min_detections_active
        ):
            self.current_state = TrackerState.ACTIVE
            self.was_active = True

        if self.__track_events is not None:
            self.__track_events[self.current_frame_id] = deepcopy(
                self._current_track_event
            )
