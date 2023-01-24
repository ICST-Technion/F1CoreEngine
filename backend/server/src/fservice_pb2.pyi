from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import state_est_pb2 as _state_est_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageAck(_message.Message):
    __slots__ = ["ackmessage"]
    ACKMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ackmessage: str
    def __init__(self, ackmessage: _Optional[str] = ...) -> None: ...

class NotifySimulationEnd(_message.Message):
    __slots__ = ["simulationid"]
    SIMULATIONID_FIELD_NUMBER: _ClassVar[int]
    simulationid: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, simulationid: _Optional[int] = ...) -> None: ...

class SimulationStartRequest(_message.Message):
    __slots__ = ["simulationid"]
    SIMULATIONID_FIELD_NUMBER: _ClassVar[int]
    simulationid: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, simulationid: _Optional[int] = ...) -> None: ...

class TimedDriveInstructions(_message.Message):
    __slots__ = ["brakes", "gas", "optimal_speed", "steering", "time_stamp"]
    BRAKES_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    OPTIMAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    STEERING_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    brakes: float
    gas: float
    optimal_speed: float
    steering: float
    time_stamp: float
    def __init__(self, gas: _Optional[float] = ..., brakes: _Optional[float] = ..., steering: _Optional[float] = ..., optimal_speed: _Optional[float] = ..., time_stamp: _Optional[float] = ...) -> None: ...
