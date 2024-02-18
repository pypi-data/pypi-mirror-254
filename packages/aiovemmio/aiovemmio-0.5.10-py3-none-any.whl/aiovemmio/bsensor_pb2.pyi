from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpenCloseState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    OPEN_CLOSE_STATE_OPEN: _ClassVar[OpenCloseState]
    OPEN_CLOSE_STATE_CLOSED: _ClassVar[OpenCloseState]

class BinarySensorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BSENSOR_STATE_IDLE: _ClassVar[BinarySensorState]
    BSENSOR_STATE_EVENT_DETECTED: _ClassVar[BinarySensorState]
OPEN_CLOSE_STATE_OPEN: OpenCloseState
OPEN_CLOSE_STATE_CLOSED: OpenCloseState
BSENSOR_STATE_IDLE: BinarySensorState
BSENSOR_STATE_EVENT_DETECTED: BinarySensorState

class OpenCloseReport(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: OpenCloseState
    def __init__(self, state: _Optional[_Union[OpenCloseState, str]] = ...) -> None: ...

class MotionReport(_message.Message):
    __slots__ = ["state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        IDLE: _ClassVar[MotionReport.State]
        DETECTED: _ClassVar[MotionReport.State]
    IDLE: MotionReport.State
    DETECTED: MotionReport.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: MotionReport.State
    def __init__(self, state: _Optional[_Union[MotionReport.State, str]] = ...) -> None: ...
