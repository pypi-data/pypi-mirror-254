from aiovemmio import units_pb2 as _units_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccelerometerAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    X: _ClassVar[AccelerometerAxis]
    Y: _ClassVar[AccelerometerAxis]
    Z: _ClassVar[AccelerometerAxis]
X: AccelerometerAxis
Y: AccelerometerAxis
Z: AccelerometerAxis

class AccelerometerReport(_message.Message):
    __slots__ = ["axis", "unit", "value"]
    AXIS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    axis: AccelerometerAxis
    unit: _units_pb2.Unit
    value: float
    def __init__(self, axis: _Optional[_Union[AccelerometerAxis, str]] = ..., unit: _Optional[_Union[_units_pb2.Unit, str]] = ..., value: _Optional[float] = ...) -> None: ...
