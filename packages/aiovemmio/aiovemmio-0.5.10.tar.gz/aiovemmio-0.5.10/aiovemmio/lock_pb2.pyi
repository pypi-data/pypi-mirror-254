from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LockMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LOCK_UNSEC: _ClassVar[LockMode]
    LOCK_UNSEC_TMOUT: _ClassVar[LockMode]
    LOCK_UNSEC_IN: _ClassVar[LockMode]
    LOCK_UNSEC_IN_TMOUT: _ClassVar[LockMode]
    LOCK_UNSEC_OUT: _ClassVar[LockMode]
    LOCK_UNSEC_OUT_TMOUT: _ClassVar[LockMode]
    LOCK_UNKNOWN: _ClassVar[LockMode]
    LOCK_SEC: _ClassVar[LockMode]
LOCK_UNSEC: LockMode
LOCK_UNSEC_TMOUT: LockMode
LOCK_UNSEC_IN: LockMode
LOCK_UNSEC_IN_TMOUT: LockMode
LOCK_UNSEC_OUT: LockMode
LOCK_UNSEC_OUT_TMOUT: LockMode
LOCK_UNKNOWN: LockMode
LOCK_SEC: LockMode

class LockSetRequest(_message.Message):
    __slots__ = ["metadata", "mode"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    metadata: _metadata_pb2.DeviceMetadata
    mode: LockMode
    def __init__(self, metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., mode: _Optional[_Union[LockMode, str]] = ...) -> None: ...

class LockResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LockReport(_message.Message):
    __slots__ = ["mode"]
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: LockMode
    def __init__(self, mode: _Optional[_Union[LockMode, str]] = ...) -> None: ...
