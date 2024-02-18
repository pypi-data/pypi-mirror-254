from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TamperState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TAMPER_COVER_REMOVED: _ClassVar[TamperState]
    TAMPER_INVALID_CODE: _ClassVar[TamperState]
    TAMPER_MOVED: _ClassVar[TamperState]
TAMPER_COVER_REMOVED: TamperState
TAMPER_INVALID_CODE: TamperState
TAMPER_MOVED: TamperState

class TamperReport(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: TamperState
    def __init__(self, state: _Optional[_Union[TamperState, str]] = ...) -> None: ...
