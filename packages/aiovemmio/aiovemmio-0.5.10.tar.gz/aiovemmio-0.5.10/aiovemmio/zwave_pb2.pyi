from google.protobuf import wrappers_pb2 as _wrappers_pb2
from aiovemmio import devices_pb2 as _devices_pb2
from aiovemmio import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZWaveHealthCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ZWAVE_HEALTH_UNSPECIFIED: _ClassVar[ZWaveHealthCategory]
    ZWAVE_HEALTH_GREEN: _ClassVar[ZWaveHealthCategory]
    ZWAVE_HEALTH_YELLOW: _ClassVar[ZWaveHealthCategory]
    ZWAVE_HEALTH_RED: _ClassVar[ZWaveHealthCategory]
    ZWAVE_HEALTH_CRITICAL: _ClassVar[ZWaveHealthCategory]

class ZWaveNodeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NODE_STATUS_UNSPECIFIED: _ClassVar[ZWaveNodeStatus]
    NODE_STATUS_ALIVE: _ClassVar[ZWaveNodeStatus]
    NODE_STATUS_DOWN: _ClassVar[ZWaveNodeStatus]
    NODE_STATUS_SLEEP: _ClassVar[ZWaveNodeStatus]
ZWAVE_HEALTH_UNSPECIFIED: ZWaveHealthCategory
ZWAVE_HEALTH_GREEN: ZWaveHealthCategory
ZWAVE_HEALTH_YELLOW: ZWaveHealthCategory
ZWAVE_HEALTH_RED: ZWaveHealthCategory
ZWAVE_HEALTH_CRITICAL: ZWaveHealthCategory
NODE_STATUS_UNSPECIFIED: ZWaveNodeStatus
NODE_STATUS_ALIVE: ZWaveNodeStatus
NODE_STATUS_DOWN: ZWaveNodeStatus
NODE_STATUS_SLEEP: ZWaveNodeStatus

class ZWaveIncludeRequest(_message.Message):
    __slots__ = ["secure"]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    secure: bool
    def __init__(self, secure: bool = ...) -> None: ...

class ZWaveIncludeStatus(_message.Message):
    __slots__ = ["found", "added", "ready", "progress"]
    class DeviceFound(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class DeviceAdded(_message.Message):
        __slots__ = ["devices"]
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[_devices_pb2.Device]
        def __init__(self, devices: _Optional[_Iterable[_Union[_devices_pb2.Device, _Mapping]]] = ...) -> None: ...
    class IncludeReady(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class IncludeProgress(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    FOUND_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    found: ZWaveIncludeStatus.DeviceFound
    added: ZWaveIncludeStatus.DeviceAdded
    ready: ZWaveIncludeStatus.IncludeReady
    progress: ZWaveIncludeStatus.IncludeProgress
    def __init__(self, found: _Optional[_Union[ZWaveIncludeStatus.DeviceFound, _Mapping]] = ..., added: _Optional[_Union[ZWaveIncludeStatus.DeviceAdded, _Mapping]] = ..., ready: _Optional[_Union[ZWaveIncludeStatus.IncludeReady, _Mapping]] = ..., progress: _Optional[_Union[ZWaveIncludeStatus.IncludeProgress, _Mapping]] = ...) -> None: ...

class ZWaveExcludeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveExcludeStatus(_message.Message):
    __slots__ = ["removed", "ready", "progress", "not_found"]
    class DeviceRemoved(_message.Message):
        __slots__ = ["metadata"]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        metadata: _metadata_pb2.ZWaveMetadata
        def __init__(self, metadata: _Optional[_Union[_metadata_pb2.ZWaveMetadata, _Mapping]] = ...) -> None: ...
    class ExcludeReady(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class ExcludeProgress(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class DeviceNotFound(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    removed: ZWaveExcludeStatus.DeviceRemoved
    ready: ZWaveExcludeStatus.ExcludeReady
    progress: ZWaveExcludeStatus.ExcludeProgress
    not_found: ZWaveExcludeStatus.DeviceNotFound
    def __init__(self, removed: _Optional[_Union[ZWaveExcludeStatus.DeviceRemoved, _Mapping]] = ..., ready: _Optional[_Union[ZWaveExcludeStatus.ExcludeReady, _Mapping]] = ..., progress: _Optional[_Union[ZWaveExcludeStatus.ExcludeProgress, _Mapping]] = ..., not_found: _Optional[_Union[ZWaveExcludeStatus.DeviceNotFound, _Mapping]] = ...) -> None: ...

class ZWaveAbortRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveAbortResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveTestRequest(_message.Message):
    __slots__ = ["node_id", "count"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    node_id: _wrappers_pb2.Int32Value
    count: int
    def __init__(self, node_id: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class ZWaveTestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveHealRequest(_message.Message):
    __slots__ = ["node_id", "init_return_routes"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INIT_RETURN_ROUTES_FIELD_NUMBER: _ClassVar[int]
    node_id: _wrappers_pb2.Int32Value
    init_return_routes: bool
    def __init__(self, node_id: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., init_return_routes: bool = ...) -> None: ...

class ZWaveHealResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveReplaceFailedRequest(_message.Message):
    __slots__ = ["node_id"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class ZWaveReplaceFailedResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveRemoveFailedRequest(_message.Message):
    __slots__ = ["node_id"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class ZWaveRemoveFailedResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveHealthCheckRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveHealthCheckStatus(_message.Message):
    __slots__ = ["started", "progress", "completed"]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    started: ZWaveHealthCheckStarted
    progress: ZWaveHealthCheckProgress
    completed: ZWaveHealthCheckCompleted
    def __init__(self, started: _Optional[_Union[ZWaveHealthCheckStarted, _Mapping]] = ..., progress: _Optional[_Union[ZWaveHealthCheckProgress, _Mapping]] = ..., completed: _Optional[_Union[ZWaveHealthCheckCompleted, _Mapping]] = ...) -> None: ...

class ZWaveHealthCheckStarted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveHealthCheckProgress(_message.Message):
    __slots__ = ["count", "total"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    count: int
    total: int
    def __init__(self, count: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...

class ZWaveHealthCheckCompleted(_message.Message):
    __slots__ = ["nodes"]
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ZWaveHealthStatusNode]
    def __init__(self, nodes: _Optional[_Iterable[_Union[ZWaveHealthStatusNode, _Mapping]]] = ...) -> None: ...

class ZWaveHealthStatusNode(_message.Message):
    __slots__ = ["node_id", "category", "value"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    category: ZWaveHealthCategory
    value: int
    def __init__(self, node_id: _Optional[int] = ..., category: _Optional[_Union[ZWaveHealthCategory, str]] = ..., value: _Optional[int] = ...) -> None: ...

class ZWaveNodesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveNodesResponse(_message.Message):
    __slots__ = ["nodes"]
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ZWaveNode]
    def __init__(self, nodes: _Optional[_Iterable[_Union[ZWaveNode, _Mapping]]] = ...) -> None: ...

class ZWaveNodeRequest(_message.Message):
    __slots__ = ["node_id"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class ZWaveNodeResponse(_message.Message):
    __slots__ = ["node"]
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: ZWaveNode
    def __init__(self, node: _Optional[_Union[ZWaveNode, _Mapping]] = ...) -> None: ...

class ZWaveUpdateRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveUpdateStatus(_message.Message):
    __slots__ = ["topology", "neighbor", "node_info"]
    TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    topology: ZWaveNetworkTopologyUpdateStarted
    neighbor: ZWaveNodeNeighborUpdateStarted
    node_info: ZWaveNodeInformationUpdateStarted
    def __init__(self, topology: _Optional[_Union[ZWaveNetworkTopologyUpdateStarted, _Mapping]] = ..., neighbor: _Optional[_Union[ZWaveNodeNeighborUpdateStarted, _Mapping]] = ..., node_info: _Optional[_Union[ZWaveNodeInformationUpdateStarted, _Mapping]] = ...) -> None: ...

class ZWaveNetworkTopologyUpdateStarted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveNodeNeighborUpdateStarted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveNodeInformationUpdateStarted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveUpdateNodeRequest(_message.Message):
    __slots__ = ["node_id"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class ZWaveUpdateNodeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveResetRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveResetResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveNode(_message.Message):
    __slots__ = ["node_id", "vendor_id", "product_type", "product_id", "endpoints", "manufacturer_name", "product_name", "user_name", "status"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    vendor_id: int
    product_type: int
    product_id: int
    endpoints: _containers.RepeatedCompositeFieldContainer[ZWaveEndpoint]
    manufacturer_name: str
    product_name: str
    user_name: str
    status: ZWaveNodeStatus
    def __init__(self, node_id: _Optional[int] = ..., vendor_id: _Optional[int] = ..., product_type: _Optional[int] = ..., product_id: _Optional[int] = ..., endpoints: _Optional[_Iterable[_Union[ZWaveEndpoint, _Mapping]]] = ..., manufacturer_name: _Optional[str] = ..., product_name: _Optional[str] = ..., user_name: _Optional[str] = ..., status: _Optional[_Union[ZWaveNodeStatus, str]] = ...) -> None: ...

class ZWaveEndpoint(_message.Message):
    __slots__ = ["ep_id", "generic_class", "specific_class", "interfaces"]
    EP_ID_FIELD_NUMBER: _ClassVar[int]
    GENERIC_CLASS_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_CLASS_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    ep_id: int
    generic_class: int
    specific_class: int
    interfaces: _containers.RepeatedCompositeFieldContainer[ZWaveInterface]
    def __init__(self, ep_id: _Optional[int] = ..., generic_class: _Optional[int] = ..., specific_class: _Optional[int] = ..., interfaces: _Optional[_Iterable[_Union[ZWaveInterface, _Mapping]]] = ...) -> None: ...

class ZWaveInterface(_message.Message):
    __slots__ = ["command_class", "version", "real_version", "label", "help", "items"]
    COMMAND_CLASS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    command_class: int
    version: int
    real_version: int
    label: str
    help: str
    items: _containers.RepeatedCompositeFieldContainer[ZWaveValueItem]
    def __init__(self, command_class: _Optional[int] = ..., version: _Optional[int] = ..., real_version: _Optional[int] = ..., label: _Optional[str] = ..., help: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ZWaveValueItem, _Mapping]]] = ...) -> None: ...

class ZWaveValueItem(_message.Message):
    __slots__ = ["value", "label"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    value: int
    label: str
    def __init__(self, value: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class ZWaveListEntriesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveListEntriesResponse(_message.Message):
    __slots__ = ["entries"]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[ZWaveProvisioningEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[ZWaveProvisioningEntry, _Mapping]]] = ...) -> None: ...

class ZWaveAddEntryRequest(_message.Message):
    __slots__ = ["dsk", "info"]
    DSK_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    dsk: str
    info: _containers.RepeatedCompositeFieldContainer[ZWaveProvisioningInfo]
    def __init__(self, dsk: _Optional[str] = ..., info: _Optional[_Iterable[_Union[ZWaveProvisioningInfo, _Mapping]]] = ...) -> None: ...

class ZWaveAddEntryResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveRemoveEntryRequest(_message.Message):
    __slots__ = ["dsk"]
    DSK_FIELD_NUMBER: _ClassVar[int]
    dsk: str
    def __init__(self, dsk: _Optional[str] = ...) -> None: ...

class ZWaveRemoveEntryResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ZWaveProvisioningEntry(_message.Message):
    __slots__ = ["dsk", "info"]
    DSK_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    dsk: str
    info: _containers.RepeatedCompositeFieldContainer[ZWaveProvisioningInfo]
    def __init__(self, dsk: _Optional[str] = ..., info: _Optional[_Iterable[_Union[ZWaveProvisioningInfo, _Mapping]]] = ...) -> None: ...

class ZWaveProvisioningInfo(_message.Message):
    __slots__ = ["product_type", "product_id", "inclusion_interval", "uuid", "name", "location", "inclusion_status", "granted_keys", "bootstrapping_mode", "network_status"]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_STATUS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_KEYS_FIELD_NUMBER: _ClassVar[int]
    BOOTSTRAPPING_MODE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_STATUS_FIELD_NUMBER: _ClassVar[int]
    product_type: ZWaveProvisioningInfoProductType
    product_id: ZWaveProvisioningInfoProductID
    inclusion_interval: int
    uuid: str
    name: str
    location: str
    inclusion_status: int
    granted_keys: int
    bootstrapping_mode: int
    network_status: ZWaveProvisioningInfoNetworkStatus
    def __init__(self, product_type: _Optional[_Union[ZWaveProvisioningInfoProductType, _Mapping]] = ..., product_id: _Optional[_Union[ZWaveProvisioningInfoProductID, _Mapping]] = ..., inclusion_interval: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., location: _Optional[str] = ..., inclusion_status: _Optional[int] = ..., granted_keys: _Optional[int] = ..., bootstrapping_mode: _Optional[int] = ..., network_status: _Optional[_Union[ZWaveProvisioningInfoNetworkStatus, _Mapping]] = ...) -> None: ...

class ZWaveProvisioningInfoProductType(_message.Message):
    __slots__ = ["generic_class", "specific_class", "icon_type"]
    GENERIC_CLASS_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_CLASS_FIELD_NUMBER: _ClassVar[int]
    ICON_TYPE_FIELD_NUMBER: _ClassVar[int]
    generic_class: int
    specific_class: int
    icon_type: int
    def __init__(self, generic_class: _Optional[int] = ..., specific_class: _Optional[int] = ..., icon_type: _Optional[int] = ...) -> None: ...

class ZWaveProvisioningInfoProductID(_message.Message):
    __slots__ = ["manufacturer_id", "product_type", "product_id", "application_version", "application_sub_version"]
    MANUFACTURER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SUB_VERSION_FIELD_NUMBER: _ClassVar[int]
    manufacturer_id: int
    product_type: int
    product_id: int
    application_version: int
    application_sub_version: int
    def __init__(self, manufacturer_id: _Optional[int] = ..., product_type: _Optional[int] = ..., product_id: _Optional[int] = ..., application_version: _Optional[int] = ..., application_sub_version: _Optional[int] = ...) -> None: ...

class ZWaveProvisioningInfoNetworkStatus(_message.Message):
    __slots__ = ["node_id", "status"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    status: int
    def __init__(self, node_id: _Optional[int] = ..., status: _Optional[int] = ...) -> None: ...

class ZWaveNotificationItemsRequest(_message.Message):
    __slots__ = ["node_id", "ep_id", "index"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    EP_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    ep_id: int
    index: int
    def __init__(self, node_id: _Optional[int] = ..., ep_id: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class ZWaveNotificationItemsResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, items: _Optional[_Iterable[int]] = ...) -> None: ...
