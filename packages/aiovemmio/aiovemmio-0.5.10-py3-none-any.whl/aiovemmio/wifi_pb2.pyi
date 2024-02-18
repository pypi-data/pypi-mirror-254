from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WiFiQueryRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WiFiQueryResponse(_message.Message):
    __slots__ = ["interfaces", "timestamp"]
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    interfaces: _containers.RepeatedCompositeFieldContainer[WiFiInterface]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, interfaces: _Optional[_Iterable[_Union[WiFiInterface, _Mapping]]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WiFiScanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WiFiScanResponse(_message.Message):
    __slots__ = ["bsss"]
    BSSS_FIELD_NUMBER: _ClassVar[int]
    bsss: _containers.RepeatedCompositeFieldContainer[WiFiBSS]
    def __init__(self, bsss: _Optional[_Iterable[_Union[WiFiBSS, _Mapping]]] = ...) -> None: ...

class WiFiConnectRequest(_message.Message):
    __slots__ = ["ssid", "psk"]
    SSID_FIELD_NUMBER: _ClassVar[int]
    PSK_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    psk: str
    def __init__(self, ssid: _Optional[str] = ..., psk: _Optional[str] = ...) -> None: ...

class WiFiConnectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WiFiInterface(_message.Message):
    __slots__ = ["name", "hardware_addr", "bss", "stations"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ADDR_FIELD_NUMBER: _ClassVar[int]
    BSS_FIELD_NUMBER: _ClassVar[int]
    STATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    hardware_addr: bytes
    bss: WiFiBSS
    stations: _containers.RepeatedCompositeFieldContainer[WiFiStation]
    def __init__(self, name: _Optional[str] = ..., hardware_addr: _Optional[bytes] = ..., bss: _Optional[_Union[WiFiBSS, _Mapping]] = ..., stations: _Optional[_Iterable[_Union[WiFiStation, _Mapping]]] = ...) -> None: ...

class WiFiBSS(_message.Message):
    __slots__ = ["ssid", "frequency", "last_seen"]
    SSID_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    frequency: int
    last_seen: int
    def __init__(self, ssid: _Optional[str] = ..., frequency: _Optional[int] = ..., last_seen: _Optional[int] = ...) -> None: ...

class WiFiStation(_message.Message):
    __slots__ = ["hardware_addr", "signal", "connected", "inactive"]
    HARDWARE_ADDR_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    hardware_addr: bytes
    signal: int
    connected: int
    inactive: int
    def __init__(self, hardware_addr: _Optional[bytes] = ..., signal: _Optional[int] = ..., connected: _Optional[int] = ..., inactive: _Optional[int] = ...) -> None: ...
