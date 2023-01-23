from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CONTROL_MODULE: Module
DESCRIPTOR: _descriptor.FileDescriptor
MISSION_EIGHT: Mission
MISSION_ENDURENCE: Mission
MISSION_MANUAL: Mission
MISSION_STRAIGHT_LINE: Mission
MISSION_UNKNOWN: Mission
PERCEPTION_MODULE: Module
REAL_TIME_DATA_MODULE: Module
SERVER: Module
STATE_EST_MODULE: Module
UNKNOWN_MODULE: Module

class Header(_message.Message):
    __slots__ = ["id", "priority", "source", "steady_timestamp", "timestamp", "triggers"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STEADY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    priority: int
    source: Module
    steady_timestamp: _timestamp_pb2.Timestamp
    timestamp: _timestamp_pb2.Timestamp
    triggers: _containers.RepeatedCompositeFieldContainer[TriggerMessage]
    def __init__(self, id: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., steady_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[_Union[Module, str]] = ..., triggers: _Optional[_Iterable[_Union[TriggerMessage, _Mapping]]] = ..., priority: _Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["data", "header"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    data: _any_pb2.Any
    header: Header
    def __init__(self, header: _Optional[_Union[Header, _Mapping]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class TriggerMessage(_message.Message):
    __slots__ = ["id", "type_url"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    id: int
    type_url: str
    def __init__(self, type_url: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class Vector2D(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Vector3D(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Module(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Mission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
