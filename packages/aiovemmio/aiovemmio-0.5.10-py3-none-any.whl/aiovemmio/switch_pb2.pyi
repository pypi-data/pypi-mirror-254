from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SWITCH_UNKNOWN: _ClassVar[SwitchValue]
    SWITCH_ON: _ClassVar[SwitchValue]
    SWITCH_OFF: _ClassVar[SwitchValue]
SWITCH_UNKNOWN: SwitchValue
SWITCH_ON: SwitchValue
SWITCH_OFF: SwitchValue

class SwitchRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class SwitchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SwitchReport(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: SwitchValue
    def __init__(self, value: _Optional[_Union[SwitchValue, str]] = ...) -> None: ...
