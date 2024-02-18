from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InfoResponse(_message.Message):
    __slots__ = ["common_name", "version", "git_commit", "build_time", "firmware_version"]
    COMMON_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIME_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    common_name: str
    version: str
    git_commit: str
    build_time: str
    firmware_version: str
    def __init__(self, common_name: _Optional[str] = ..., version: _Optional[str] = ..., git_commit: _Optional[str] = ..., build_time: _Optional[str] = ..., firmware_version: _Optional[str] = ...) -> None: ...
