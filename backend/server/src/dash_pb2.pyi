import common_pb2 as _common_pb2
import control_pb2 as _control_pb2
import state_est_pb2 as _state_est_pb2
import perception_pb2 as _perception_pb2
import ground_truth_pb2 as _ground_truth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ControlDashbaord(_message.Message):
    __slots__ = ["current_position", "current_speed", "current_steering_angle", "instructions", "left_bound", "left_bound_cones", "optimal_route", "right_bound", "right_bound_cones"]
    CURRENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SPEED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STEERING_ANGLE_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    LEFT_BOUND_CONES_FIELD_NUMBER: _ClassVar[int]
    LEFT_BOUND_FIELD_NUMBER: _ClassVar[int]
    OPTIMAL_ROUTE_FIELD_NUMBER: _ClassVar[int]
    RIGHT_BOUND_CONES_FIELD_NUMBER: _ClassVar[int]
    RIGHT_BOUND_FIELD_NUMBER: _ClassVar[int]
    current_position: _common_pb2.Vector2D
    current_speed: float
    current_steering_angle: float
    instructions: _control_pb2.DriveInstructions
    left_bound: _containers.RepeatedScalarFieldContainer[float]
    left_bound_cones: _containers.RepeatedCompositeFieldContainer[_state_est_pb2.StateCone]
    optimal_route: _containers.RepeatedScalarFieldContainer[float]
    right_bound: _containers.RepeatedScalarFieldContainer[float]
    right_bound_cones: _containers.RepeatedCompositeFieldContainer[_state_est_pb2.StateCone]
    def __init__(self, instructions: _Optional[_Union[_control_pb2.DriveInstructions, _Mapping]] = ..., current_position: _Optional[_Union[_common_pb2.Vector2D, _Mapping]] = ..., current_steering_angle: _Optional[float] = ..., current_speed: _Optional[float] = ..., optimal_route: _Optional[_Iterable[float]] = ..., right_bound: _Optional[_Iterable[float]] = ..., left_bound: _Optional[_Iterable[float]] = ..., right_bound_cones: _Optional[_Iterable[_Union[_state_est_pb2.StateCone, _Mapping]]] = ..., left_bound_cones: _Optional[_Iterable[_Union[_state_est_pb2.StateCone, _Mapping]]] = ...) -> None: ...

class FormulaStateDash(_message.Message):
    __slots__ = ["cone_clusters", "cone_samples", "formula_state_message", "ground_truth"]
    CONE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    CONE_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    FORMULA_STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GROUND_TRUTH_FIELD_NUMBER: _ClassVar[int]
    cone_clusters: _containers.RepeatedCompositeFieldContainer[_state_est_pb2.StateCone]
    cone_samples: _containers.RepeatedCompositeFieldContainer[_state_est_pb2.StateCone]
    formula_state_message: _state_est_pb2.FormulaState
    ground_truth: _ground_truth_pb2.StateGroundTruth
    def __init__(self, formula_state_message: _Optional[_Union[_state_est_pb2.FormulaState, _Mapping]] = ..., cone_samples: _Optional[_Iterable[_Union[_state_est_pb2.StateCone, _Mapping]]] = ..., cone_clusters: _Optional[_Iterable[_Union[_state_est_pb2.StateCone, _Mapping]]] = ..., ground_truth: _Optional[_Union[_ground_truth_pb2.StateGroundTruth, _Mapping]] = ...) -> None: ...

class PerceptionDash(_message.Message):
    __slots__ = ["bbs", "cone_map"]
    BBS_FIELD_NUMBER: _ClassVar[int]
    CONE_MAP_FIELD_NUMBER: _ClassVar[int]
    bbs: _containers.RepeatedCompositeFieldContainer[_perception_pb2.BoundingBox]
    cone_map: _perception_pb2.ConeMap
    def __init__(self, bbs: _Optional[_Iterable[_Union[_perception_pb2.BoundingBox, _Mapping]]] = ..., cone_map: _Optional[_Union[_perception_pb2.ConeMap, _Mapping]] = ...) -> None: ...
