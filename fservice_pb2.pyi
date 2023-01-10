import sensors_pb2 as _sensors_pb2
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
    def __init__(self, simulationid: _Optional[int] = ...) -> None: ...

class SimulationStartRequest(_message.Message):
    __slots__ = ["simulationid"]
    SIMULATIONID_FIELD_NUMBER: _ClassVar[int]
    simulationid: int
    def __init__(self, simulationid: _Optional[int] = ...) -> None: ...
