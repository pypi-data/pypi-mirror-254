from aiovemmio import metadata_pb2 as _metadata_pb2
from aiovemmio import units_pb2 as _units_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemperatureGetRequest(_message.Message):
    __slots__ = ["metadata", "refresh"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    refresh: bool
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., refresh: bool = ...) -> None: ...

class TemperatureGetResponse(_message.Message):
    __slots__ = ["unit", "value"]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: _units_pb2.Unit
    value: float
    def __init__(self, unit: _Optional[_Union[_units_pb2.Unit, str]] = ..., value: _Optional[float] = ...) -> None: ...

class TemperatureReport(_message.Message):
    __slots__ = ["unit", "value"]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: _units_pb2.Unit
    value: float
    def __init__(self, unit: _Optional[_Union[_units_pb2.Unit, str]] = ..., value: _Optional[float] = ...) -> None: ...
