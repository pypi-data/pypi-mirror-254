from aiovemmio import units_pb2 as _units_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HumidityReport(_message.Message):
    __slots__ = ["unit", "value"]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: _units_pb2.Unit
    value: float
    def __init__(self, unit: _Optional[_Union[_units_pb2.Unit, str]] = ..., value: _Optional[float] = ...) -> None: ...

class IlluminationReport(_message.Message):
    __slots__ = ["unit", "value"]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: _units_pb2.Unit
    value: float
    def __init__(self, unit: _Optional[_Union[_units_pb2.Unit, str]] = ..., value: _Optional[float] = ...) -> None: ...

class DirectionReport(_message.Message):
    __slots__ = ["unit", "value"]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: _units_pb2.Unit
    value: int
    def __init__(self, unit: _Optional[_Union[_units_pb2.Unit, str]] = ..., value: _Optional[int] = ...) -> None: ...
