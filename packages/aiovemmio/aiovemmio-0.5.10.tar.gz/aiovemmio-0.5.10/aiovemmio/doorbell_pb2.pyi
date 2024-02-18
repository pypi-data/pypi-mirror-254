from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoorbellReport(_message.Message):
    __slots__ = ["state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CLEAR: _ClassVar[DoorbellReport.State]
        ACTIVE: _ClassVar[DoorbellReport.State]
    CLEAR: DoorbellReport.State
    ACTIVE: DoorbellReport.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: DoorbellReport.State
    def __init__(self, state: _Optional[_Union[DoorbellReport.State, str]] = ...) -> None: ...
