from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RollerShutterRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class RollerShutterSetRequest(_message.Message):
    __slots__ = ["metadata", "level"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    level: int
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., level: _Optional[int] = ...) -> None: ...

class RollerShutterResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RollerShutterLevelReport(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...
