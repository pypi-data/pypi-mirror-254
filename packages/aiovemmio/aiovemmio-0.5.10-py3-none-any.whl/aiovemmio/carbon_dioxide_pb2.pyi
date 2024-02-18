from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CarbonDioxideState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CARBON_DIOXIDE_STATE_UNSPECIFIED: _ClassVar[CarbonDioxideState]
    CARBON_DIOXIDE_STATE_CLEAR: _ClassVar[CarbonDioxideState]
    CARBON_DIOXIDE_STATE_DETECTED: _ClassVar[CarbonDioxideState]
    CARBON_DIOXIDE_STATE_TEST: _ClassVar[CarbonDioxideState]
    CARBON_DIOXIDE_STATE_SILENCED: _ClassVar[CarbonDioxideState]
    CARBON_DIOXIDE_STATE_REPLACEMENT_REQUIRED: _ClassVar[CarbonDioxideState]
    CARBON_DIOXIDE_STATE_MAINTENANCE_REQUIRED: _ClassVar[CarbonDioxideState]

class CarbonDioxideReplacement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CARBON_DIOXIDE_REPLACEMENT_UNSPECIFIED: _ClassVar[CarbonDioxideReplacement]
    CARBON_DIOXIDE_REPLACEMENT_EOL: _ClassVar[CarbonDioxideReplacement]

class CarbonDioxideMaintenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CARBON_DIOXIDE_MAINTENANCE_UNSPECIFIED: _ClassVar[CarbonDioxideMaintenance]
    CARBON_DIOXIDE_MAINTENANCE_PERIODIC_INSPECTION: _ClassVar[CarbonDioxideMaintenance]
CARBON_DIOXIDE_STATE_UNSPECIFIED: CarbonDioxideState
CARBON_DIOXIDE_STATE_CLEAR: CarbonDioxideState
CARBON_DIOXIDE_STATE_DETECTED: CarbonDioxideState
CARBON_DIOXIDE_STATE_TEST: CarbonDioxideState
CARBON_DIOXIDE_STATE_SILENCED: CarbonDioxideState
CARBON_DIOXIDE_STATE_REPLACEMENT_REQUIRED: CarbonDioxideState
CARBON_DIOXIDE_STATE_MAINTENANCE_REQUIRED: CarbonDioxideState
CARBON_DIOXIDE_REPLACEMENT_UNSPECIFIED: CarbonDioxideReplacement
CARBON_DIOXIDE_REPLACEMENT_EOL: CarbonDioxideReplacement
CARBON_DIOXIDE_MAINTENANCE_UNSPECIFIED: CarbonDioxideMaintenance
CARBON_DIOXIDE_MAINTENANCE_PERIODIC_INSPECTION: CarbonDioxideMaintenance

class CarbonDioxideReport(_message.Message):
    __slots__ = ["state", "replacement", "maintenance"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    state: CarbonDioxideState
    replacement: CarbonDioxideReplacement
    maintenance: CarbonDioxideMaintenance
    def __init__(self, state: _Optional[_Union[CarbonDioxideState, str]] = ..., replacement: _Optional[_Union[CarbonDioxideReplacement, str]] = ..., maintenance: _Optional[_Union[CarbonDioxideMaintenance, str]] = ...) -> None: ...
