from google.protobuf import duration_pb2 as _duration_pb2
from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColorComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COLOR_UNSPECIFIED: _ClassVar[ColorComponent]
    COLOR_WARM_WHITE: _ClassVar[ColorComponent]
    COLOR_COLD_WHITE: _ClassVar[ColorComponent]
    COLOR_RED: _ClassVar[ColorComponent]
    COLOR_GREEN: _ClassVar[ColorComponent]
    COLOR_BLUE: _ClassVar[ColorComponent]
COLOR_UNSPECIFIED: ColorComponent
COLOR_WARM_WHITE: ColorComponent
COLOR_COLD_WHITE: ColorComponent
COLOR_RED: ColorComponent
COLOR_GREEN: ColorComponent
COLOR_BLUE: ColorComponent

class ColorSetRequest(_message.Message):
    __slots__ = ["metadata", "values", "duration"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    values: _containers.RepeatedCompositeFieldContainer[ColorValue]
    duration: _duration_pb2.Duration
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., values: _Optional[_Iterable[_Union[ColorValue, _Mapping]]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ColorResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ColorReport(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[ColorValue]
    def __init__(self, values: _Optional[_Iterable[_Union[ColorValue, _Mapping]]] = ...) -> None: ...

class ColorValue(_message.Message):
    __slots__ = ["component", "value"]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    component: ColorComponent
    value: int
    def __init__(self, component: _Optional[_Union[ColorComponent, str]] = ..., value: _Optional[int] = ...) -> None: ...
