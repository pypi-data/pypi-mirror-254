from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SirenGetTonesRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class SirenGetTonesResponse(_message.Message):
    __slots__ = ["tones"]
    TONES_FIELD_NUMBER: _ClassVar[int]
    tones: _containers.RepeatedCompositeFieldContainer[SirenTone]
    def __init__(self, tones: _Optional[_Iterable[_Union[SirenTone, _Mapping]]] = ...) -> None: ...

class SirenPlayToneRequest(_message.Message):
    __slots__ = ["metadata", "tone_index"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TONE_INDEX_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    tone_index: int
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., tone_index: _Optional[int] = ...) -> None: ...

class SirenPlayToneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SirenPlayDefaultToneRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class SirenPlayDefaultToneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SirenGetDefaultToneRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class SirenGetDefaultToneResponse(_message.Message):
    __slots__ = ["tone"]
    TONE_FIELD_NUMBER: _ClassVar[int]
    tone: SirenTone
    def __init__(self, tone: _Optional[_Union[SirenTone, _Mapping]] = ...) -> None: ...

class SirenSetDefaultToneRequest(_message.Message):
    __slots__ = ["metadata", "tone_index"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TONE_INDEX_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    tone_index: int
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., tone_index: _Optional[int] = ...) -> None: ...

class SirenSetDefaultToneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SirenGetVolumeRequest(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ...) -> None: ...

class SirenGetVolumeResponse(_message.Message):
    __slots__ = ["volume"]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    volume: int
    def __init__(self, volume: _Optional[int] = ...) -> None: ...

class SirenSetVolumeRequest(_message.Message):
    __slots__ = ["metadata", "volume"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    volume: int
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., volume: _Optional[int] = ...) -> None: ...

class SirenSetVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SirenTone(_message.Message):
    __slots__ = ["index", "label"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    index: int
    label: str
    def __init__(self, index: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class SirenReport(_message.Message):
    __slots__ = ["state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        CLEAR: _ClassVar[SirenReport.State]
        ACTIVE: _ClassVar[SirenReport.State]
    CLEAR: SirenReport.State
    ACTIVE: SirenReport.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SirenReport.State
    def __init__(self, state: _Optional[_Union[SirenReport.State, str]] = ...) -> None: ...

class ToneReport(_message.Message):
    __slots__ = ["state", "tone_index"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        INACTIVE: _ClassVar[ToneReport.State]
        ACTIVE: _ClassVar[ToneReport.State]
        DEFAULT: _ClassVar[ToneReport.State]
    INACTIVE: ToneReport.State
    ACTIVE: ToneReport.State
    DEFAULT: ToneReport.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    TONE_INDEX_FIELD_NUMBER: _ClassVar[int]
    state: ToneReport.State
    tone_index: int
    def __init__(self, state: _Optional[_Union[ToneReport.State, str]] = ..., tone_index: _Optional[int] = ...) -> None: ...

class VolumeReport(_message.Message):
    __slots__ = ["volume"]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    volume: int
    def __init__(self, volume: _Optional[int] = ...) -> None: ...
