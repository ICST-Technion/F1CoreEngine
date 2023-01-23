import perception_pb2 as _perception_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
finished_lap: FormulaStateMessageType
only_prediction: FormulaStateMessageType
prediction_and_correction: FormulaStateMessageType
still_calibrating: FormulaStateMessageType

class CarState(_message.Message):
    __slots__ = ["acceleration", "acceleration_deviation", "position", "position_deviation", "steering_angle", "steering_angle_deviation", "theta", "theta_deviation", "theta_dot", "theta_dot_deviation", "velocity", "velocity_deviation"]
    ACCELERATION_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    POSITION_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    STEERING_ANGLE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    STEERING_ANGLE_FIELD_NUMBER: _ClassVar[int]
    THETA_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    THETA_DOT_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    THETA_DOT_FIELD_NUMBER: _ClassVar[int]
    THETA_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    acceleration: float
    acceleration_deviation: float
    position: _common_pb2.Vector2D
    position_deviation: _common_pb2.Vector2D
    steering_angle: float
    steering_angle_deviation: float
    theta: float
    theta_deviation: float
    theta_dot: float
    theta_dot_deviation: float
    velocity: _common_pb2.Vector2D
    velocity_deviation: _common_pb2.Vector2D
    def __init__(self, position: _Optional[_Union[_common_pb2.Vector2D, _Mapping]] = ..., position_deviation: _Optional[_Union[_common_pb2.Vector2D, _Mapping]] = ..., velocity: _Optional[_Union[_common_pb2.Vector2D, _Mapping]] = ..., velocity_deviation: _Optional[_Union[_common_pb2.Vector2D, _Mapping]] = ..., theta: _Optional[float] = ..., theta_deviation: _Optional[float] = ..., theta_dot: _Optional[float] = ..., theta_dot_deviation: _Optional[float] = ..., steering_angle: _Optional[float] = ..., steering_angle_deviation: _Optional[float] = ..., acceleration: _Optional[float] = ..., acceleration_deviation: _Optional[float] = ...) -> None: ...

class ClusterInfo(_message.Message):
    __slots__ = ["age", "extra", "num_of_cones"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_CONES_FIELD_NUMBER: _ClassVar[int]
    age: int
    extra: float
    num_of_cones: int
    def __init__(self, age: _Optional[int] = ..., num_of_cones: _Optional[int] = ..., extra: _Optional[float] = ...) -> None: ...

class FormulaState(_message.Message):
    __slots__ = ["current_state", "distance_from_left", "distance_from_right", "distance_to_finish", "left_bound_cones", "message_type", "right_bound_cones", "road_angle"]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FROM_LEFT_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FROM_RIGHT_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_TO_FINISH_FIELD_NUMBER: _ClassVar[int]
    LEFT_BOUND_CONES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RIGHT_BOUND_CONES_FIELD_NUMBER: _ClassVar[int]
    ROAD_ANGLE_FIELD_NUMBER: _ClassVar[int]
    current_state: CarState
    distance_from_left: float
    distance_from_right: float
    distance_to_finish: float
    left_bound_cones: _containers.RepeatedCompositeFieldContainer[StateCone]
    message_type: FormulaStateMessageType
    right_bound_cones: _containers.RepeatedCompositeFieldContainer[StateCone]
    road_angle: float
    def __init__(self, right_bound_cones: _Optional[_Iterable[_Union[StateCone, _Mapping]]] = ..., left_bound_cones: _Optional[_Iterable[_Union[StateCone, _Mapping]]] = ..., current_state: _Optional[_Union[CarState, _Mapping]] = ..., distance_to_finish: _Optional[float] = ..., message_type: _Optional[_Union[FormulaStateMessageType, str]] = ..., distance_from_left: _Optional[float] = ..., distance_from_right: _Optional[float] = ..., road_angle: _Optional[float] = ...) -> None: ...

class StateCone(_message.Message):
    __slots__ = ["alpha", "cluster_info", "cone_id", "position", "position_deviation", "r", "type"]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    CONE_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    alpha: float
    cluster_info: ClusterInfo
    cone_id: int
    position: _common_pb2.Vector2D
    position_deviation: float
    r: float
    type: _perception_pb2.ConeType
    def __init__(self, cone_id: _Optional[int] = ..., r: _Optional[float] = ..., alpha: _Optional[float] = ..., position: _Optional[_Union[_common_pb2.Vector2D, _Mapping]] = ..., type: _Optional[_Union[_perception_pb2.ConeType, str]] = ..., position_deviation: _Optional[float] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ...) -> None: ...

class FormulaStateMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
