import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Blue: ConeType
DESCRIPTOR: _descriptor.FileDescriptor
Orange: ConeType
OrangeBig: ConeType
UnknownType: ConeType
Yellow: ConeType

class BoundingBox(_message.Message):
    __slots__ = ["cone_id", "frame_position", "height", "length", "position", "type", "width"]
    CONE_ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_POSITION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    cone_id: int
    frame_position: FramePosition
    height: float
    length: float
    position: _common_pb2.Vector3D
    type: ConeType
    width: float
    def __init__(self, cone_id: _Optional[int] = ..., type: _Optional[_Union[ConeType, str]] = ..., height: _Optional[float] = ..., width: _Optional[float] = ..., length: _Optional[float] = ..., frame_position: _Optional[_Union[FramePosition, _Mapping]] = ..., position: _Optional[_Union[_common_pb2.Vector3D, _Mapping]] = ...) -> None: ...

class Cone(_message.Message):
    __slots__ = ["cone_id", "confidence", "type", "x", "y", "z"]
    CONE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    cone_id: int
    confidence: float
    type: ConeType
    x: float
    y: float
    z: float
    def __init__(self, cone_id: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., type: _Optional[_Union[ConeType, str]] = ..., confidence: _Optional[float] = ...) -> None: ...

class ConeMap(_message.Message):
    __slots__ = ["cones"]
    CONES_FIELD_NUMBER: _ClassVar[int]
    cones: _containers.RepeatedCompositeFieldContainer[Cone]
    def __init__(self, cones: _Optional[_Iterable[_Union[Cone, _Mapping]]] = ...) -> None: ...

class FramePosition(_message.Message):
    __slots__ = ["depth", "u", "v"]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    U_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    depth: int
    u: int
    v: int
    def __init__(self, u: _Optional[int] = ..., v: _Optional[int] = ..., depth: _Optional[int] = ...) -> None: ...

class PerceptionGroundTruth(_message.Message):
    __slots__ = ["bbs", "has_bounding_boxes_truth"]
    BBS_FIELD_NUMBER: _ClassVar[int]
    HAS_BOUNDING_BOXES_TRUTH_FIELD_NUMBER: _ClassVar[int]
    bbs: _containers.RepeatedCompositeFieldContainer[BoundingBox]
    has_bounding_boxes_truth: bool
    def __init__(self, has_bounding_boxes_truth: bool = ..., bbs: _Optional[_Iterable[_Union[BoundingBox, _Mapping]]] = ...) -> None: ...

class ConeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
