import perception_pb2 as _perception_pb2
import state_est_pb2 as _state_est_pb2
import sensors_pb2 as _sensors_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroundTruth(_message.Message):
    __slots__ = ["frame_number", "perception_ground_truth", "state_ground_truth"]
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PERCEPTION_GROUND_TRUTH_FIELD_NUMBER: _ClassVar[int]
    STATE_GROUND_TRUTH_FIELD_NUMBER: _ClassVar[int]
    frame_number: int
    perception_ground_truth: _perception_pb2.PerceptionGroundTruth
    state_ground_truth: StateGroundTruth
    def __init__(self, frame_number: _Optional[int] = ..., state_ground_truth: _Optional[_Union[StateGroundTruth, _Mapping]] = ..., perception_ground_truth: _Optional[_Union[_perception_pb2.PerceptionGroundTruth, _Mapping]] = ...) -> None: ...

class StateGroundTruth(_message.Message):
    __slots__ = ["car_measurments", "cones", "has_car_measurments_truth", "has_cones_truth", "has_imu_measurments_truth", "has_position_truth", "imu_measurments", "position"]
    CAR_MEASURMENTS_FIELD_NUMBER: _ClassVar[int]
    CONES_FIELD_NUMBER: _ClassVar[int]
    HAS_CAR_MEASURMENTS_TRUTH_FIELD_NUMBER: _ClassVar[int]
    HAS_CONES_TRUTH_FIELD_NUMBER: _ClassVar[int]
    HAS_IMU_MEASURMENTS_TRUTH_FIELD_NUMBER: _ClassVar[int]
    HAS_POSITION_TRUTH_FIELD_NUMBER: _ClassVar[int]
    IMU_MEASURMENTS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    car_measurments: _sensors_pb2.CarMeasurments
    cones: _containers.RepeatedCompositeFieldContainer[_state_est_pb2.StateCone]
    has_car_measurments_truth: bool
    has_cones_truth: bool
    has_imu_measurments_truth: bool
    has_position_truth: bool
    imu_measurments: _sensors_pb2.IMUMeasurments
    position: _common_pb2.Vector3D
    def __init__(self, has_position_truth: bool = ..., position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., has_car_measurments_truth: bool = ..., car_measurments: _Optional[_Union[_sensors_pb2.CarMeasurments, _Mapping]] = ..., has_imu_measurments_truth: bool = ..., imu_measurments: _Optional[_Union[_sensors_pb2.IMUMeasurments, _Mapping]] = ..., has_cones_truth: bool = ..., cones: _Optional[_Iterable[_Union[_state_est_pb2.StateCone, _Mapping]]] = ...) -> None: ...
