# Copyright Open Logistics Foundation
#
# Licensed under the Open Logistics Foundation License 1.3.
# For details on the licensing terms, see the LICENSE file.
# SPDX-License-Identifier: OLFL-1.3

"""
Definition of the TrackerConfig
"""

import logging
from typing import List, Optional

import related
from attr import define
from config_builder import BaseConfigClass

logger = logging.getLogger(__name__)


@define
class TrackingToolTrackerConfigObjectSpeed(BaseConfigClass):
    """
    Configuration for defining the parameters for the uniform motion model
    of a ImageTrack. It is used to define a radius where an object could have
    been moved while ImageTrack got no sensor updated.

    The motion model is defined by:
    s = v*t + s0

    v:= pixel speed per frame (take into account that this could be different for different images sizes
    s0:= constant pixel distance a track can travel

    The speed is the pixel distance between the centers of two consecutive track bounding boxes
    """

    v: int = related.IntegerField(required=False, default=1)
    s_0: int = related.IntegerField(required=False, default=0)


@define
class KalmanFilterConfig(BaseConfigClass):
    """Kalman filter related parameter

    Args:
        R: Constant that is multiplied with the kalman_filter.R matrix.
           It is representing the measurement uncertainty/noise
        P: Constant that is multiplied with the kalman_filter.P matrix.
           It is representing the covariance matrix
        kalman_delay: Use the bounding-boxes for <kalman_delay> frames as tracker positions
                      instead of the position from the filter.
                      Reason: We need some detections to be able to estimate a good speed.
    """

    R: int = related.IntegerField(required=False, default=1000)
    P: int = related.IntegerField(required=False, default=10)

    kalman_delay: int = related.IntegerField(required=False, default=10)


@define
class DistanceCostConfig(BaseConfigClass):
    weight: float = related.FloatField(required=False, default=1.0)

    obj_speed: TrackingToolTrackerConfigObjectSpeed = related.ChildField(
        cls=TrackingToolTrackerConfigObjectSpeed,
        required=False,
        default=TrackingToolTrackerConfigObjectSpeed(),
    )


@define
class IoUCostConfig(BaseConfigClass):
    weight: float = related.FloatField(required=False, default=1.0)


@define
class ColorCostConfig(BaseConfigClass):
    # Color histogram related parameter
    weight: float = related.FloatField(required=False, default=0.0)

    # Margin for cropping the image
    margin_x: float = related.FloatField(required=False, default=0.5)
    margin_y: float = related.FloatField(required=False, default=0.5)
    # Alpha value for the histogram
    color_filter_alpha: float = related.FloatField(required=False, default=0)


@define
class AssignmentCostConfig(BaseConfigClass):
    color_cost: ColorCostConfig = related.ChildField(
        cls=ColorCostConfig, required=False, default=ColorCostConfig()
    )

    distance_cost: DistanceCostConfig = related.ChildField(
        cls=DistanceCostConfig, required=False, default=DistanceCostConfig()
    )

    iou_cost: IoUCostConfig = related.ChildField(
        cls=IoUCostConfig, required=False, default=IoUCostConfig()
    )

    # Threshold for the total weights that determining if a
    # bounding-box should be assigned to a track, sum of:
    # - IoU costs,
    # - Color Histogram costs
    # - Distance costs
    assignment_threshold: float = related.FloatField(required=False, default=1.5)


@define
class TrackerConfig(BaseConfigClass):
    kalman_filter_config: KalmanFilterConfig = related.ChildField(
        cls=KalmanFilterConfig, required=False, default=KalmanFilterConfig()
    )

    assignment_cost_config: AssignmentCostConfig = related.ChildField(
        cls=AssignmentCostConfig, required=False, default=AssignmentCostConfig()
    )

    # Minimum amount of bounding-box sensor updates for a track to be ACTIVE
    min_detections_active: int = related.IntegerField(required=False, default=5)

    # The maximum number of frames a track is allowed to get no sensor updates.
    # If this value is exceeded, the track is counted as DEAD
    max_age: int = related.IntegerField(required=False, default=20)

    # Whether to keep ImageTracks with the state DEAD
    keep_dead_tracks: bool = related.BooleanField(required=False, default=True)

    # The maximum number of TrackEvents that are kept in ImageTrack.__track_events.
    # None means ImageTrack.__track_events will not be managed.
    # REMARK: Type has to float in order to be able to pass .inf as value for infinity, which means
    #         that the dictionary will grow infinitely.
    max_number_track_events: Optional[float] = related.ChildField(
        cls=float, required=False, default=None
    )

    def check_values(self) -> bool:
        if self.min_detections_active < 0:
            logger.error("The minimum value for min_detections_active is zero.")
            return False

        if self.max_age < 0:
            logger.error(
                "The minimum value for max_age is zero. In this case, a sensor update is "
                "required in each iteration to keep the trace alive."
            )
            return False

        return True
