from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddonListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AddonListResponse(_message.Message):
    __slots__ = ["addons"]
    class Addon(_message.Message):
        __slots__ = ["uuid", "thermostat"]
        UUID_FIELD_NUMBER: _ClassVar[int]
        THERMOSTAT_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        thermostat: AddonThermostat
        def __init__(self, uuid: _Optional[str] = ..., thermostat: _Optional[_Union[AddonThermostat, _Mapping]] = ...) -> None: ...
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    addons: _containers.RepeatedCompositeFieldContainer[AddonListResponse.Addon]
    def __init__(self, addons: _Optional[_Iterable[_Union[AddonListResponse.Addon, _Mapping]]] = ...) -> None: ...

class AddonAddThermostatRequest(_message.Message):
    __slots__ = ["thermostat"]
    THERMOSTAT_FIELD_NUMBER: _ClassVar[int]
    thermostat: AddonThermostat
    def __init__(self, thermostat: _Optional[_Union[AddonThermostat, _Mapping]] = ...) -> None: ...

class AddonAddResponse(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class AddonThermostat(_message.Message):
    __slots__ = ["input_filename", "output_filename"]
    INPUT_FILENAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILENAME_FIELD_NUMBER: _ClassVar[int]
    input_filename: str
    output_filename: str
    def __init__(self, input_filename: _Optional[str] = ..., output_filename: _Optional[str] = ...) -> None: ...
