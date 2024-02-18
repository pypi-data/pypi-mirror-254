from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoorEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DOOR_EVENT_INTRUSION: _ClassVar[DoorEvent]
    DOOR_EVENT_HARD_KNOCK: _ClassVar[DoorEvent]
    DOOR_EVENT_KNOCK: _ClassVar[DoorEvent]
DOOR_EVENT_INTRUSION: DoorEvent
DOOR_EVENT_HARD_KNOCK: DoorEvent
DOOR_EVENT_KNOCK: DoorEvent

class DoorReport(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: DoorEvent
    def __init__(self, event: _Optional[_Union[DoorEvent, str]] = ...) -> None: ...
