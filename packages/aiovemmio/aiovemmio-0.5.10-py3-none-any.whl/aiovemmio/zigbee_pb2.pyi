from aiovemmio import devices_pb2 as _devices_pb2
from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZigbeeIncludeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZigbeeIncludeResponse(_message.Message):
    __slots__ = ["devices"]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_devices_pb2.Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[_devices_pb2.Device, _Mapping]]] = ...) -> None: ...

class ZigbeeExcludeRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.ZigbeeMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.ZigbeeMetadata, _Mapping]] = ...) -> None: ...

class ZigbeeExcludeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZigbeeNodesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZigbeeNodesResponse(_message.Message):
    __slots__ = ["nodes"]
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ZigbeeNode]
    def __init__(self, nodes: _Optional[_Iterable[_Union[ZigbeeNode, _Mapping]]] = ...) -> None: ...

class ZigbeeNode(_message.Message):
    __slots__ = ["ieee_addr", "eui64_addr", "endpoint", "clusters"]
    IEEE_ADDR_FIELD_NUMBER: _ClassVar[int]
    EUI64_ADDR_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    ieee_addr: int
    eui64_addr: str
    endpoint: int
    clusters: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ieee_addr: _Optional[int] = ..., eui64_addr: _Optional[str] = ..., endpoint: _Optional[int] = ..., clusters: _Optional[_Iterable[int]] = ...) -> None: ...
