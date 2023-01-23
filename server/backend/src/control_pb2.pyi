from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DriveInstructions(_message.Message):
    __slots__ = ["brakes", "gas", "optimal_speed", "steering"]
    BRAKES_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    OPTIMAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    STEERING_FIELD_NUMBER: _ClassVar[int]
    brakes: float
    gas: float
    optimal_speed: float
    steering: float
    def __init__(self, gas: _Optional[float] = ..., brakes: _Optional[float] = ..., steering: _Optional[float] = ..., optimal_speed: _Optional[float] = ...) -> None: ...
