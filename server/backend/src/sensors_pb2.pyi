import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DCH_Float32: DepthCameraDataType
DCS_UInt16: DepthCameraDataType
DESCRIPTOR: _descriptor.FileDescriptor

class CameraConfig(_message.Message):
    __slots__ = ["hfov", "sensor_id", "sensor_position", "vfov"]
    HFOV_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    SENSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    VFOV_FIELD_NUMBER: _ClassVar[int]
    hfov: float
    sensor_id: int
    sensor_position: _common_pb2.Vector3D
    vfov: float
    def __init__(self, sensor_id: _Optional[int] = ..., sensor_position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., hfov: _Optional[float] = ..., vfov: _Optional[float] = ...) -> None: ...

class CameraSensor(_message.Message):
    __slots__ = ["config", "frame_number", "height", "pixels", "width"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PIXELS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    config: CameraConfig
    frame_number: int
    height: int
    pixels: bytes
    width: int
    def __init__(self, config: _Optional[_Union[CameraConfig, _Mapping]] = ..., frame_number: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., pixels: _Optional[bytes] = ...) -> None: ...

class CarData(_message.Message):
    __slots__ = ["car_measurments", "imu_sensor"]
    CAR_MEASURMENTS_FIELD_NUMBER: _ClassVar[int]
    IMU_SENSOR_FIELD_NUMBER: _ClassVar[int]
    car_measurments: CarMeasurments
    imu_sensor: IMUSensor
    def __init__(self, imu_sensor: _Optional[_Union[IMUSensor, _Mapping]] = ..., car_measurments: _Optional[_Union[CarMeasurments, _Mapping]] = ...) -> None: ...

class CarMeasurments(_message.Message):
    __slots__ = ["brakes_position", "steering_angle", "throttle_position", "wheel_velocity_front_left", "wheel_velocity_front_right", "wheel_velocity_rear_left", "wheel_velocity_rear_right"]
    BRAKES_POSITION_FIELD_NUMBER: _ClassVar[int]
    STEERING_ANGLE_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_POSITION_FIELD_NUMBER: _ClassVar[int]
    WHEEL_VELOCITY_FRONT_LEFT_FIELD_NUMBER: _ClassVar[int]
    WHEEL_VELOCITY_FRONT_RIGHT_FIELD_NUMBER: _ClassVar[int]
    WHEEL_VELOCITY_REAR_LEFT_FIELD_NUMBER: _ClassVar[int]
    WHEEL_VELOCITY_REAR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    brakes_position: float
    steering_angle: float
    throttle_position: float
    wheel_velocity_front_left: float
    wheel_velocity_front_right: float
    wheel_velocity_rear_left: float
    wheel_velocity_rear_right: float
    def __init__(self, wheel_velocity_rear_left: _Optional[float] = ..., wheel_velocity_rear_right: _Optional[float] = ..., wheel_velocity_front_left: _Optional[float] = ..., wheel_velocity_front_right: _Optional[float] = ..., throttle_position: _Optional[float] = ..., steering_angle: _Optional[float] = ..., brakes_position: _Optional[float] = ...) -> None: ...

class DepthCameraConfig(_message.Message):
    __slots__ = ["data_type", "hfov", "sensor_id", "sensor_position", "vfov"]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    HFOV_FIELD_NUMBER: _ClassVar[int]
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    SENSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    VFOV_FIELD_NUMBER: _ClassVar[int]
    data_type: DepthCameraDataType
    hfov: float
    sensor_id: int
    sensor_position: _common_pb2.Vector3D
    vfov: float
    def __init__(self, sensor_id: _Optional[int] = ..., sensor_position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., hfov: _Optional[float] = ..., vfov: _Optional[float] = ..., data_type: _Optional[_Union[DepthCameraDataType, str]] = ...) -> None: ...

class DepthCameraSensor(_message.Message):
    __slots__ = ["config", "frame_number", "height", "pixels", "width"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PIXELS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    config: DepthCameraConfig
    frame_number: int
    height: int
    pixels: bytes
    width: int
    def __init__(self, config: _Optional[_Union[DepthCameraConfig, _Mapping]] = ..., frame_number: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., pixels: _Optional[bytes] = ...) -> None: ...

class GPSConfig(_message.Message):
    __slots__ = ["sensor_id", "sensor_position"]
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    SENSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    sensor_id: int
    sensor_position: _common_pb2.Vector3D
    def __init__(self, sensor_id: _Optional[int] = ..., sensor_position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ...) -> None: ...

class GPSSensor(_message.Message):
    __slots__ = ["config", "position"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    config: GPSConfig
    position: _common_pb2.Vector3D
    def __init__(self, config: _Optional[_Union[GPSConfig, _Mapping]] = ..., position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ...) -> None: ...

class IMUConfig(_message.Message):
    __slots__ = ["sensor_id", "sensor_position"]
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    SENSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    sensor_id: int
    sensor_position: _common_pb2.Vector3D
    def __init__(self, sensor_id: _Optional[int] = ..., sensor_position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ...) -> None: ...

class IMUMeasurments(_message.Message):
    __slots__ = ["acceleration", "angular_acceleration", "angular_velocity", "orientation", "speed", "velocity"]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    acceleration: _common_pb2.Vector3D
    angular_acceleration: _common_pb2.Vector3D
    angular_velocity: _common_pb2.Vector3D
    orientation: _common_pb2.Vector3D
    speed: float
    velocity: _common_pb2.Vector3D
    def __init__(self, acceleration: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., angular_acceleration: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., velocity: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., angular_velocity: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., orientation: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ..., speed: _Optional[float] = ...) -> None: ...

class IMUSensor(_message.Message):
    __slots__ = ["config", "imu_measurments"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    IMU_MEASURMENTS_FIELD_NUMBER: _ClassVar[int]
    config: IMUConfig
    imu_measurments: IMUMeasurments
    def __init__(self, config: _Optional[_Union[IMUConfig, _Mapping]] = ..., imu_measurments: _Optional[_Union[IMUMeasurments, _Mapping]] = ...) -> None: ...

class DepthCameraDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
