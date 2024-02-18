from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PowerSourceEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CLEAR: _ClassVar[PowerSourceEvent]
    POWER_APPLIED: _ClassVar[PowerSourceEvent]
    AC_POWER_LOST: _ClassVar[PowerSourceEvent]
    AC_POWER_RESTORED: _ClassVar[PowerSourceEvent]
    SURGE_DETECTED: _ClassVar[PowerSourceEvent]
    BROWNOUT_DETECTED: _ClassVar[PowerSourceEvent]
    OVER_CURRENT_DETECTED: _ClassVar[PowerSourceEvent]
    OVER_VOLTAGE_DETECTED: _ClassVar[PowerSourceEvent]
    OVER_LOAD_DETECTED: _ClassVar[PowerSourceEvent]
    LOAD_ERROR: _ClassVar[PowerSourceEvent]
    BATTERY_REPLACE_SOON: _ClassVar[PowerSourceEvent]
    BATTERY_REPLACE_NOW: _ClassVar[PowerSourceEvent]
    BATTERY_CHARGING: _ClassVar[PowerSourceEvent]
    BATTERY_CHARGED: _ClassVar[PowerSourceEvent]
    BATTERY_LOW: _ClassVar[PowerSourceEvent]
    BATTERY_CRITICAL: _ClassVar[PowerSourceEvent]
CLEAR: PowerSourceEvent
POWER_APPLIED: PowerSourceEvent
AC_POWER_LOST: PowerSourceEvent
AC_POWER_RESTORED: PowerSourceEvent
SURGE_DETECTED: PowerSourceEvent
BROWNOUT_DETECTED: PowerSourceEvent
OVER_CURRENT_DETECTED: PowerSourceEvent
OVER_VOLTAGE_DETECTED: PowerSourceEvent
OVER_LOAD_DETECTED: PowerSourceEvent
LOAD_ERROR: PowerSourceEvent
BATTERY_REPLACE_SOON: PowerSourceEvent
BATTERY_REPLACE_NOW: PowerSourceEvent
BATTERY_CHARGING: PowerSourceEvent
BATTERY_CHARGED: PowerSourceEvent
BATTERY_LOW: PowerSourceEvent
BATTERY_CRITICAL: PowerSourceEvent

class PowerSourceReport(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: PowerSourceEvent
    def __init__(self, event: _Optional[_Union[PowerSourceEvent, str]] = ...) -> None: ...
