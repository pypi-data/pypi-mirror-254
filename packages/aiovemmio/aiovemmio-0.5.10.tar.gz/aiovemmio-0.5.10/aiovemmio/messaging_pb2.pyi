from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmailMessage(_message.Message):
    __slots__ = ["recipient", "subject", "message"]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    recipient: str
    subject: str
    message: str
    def __init__(self, recipient: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class PushMessage(_message.Message):
    __slots__ = ["token", "message", "badge", "site_id", "site_name"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BADGE_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    token: str
    message: str
    badge: int
    site_id: str
    site_name: str
    def __init__(self, token: _Optional[str] = ..., message: _Optional[str] = ..., badge: _Optional[int] = ..., site_id: _Optional[str] = ..., site_name: _Optional[str] = ...) -> None: ...
