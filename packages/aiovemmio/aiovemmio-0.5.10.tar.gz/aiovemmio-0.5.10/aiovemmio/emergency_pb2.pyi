from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmergencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EMERGENCY_POLICE: _ClassVar[EmergencyType]
    EMERGENCY_FIRE: _ClassVar[EmergencyType]
    EMERGENCY_MEDICAL: _ClassVar[EmergencyType]
EMERGENCY_POLICE: EmergencyType
EMERGENCY_FIRE: EmergencyType
EMERGENCY_MEDICAL: EmergencyType

class EmergencyReport(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: EmergencyType
    def __init__(self, type: _Optional[_Union[EmergencyType, str]] = ...) -> None: ...
