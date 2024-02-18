from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FIRMWARE_UPDATE_STATUS_UNKNOWN: _ClassVar[FirmwareUpdateStatus]
    FIRMWARE_UPDATE_STATUS_IN_PROGRESS: _ClassVar[FirmwareUpdateStatus]
    FIRMWARE_UPDATE_STATUS_COMPLETE: _ClassVar[FirmwareUpdateStatus]
    FIRMWARE_UPDATE_STATUS_FAILED: _ClassVar[FirmwareUpdateStatus]
    FIRMWARE_UPDATE_STATUS_UP_TO_DATE: _ClassVar[FirmwareUpdateStatus]
FIRMWARE_UPDATE_STATUS_UNKNOWN: FirmwareUpdateStatus
FIRMWARE_UPDATE_STATUS_IN_PROGRESS: FirmwareUpdateStatus
FIRMWARE_UPDATE_STATUS_COMPLETE: FirmwareUpdateStatus
FIRMWARE_UPDATE_STATUS_FAILED: FirmwareUpdateStatus
FIRMWARE_UPDATE_STATUS_UP_TO_DATE: FirmwareUpdateStatus

class FirmwareChunk(_message.Message):
    __slots__ = ["data", "index"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    index: int
    def __init__(self, data: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

class FirmwareChunkAck(_message.Message):
    __slots__ = ["filename"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class FirmwareUpgradeRequest(_message.Message):
    __slots__ = ["filename", "sha256"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    filename: str
    sha256: str
    def __init__(self, filename: _Optional[str] = ..., sha256: _Optional[str] = ...) -> None: ...

class FirmwareUpgradeAck(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FirmwareUpdateRequest(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class FirmwareUpdateResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FirmwareLatestVersionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FirmwareLatestVersionResponse(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class FirmwareUpdateStatusReport(_message.Message):
    __slots__ = ["status", "progress", "version"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: FirmwareUpdateStatus
    progress: int
    version: str
    def __init__(self, status: _Optional[_Union[FirmwareUpdateStatus, str]] = ..., progress: _Optional[int] = ..., version: _Optional[str] = ...) -> None: ...
