from aiovemmio import pubsub_pb2 as _pubsub_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MQTTCommandRequest(_message.Message):
    __slots__ = ["request", "response_topic"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TOPIC_FIELD_NUMBER: _ClassVar[int]
    request: _pubsub_pb2.CommandRequest
    response_topic: str
    def __init__(self, request: _Optional[_Union[_pubsub_pb2.CommandRequest, _Mapping]] = ..., response_topic: _Optional[str] = ...) -> None: ...
