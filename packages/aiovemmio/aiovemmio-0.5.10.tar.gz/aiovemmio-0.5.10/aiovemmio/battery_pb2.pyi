from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatteryGetRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class BatteryGetResponse(_message.Message):
    __slots__ = ["level"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: int
    def __init__(self, level: _Optional[int] = ...) -> None: ...

class BatteryReport(_message.Message):
    __slots__ = ["level"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: int
    def __init__(self, level: _Optional[int] = ...) -> None: ...
