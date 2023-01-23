import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionApproved(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExitMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishedControlLap(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishedFinalLap(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SwitchToASDReady(_message.Message):
    __slots__ = ["mission"]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    mission: _common_pb2.Mission
    def __init__(self, mission: _Optional[_Union[_common_pb2.Mission, str]] = ...) -> None: ...

class SwitchToASDriving(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SwitchToASEmergency(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SwitchToASFinished(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SwitchToASOff(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
