from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RebootRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RebootResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RestartRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RestartResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SupportRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SupportResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
