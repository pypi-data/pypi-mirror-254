from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StructureRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StructureResponse(_message.Message):
    __slots__ = ["structure"]
    STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    structure: StructureReport
    def __init__(self, structure: _Optional[_Union[StructureReport, _Mapping]] = ...) -> None: ...

class StructureReport(_message.Message):
    __slots__ = ["mac", "type", "revision", "nodes"]
    MAC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    mac: str
    type: str
    revision: str
    nodes: _containers.RepeatedCompositeFieldContainer[StructureNode]
    def __init__(self, mac: _Optional[str] = ..., type: _Optional[str] = ..., revision: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[StructureNode, _Mapping]]] = ...) -> None: ...

class StructureNode(_message.Message):
    __slots__ = ["uuid", "capabilities"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    uuid: bytes
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[bytes] = ..., capabilities: _Optional[_Iterable[str]] = ...) -> None: ...
