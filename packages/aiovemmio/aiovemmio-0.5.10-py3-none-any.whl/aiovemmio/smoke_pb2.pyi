from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmokeDetectorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SMOKE_STATE_UNSPECIFIED: _ClassVar[SmokeDetectorState]
    SMOKE_STATE_CLEAR: _ClassVar[SmokeDetectorState]
    SMOKE_STATE_DETECTED: _ClassVar[SmokeDetectorState]
    SMOKE_STATE_TEST: _ClassVar[SmokeDetectorState]
    SMOKE_STATE_SILENCED: _ClassVar[SmokeDetectorState]
    SMOKE_STATE_REPLACEMENT_REQUIRED: _ClassVar[SmokeDetectorState]
    SMOKE_STATE_MAINTENANCE_REQUIRED: _ClassVar[SmokeDetectorState]

class SmokeDetectorReplacement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SMOKE_REPLACEMENT_UNSPECIFIED: _ClassVar[SmokeDetectorReplacement]
    SMOKE_REPLACEMENT_EOL: _ClassVar[SmokeDetectorReplacement]

class SmokeDetectorMaintenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SMOKE_MAINTENANCE_UNSPECIFIED: _ClassVar[SmokeDetectorMaintenance]
    SMOKE_MAINTENANCE_PERIODIC_INSPECTION: _ClassVar[SmokeDetectorMaintenance]
    SMOKE_MAINTENANCE_DUST_IN_DEVICE: _ClassVar[SmokeDetectorMaintenance]
SMOKE_STATE_UNSPECIFIED: SmokeDetectorState
SMOKE_STATE_CLEAR: SmokeDetectorState
SMOKE_STATE_DETECTED: SmokeDetectorState
SMOKE_STATE_TEST: SmokeDetectorState
SMOKE_STATE_SILENCED: SmokeDetectorState
SMOKE_STATE_REPLACEMENT_REQUIRED: SmokeDetectorState
SMOKE_STATE_MAINTENANCE_REQUIRED: SmokeDetectorState
SMOKE_REPLACEMENT_UNSPECIFIED: SmokeDetectorReplacement
SMOKE_REPLACEMENT_EOL: SmokeDetectorReplacement
SMOKE_MAINTENANCE_UNSPECIFIED: SmokeDetectorMaintenance
SMOKE_MAINTENANCE_PERIODIC_INSPECTION: SmokeDetectorMaintenance
SMOKE_MAINTENANCE_DUST_IN_DEVICE: SmokeDetectorMaintenance

class SmokeReport(_message.Message):
    __slots__ = ["state", "replacement", "maintenance"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    state: SmokeDetectorState
    replacement: SmokeDetectorReplacement
    maintenance: SmokeDetectorMaintenance
    def __init__(self, state: _Optional[_Union[SmokeDetectorState, str]] = ..., replacement: _Optional[_Union[SmokeDetectorReplacement, str]] = ..., maintenance: _Optional[_Union[SmokeDetectorMaintenance, str]] = ...) -> None: ...
