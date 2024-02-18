from aiovemmio import addon_pb2 as _addon_pb2
from aiovemmio import admin_pb2 as _admin_pb2
from aiovemmio import battery_pb2 as _battery_pb2
from aiovemmio import ble_pb2 as _ble_pb2
from aiovemmio import carbon_monoxide_pb2 as _carbon_monoxide_pb2
from aiovemmio import color_pb2 as _color_pb2
from aiovemmio import configuration_pb2 as _configuration_pb2
from aiovemmio import devices_pb2 as _devices_pb2
from aiovemmio import firmware_pb2 as _firmware_pb2
from aiovemmio import gate_pb2 as _gate_pb2
from aiovemmio import gateway_pb2 as _gateway_pb2
from aiovemmio import info_pb2 as _info_pb2
from aiovemmio import level_pb2 as _level_pb2
from aiovemmio import lock_pb2 as _lock_pb2
from aiovemmio import messaging_pb2 as _messaging_pb2
from aiovemmio import meter_pb2 as _meter_pb2
from aiovemmio import remote_pb2 as _remote_pb2
from aiovemmio import roller_shutter_pb2 as _roller_shutter_pb2
from aiovemmio import siren_pb2 as _siren_pb2
from aiovemmio import status_pb2 as _status_pb2
from aiovemmio import structure_pb2 as _structure_pb2
from aiovemmio import switch_pb2 as _switch_pb2
from aiovemmio import temperature_pb2 as _temperature_pb2
from aiovemmio import thermostat_pb2 as _thermostat_pb2
from aiovemmio import ultraviolet_pb2 as _ultraviolet_pb2
from aiovemmio import wifi_pb2 as _wifi_pb2
from aiovemmio import zigbee_pb2 as _zigbee_pb2
from aiovemmio import zwave_pb2 as _zwave_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REQUEST_TYPE_UNSPECIFIED: _ClassVar[CommandRequestType]
    REQUEST_TYPE_DATA: _ClassVar[CommandRequestType]
    REQUEST_TYPE_EOF: _ClassVar[CommandRequestType]

class CommandRequestOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REQUEST_OPTION_UNSPECIFIED: _ClassVar[CommandRequestOption]
    REQUEST_OPTION_NOACK: _ClassVar[CommandRequestOption]
    REQUEST_OPTION_NORESPONSE: _ClassVar[CommandRequestOption]

class CommandReplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REPLY_TYPE_UNSPECIFIED: _ClassVar[CommandReplyType]
    REPLY_TYPE_ACK: _ClassVar[CommandReplyType]
    REPLY_TYPE_ERROR: _ClassVar[CommandReplyType]
    REPLY_TYPE_EOF: _ClassVar[CommandReplyType]
    REPLY_TYPE_DATA: _ClassVar[CommandReplyType]
REQUEST_TYPE_UNSPECIFIED: CommandRequestType
REQUEST_TYPE_DATA: CommandRequestType
REQUEST_TYPE_EOF: CommandRequestType
REQUEST_OPTION_UNSPECIFIED: CommandRequestOption
REQUEST_OPTION_NOACK: CommandRequestOption
REQUEST_OPTION_NORESPONSE: CommandRequestOption
REPLY_TYPE_UNSPECIFIED: CommandReplyType
REPLY_TYPE_ACK: CommandReplyType
REPLY_TYPE_ERROR: CommandReplyType
REPLY_TYPE_EOF: CommandReplyType
REPLY_TYPE_DATA: CommandReplyType

class MetricsNotification(_message.Message):
    __slots__ = ["mac", "data"]
    MAC_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mac: str
    data: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, mac: _Optional[str] = ..., data: _Optional[_Iterable[bytes]] = ...) -> None: ...

class PresenceNotification(_message.Message):
    __slots__ = ["mac", "version", "git_commit", "build_time", "firmware_version"]
    MAC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIME_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    mac: str
    version: str
    git_commit: str
    build_time: str
    firmware_version: str
    def __init__(self, mac: _Optional[str] = ..., version: _Optional[str] = ..., git_commit: _Optional[str] = ..., build_time: _Optional[str] = ..., firmware_version: _Optional[str] = ...) -> None: ...

class CommandRequest(_message.Message):
    __slots__ = ["method", "type", "data", "payload", "options"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    method: str
    type: CommandRequestType
    data: CommandRequestData
    payload: bytes
    options: _containers.RepeatedScalarFieldContainer[CommandRequestOption]
    def __init__(self, method: _Optional[str] = ..., type: _Optional[_Union[CommandRequestType, str]] = ..., data: _Optional[_Union[CommandRequestData, _Mapping]] = ..., payload: _Optional[bytes] = ..., options: _Optional[_Iterable[_Union[CommandRequestOption, str]]] = ...) -> None: ...

class CommandReply(_message.Message):
    __slots__ = ["type", "error", "data", "payload"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    type: CommandReplyType
    error: CommandReplyError
    data: CommandReplyData
    payload: bytes
    def __init__(self, type: _Optional[_Union[CommandReplyType, str]] = ..., error: _Optional[_Union[CommandReplyError, _Mapping]] = ..., data: _Optional[_Union[CommandReplyData, _Mapping]] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CommandReplyError(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class MessagingRequest(_message.Message):
    __slots__ = ["email", "push"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PUSH_FIELD_NUMBER: _ClassVar[int]
    email: _messaging_pb2.EmailMessage
    push: _messaging_pb2.PushMessage
    def __init__(self, email: _Optional[_Union[_messaging_pb2.EmailMessage, _Mapping]] = ..., push: _Optional[_Union[_messaging_pb2.PushMessage, _Mapping]] = ...) -> None: ...

class CommandRequestData(_message.Message):
    __slots__ = ["AddonList", "AddonAddThermostat", "WalkNodes", "ReadLogs", "FollowLogs", "BatteryGet", "ColorSet", "ConfigurationList", "ConfigurationGet", "ConfigurationSet", "ThermostatModeSet", "ThermostatModeSupGet", "ThermostatSetpointSet", "ThermostatFanModeSet", "DevicesList", "FirmwareUpload", "FirmwareUpgrade", "FirmwareUpdate", "FirmwareLatestVersion", "Reboot", "Restart", "StartSupport", "StopSupport", "Info", "LevelGet", "LevelGetStep", "LevelSet", "LevelUp", "LevelDown", "LevelIncrease", "LevelDecrease", "LockSet", "MeterGet", "MeterReset", "RollerShutterOpen", "RollerShutterClose", "RollerShutterSet", "SirenGetTones", "SirenPlayTone", "SirenPlayDefaultTone", "SirenGetDefaultTone", "SirenSetDefaultTone", "SirenGetVolume", "SirenSetVolume", "SwitchOn", "SwitchOff", "TemperatureGet", "WiFiQuery", "WiFiScan", "WiFiConnect", "ZigbeeInclude", "ZigbeeExclude", "ZigbeeGetNodes", "ZWaveInclude", "ZWaveExclude", "ZWaveAbort", "ZWaveReadNodes", "ZWaveUpdate", "ZWaveUpdateNode", "ZWaveReset", "ZWaveListEntries", "ZWaveAddEntry", "ZWaveRemoveEntry", "ZWaveNotificationItems", "ZWaveTest", "ZWaveHeal", "ZWaveReplaceFailed", "ZWaveRemoveFailed", "ZWaveHealthCheck", "ZWaveReadNode", "CarbonMonoxideGet", "EnableAdvertising", "DisableAdvertising", "UltravioletGet", "KeyUp", "KeyDown", "GateOpen", "GateClose", "GateCycle", "StatusCheck", "GetStructure"]
    ADDONLIST_FIELD_NUMBER: _ClassVar[int]
    ADDONADDTHERMOSTAT_FIELD_NUMBER: _ClassVar[int]
    WALKNODES_FIELD_NUMBER: _ClassVar[int]
    READLOGS_FIELD_NUMBER: _ClassVar[int]
    FOLLOWLOGS_FIELD_NUMBER: _ClassVar[int]
    BATTERYGET_FIELD_NUMBER: _ClassVar[int]
    COLORSET_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONLIST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONGET_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONSET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATMODESET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATMODESUPGET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATSETPOINTSET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATFANMODESET_FIELD_NUMBER: _ClassVar[int]
    DEVICESLIST_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREUPLOAD_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREUPGRADE_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREUPDATE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARELATESTVERSION_FIELD_NUMBER: _ClassVar[int]
    REBOOT_FIELD_NUMBER: _ClassVar[int]
    RESTART_FIELD_NUMBER: _ClassVar[int]
    STARTSUPPORT_FIELD_NUMBER: _ClassVar[int]
    STOPSUPPORT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    LEVELGET_FIELD_NUMBER: _ClassVar[int]
    LEVELGETSTEP_FIELD_NUMBER: _ClassVar[int]
    LEVELSET_FIELD_NUMBER: _ClassVar[int]
    LEVELUP_FIELD_NUMBER: _ClassVar[int]
    LEVELDOWN_FIELD_NUMBER: _ClassVar[int]
    LEVELINCREASE_FIELD_NUMBER: _ClassVar[int]
    LEVELDECREASE_FIELD_NUMBER: _ClassVar[int]
    LOCKSET_FIELD_NUMBER: _ClassVar[int]
    METERGET_FIELD_NUMBER: _ClassVar[int]
    METERRESET_FIELD_NUMBER: _ClassVar[int]
    ROLLERSHUTTEROPEN_FIELD_NUMBER: _ClassVar[int]
    ROLLERSHUTTERCLOSE_FIELD_NUMBER: _ClassVar[int]
    ROLLERSHUTTERSET_FIELD_NUMBER: _ClassVar[int]
    SIRENGETTONES_FIELD_NUMBER: _ClassVar[int]
    SIRENPLAYTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENPLAYDEFAULTTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENGETDEFAULTTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENSETDEFAULTTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENGETVOLUME_FIELD_NUMBER: _ClassVar[int]
    SIRENSETVOLUME_FIELD_NUMBER: _ClassVar[int]
    SWITCHON_FIELD_NUMBER: _ClassVar[int]
    SWITCHOFF_FIELD_NUMBER: _ClassVar[int]
    TEMPERATUREGET_FIELD_NUMBER: _ClassVar[int]
    WIFIQUERY_FIELD_NUMBER: _ClassVar[int]
    WIFISCAN_FIELD_NUMBER: _ClassVar[int]
    WIFICONNECT_FIELD_NUMBER: _ClassVar[int]
    ZIGBEEINCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZIGBEEEXCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZIGBEEGETNODES_FIELD_NUMBER: _ClassVar[int]
    ZWAVEINCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZWAVEEXCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZWAVEABORT_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREADNODES_FIELD_NUMBER: _ClassVar[int]
    ZWAVEUPDATE_FIELD_NUMBER: _ClassVar[int]
    ZWAVEUPDATENODE_FIELD_NUMBER: _ClassVar[int]
    ZWAVERESET_FIELD_NUMBER: _ClassVar[int]
    ZWAVELISTENTRIES_FIELD_NUMBER: _ClassVar[int]
    ZWAVEADDENTRY_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREMOVEENTRY_FIELD_NUMBER: _ClassVar[int]
    ZWAVENOTIFICATIONITEMS_FIELD_NUMBER: _ClassVar[int]
    ZWAVETEST_FIELD_NUMBER: _ClassVar[int]
    ZWAVEHEAL_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREPLACEFAILED_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREMOVEFAILED_FIELD_NUMBER: _ClassVar[int]
    ZWAVEHEALTHCHECK_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREADNODE_FIELD_NUMBER: _ClassVar[int]
    CARBONMONOXIDEGET_FIELD_NUMBER: _ClassVar[int]
    ENABLEADVERTISING_FIELD_NUMBER: _ClassVar[int]
    DISABLEADVERTISING_FIELD_NUMBER: _ClassVar[int]
    ULTRAVIOLETGET_FIELD_NUMBER: _ClassVar[int]
    KEYUP_FIELD_NUMBER: _ClassVar[int]
    KEYDOWN_FIELD_NUMBER: _ClassVar[int]
    GATEOPEN_FIELD_NUMBER: _ClassVar[int]
    GATECLOSE_FIELD_NUMBER: _ClassVar[int]
    GATECYCLE_FIELD_NUMBER: _ClassVar[int]
    STATUSCHECK_FIELD_NUMBER: _ClassVar[int]
    GETSTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    AddonList: _addon_pb2.AddonListRequest
    AddonAddThermostat: _addon_pb2.AddonAddThermostatRequest
    WalkNodes: _admin_pb2.WalkNodesRequest
    ReadLogs: _admin_pb2.LogsRequest
    FollowLogs: _admin_pb2.LogsRequest
    BatteryGet: _battery_pb2.BatteryGetRequest
    ColorSet: _color_pb2.ColorSetRequest
    ConfigurationList: _configuration_pb2.ConfigurationListRequest
    ConfigurationGet: _configuration_pb2.ConfigurationGetRequest
    ConfigurationSet: _configuration_pb2.ConfigurationSetRequest
    ThermostatModeSet: _thermostat_pb2.ThermostatModeSetRequest
    ThermostatModeSupGet: _thermostat_pb2.ThermostatModeSupGetRequest
    ThermostatSetpointSet: _thermostat_pb2.ThermostatSetpointSetRequest
    ThermostatFanModeSet: _thermostat_pb2.ThermostatFanModeSetRequest
    DevicesList: _devices_pb2.DevicesListRequest
    FirmwareUpload: _firmware_pb2.FirmwareChunk
    FirmwareUpgrade: _firmware_pb2.FirmwareUpgradeRequest
    FirmwareUpdate: _firmware_pb2.FirmwareUpdateRequest
    FirmwareLatestVersion: _firmware_pb2.FirmwareLatestVersionRequest
    Reboot: _gateway_pb2.RebootRequest
    Restart: _gateway_pb2.RestartRequest
    StartSupport: _gateway_pb2.SupportRequest
    StopSupport: _gateway_pb2.SupportRequest
    Info: _info_pb2.InfoRequest
    LevelGet: _level_pb2.LevelRequest
    LevelGetStep: _level_pb2.LevelRequest
    LevelSet: _level_pb2.LevelSetRequest
    LevelUp: _level_pb2.LevelStepRequest
    LevelDown: _level_pb2.LevelStepRequest
    LevelIncrease: _level_pb2.LevelStepRequest
    LevelDecrease: _level_pb2.LevelStepRequest
    LockSet: _lock_pb2.LockSetRequest
    MeterGet: _meter_pb2.MeterGetRequest
    MeterReset: _meter_pb2.MeterResetRequest
    RollerShutterOpen: _roller_shutter_pb2.RollerShutterRequest
    RollerShutterClose: _roller_shutter_pb2.RollerShutterRequest
    RollerShutterSet: _roller_shutter_pb2.RollerShutterSetRequest
    SirenGetTones: _siren_pb2.SirenGetTonesRequest
    SirenPlayTone: _siren_pb2.SirenPlayToneRequest
    SirenPlayDefaultTone: _siren_pb2.SirenPlayDefaultToneRequest
    SirenGetDefaultTone: _siren_pb2.SirenGetDefaultToneRequest
    SirenSetDefaultTone: _siren_pb2.SirenSetDefaultToneRequest
    SirenGetVolume: _siren_pb2.SirenGetVolumeRequest
    SirenSetVolume: _siren_pb2.SirenSetVolumeRequest
    SwitchOn: _switch_pb2.SwitchRequest
    SwitchOff: _switch_pb2.SwitchRequest
    TemperatureGet: _temperature_pb2.TemperatureGetRequest
    WiFiQuery: _wifi_pb2.WiFiQueryRequest
    WiFiScan: _wifi_pb2.WiFiScanRequest
    WiFiConnect: _wifi_pb2.WiFiConnectRequest
    ZigbeeInclude: _zigbee_pb2.ZigbeeIncludeRequest
    ZigbeeExclude: _zigbee_pb2.ZigbeeExcludeRequest
    ZigbeeGetNodes: _zigbee_pb2.ZigbeeNodesRequest
    ZWaveInclude: _zwave_pb2.ZWaveIncludeRequest
    ZWaveExclude: _zwave_pb2.ZWaveExcludeRequest
    ZWaveAbort: _zwave_pb2.ZWaveAbortRequest
    ZWaveReadNodes: _zwave_pb2.ZWaveNodesRequest
    ZWaveUpdate: _zwave_pb2.ZWaveUpdateRequest
    ZWaveUpdateNode: _zwave_pb2.ZWaveUpdateNodeRequest
    ZWaveReset: _zwave_pb2.ZWaveResetRequest
    ZWaveListEntries: _zwave_pb2.ZWaveListEntriesRequest
    ZWaveAddEntry: _zwave_pb2.ZWaveAddEntryRequest
    ZWaveRemoveEntry: _zwave_pb2.ZWaveRemoveEntryRequest
    ZWaveNotificationItems: _zwave_pb2.ZWaveNotificationItemsRequest
    ZWaveTest: _zwave_pb2.ZWaveTestRequest
    ZWaveHeal: _zwave_pb2.ZWaveHealRequest
    ZWaveReplaceFailed: _zwave_pb2.ZWaveReplaceFailedRequest
    ZWaveRemoveFailed: _zwave_pb2.ZWaveRemoveFailedRequest
    ZWaveHealthCheck: _zwave_pb2.ZWaveHealthCheckRequest
    ZWaveReadNode: _zwave_pb2.ZWaveNodeRequest
    CarbonMonoxideGet: _carbon_monoxide_pb2.CarbonMonoxideGetRequest
    EnableAdvertising: _ble_pb2.AdvertisingRequest
    DisableAdvertising: _ble_pb2.AdvertisingRequest
    UltravioletGet: _ultraviolet_pb2.UltravioletGetRequest
    KeyUp: _remote_pb2.RemoteRequest
    KeyDown: _remote_pb2.RemoteRequest
    GateOpen: _gate_pb2.GateRequest
    GateClose: _gate_pb2.GateRequest
    GateCycle: _gate_pb2.GateRequest
    StatusCheck: _status_pb2.StatusCheckRequest
    GetStructure: _structure_pb2.StructureRequest
    def __init__(self, AddonList: _Optional[_Union[_addon_pb2.AddonListRequest, _Mapping]] = ..., AddonAddThermostat: _Optional[_Union[_addon_pb2.AddonAddThermostatRequest, _Mapping]] = ..., WalkNodes: _Optional[_Union[_admin_pb2.WalkNodesRequest, _Mapping]] = ..., ReadLogs: _Optional[_Union[_admin_pb2.LogsRequest, _Mapping]] = ..., FollowLogs: _Optional[_Union[_admin_pb2.LogsRequest, _Mapping]] = ..., BatteryGet: _Optional[_Union[_battery_pb2.BatteryGetRequest, _Mapping]] = ..., ColorSet: _Optional[_Union[_color_pb2.ColorSetRequest, _Mapping]] = ..., ConfigurationList: _Optional[_Union[_configuration_pb2.ConfigurationListRequest, _Mapping]] = ..., ConfigurationGet: _Optional[_Union[_configuration_pb2.ConfigurationGetRequest, _Mapping]] = ..., ConfigurationSet: _Optional[_Union[_configuration_pb2.ConfigurationSetRequest, _Mapping]] = ..., ThermostatModeSet: _Optional[_Union[_thermostat_pb2.ThermostatModeSetRequest, _Mapping]] = ..., ThermostatModeSupGet: _Optional[_Union[_thermostat_pb2.ThermostatModeSupGetRequest, _Mapping]] = ..., ThermostatSetpointSet: _Optional[_Union[_thermostat_pb2.ThermostatSetpointSetRequest, _Mapping]] = ..., ThermostatFanModeSet: _Optional[_Union[_thermostat_pb2.ThermostatFanModeSetRequest, _Mapping]] = ..., DevicesList: _Optional[_Union[_devices_pb2.DevicesListRequest, _Mapping]] = ..., FirmwareUpload: _Optional[_Union[_firmware_pb2.FirmwareChunk, _Mapping]] = ..., FirmwareUpgrade: _Optional[_Union[_firmware_pb2.FirmwareUpgradeRequest, _Mapping]] = ..., FirmwareUpdate: _Optional[_Union[_firmware_pb2.FirmwareUpdateRequest, _Mapping]] = ..., FirmwareLatestVersion: _Optional[_Union[_firmware_pb2.FirmwareLatestVersionRequest, _Mapping]] = ..., Reboot: _Optional[_Union[_gateway_pb2.RebootRequest, _Mapping]] = ..., Restart: _Optional[_Union[_gateway_pb2.RestartRequest, _Mapping]] = ..., StartSupport: _Optional[_Union[_gateway_pb2.SupportRequest, _Mapping]] = ..., StopSupport: _Optional[_Union[_gateway_pb2.SupportRequest, _Mapping]] = ..., Info: _Optional[_Union[_info_pb2.InfoRequest, _Mapping]] = ..., LevelGet: _Optional[_Union[_level_pb2.LevelRequest, _Mapping]] = ..., LevelGetStep: _Optional[_Union[_level_pb2.LevelRequest, _Mapping]] = ..., LevelSet: _Optional[_Union[_level_pb2.LevelSetRequest, _Mapping]] = ..., LevelUp: _Optional[_Union[_level_pb2.LevelStepRequest, _Mapping]] = ..., LevelDown: _Optional[_Union[_level_pb2.LevelStepRequest, _Mapping]] = ..., LevelIncrease: _Optional[_Union[_level_pb2.LevelStepRequest, _Mapping]] = ..., LevelDecrease: _Optional[_Union[_level_pb2.LevelStepRequest, _Mapping]] = ..., LockSet: _Optional[_Union[_lock_pb2.LockSetRequest, _Mapping]] = ..., MeterGet: _Optional[_Union[_meter_pb2.MeterGetRequest, _Mapping]] = ..., MeterReset: _Optional[_Union[_meter_pb2.MeterResetRequest, _Mapping]] = ..., RollerShutterOpen: _Optional[_Union[_roller_shutter_pb2.RollerShutterRequest, _Mapping]] = ..., RollerShutterClose: _Optional[_Union[_roller_shutter_pb2.RollerShutterRequest, _Mapping]] = ..., RollerShutterSet: _Optional[_Union[_roller_shutter_pb2.RollerShutterSetRequest, _Mapping]] = ..., SirenGetTones: _Optional[_Union[_siren_pb2.SirenGetTonesRequest, _Mapping]] = ..., SirenPlayTone: _Optional[_Union[_siren_pb2.SirenPlayToneRequest, _Mapping]] = ..., SirenPlayDefaultTone: _Optional[_Union[_siren_pb2.SirenPlayDefaultToneRequest, _Mapping]] = ..., SirenGetDefaultTone: _Optional[_Union[_siren_pb2.SirenGetDefaultToneRequest, _Mapping]] = ..., SirenSetDefaultTone: _Optional[_Union[_siren_pb2.SirenSetDefaultToneRequest, _Mapping]] = ..., SirenGetVolume: _Optional[_Union[_siren_pb2.SirenGetVolumeRequest, _Mapping]] = ..., SirenSetVolume: _Optional[_Union[_siren_pb2.SirenSetVolumeRequest, _Mapping]] = ..., SwitchOn: _Optional[_Union[_switch_pb2.SwitchRequest, _Mapping]] = ..., SwitchOff: _Optional[_Union[_switch_pb2.SwitchRequest, _Mapping]] = ..., TemperatureGet: _Optional[_Union[_temperature_pb2.TemperatureGetRequest, _Mapping]] = ..., WiFiQuery: _Optional[_Union[_wifi_pb2.WiFiQueryRequest, _Mapping]] = ..., WiFiScan: _Optional[_Union[_wifi_pb2.WiFiScanRequest, _Mapping]] = ..., WiFiConnect: _Optional[_Union[_wifi_pb2.WiFiConnectRequest, _Mapping]] = ..., ZigbeeInclude: _Optional[_Union[_zigbee_pb2.ZigbeeIncludeRequest, _Mapping]] = ..., ZigbeeExclude: _Optional[_Union[_zigbee_pb2.ZigbeeExcludeRequest, _Mapping]] = ..., ZigbeeGetNodes: _Optional[_Union[_zigbee_pb2.ZigbeeNodesRequest, _Mapping]] = ..., ZWaveInclude: _Optional[_Union[_zwave_pb2.ZWaveIncludeRequest, _Mapping]] = ..., ZWaveExclude: _Optional[_Union[_zwave_pb2.ZWaveExcludeRequest, _Mapping]] = ..., ZWaveAbort: _Optional[_Union[_zwave_pb2.ZWaveAbortRequest, _Mapping]] = ..., ZWaveReadNodes: _Optional[_Union[_zwave_pb2.ZWaveNodesRequest, _Mapping]] = ..., ZWaveUpdate: _Optional[_Union[_zwave_pb2.ZWaveUpdateRequest, _Mapping]] = ..., ZWaveUpdateNode: _Optional[_Union[_zwave_pb2.ZWaveUpdateNodeRequest, _Mapping]] = ..., ZWaveReset: _Optional[_Union[_zwave_pb2.ZWaveResetRequest, _Mapping]] = ..., ZWaveListEntries: _Optional[_Union[_zwave_pb2.ZWaveListEntriesRequest, _Mapping]] = ..., ZWaveAddEntry: _Optional[_Union[_zwave_pb2.ZWaveAddEntryRequest, _Mapping]] = ..., ZWaveRemoveEntry: _Optional[_Union[_zwave_pb2.ZWaveRemoveEntryRequest, _Mapping]] = ..., ZWaveNotificationItems: _Optional[_Union[_zwave_pb2.ZWaveNotificationItemsRequest, _Mapping]] = ..., ZWaveTest: _Optional[_Union[_zwave_pb2.ZWaveTestRequest, _Mapping]] = ..., ZWaveHeal: _Optional[_Union[_zwave_pb2.ZWaveHealRequest, _Mapping]] = ..., ZWaveReplaceFailed: _Optional[_Union[_zwave_pb2.ZWaveReplaceFailedRequest, _Mapping]] = ..., ZWaveRemoveFailed: _Optional[_Union[_zwave_pb2.ZWaveRemoveFailedRequest, _Mapping]] = ..., ZWaveHealthCheck: _Optional[_Union[_zwave_pb2.ZWaveHealthCheckRequest, _Mapping]] = ..., ZWaveReadNode: _Optional[_Union[_zwave_pb2.ZWaveNodeRequest, _Mapping]] = ..., CarbonMonoxideGet: _Optional[_Union[_carbon_monoxide_pb2.CarbonMonoxideGetRequest, _Mapping]] = ..., EnableAdvertising: _Optional[_Union[_ble_pb2.AdvertisingRequest, _Mapping]] = ..., DisableAdvertising: _Optional[_Union[_ble_pb2.AdvertisingRequest, _Mapping]] = ..., UltravioletGet: _Optional[_Union[_ultraviolet_pb2.UltravioletGetRequest, _Mapping]] = ..., KeyUp: _Optional[_Union[_remote_pb2.RemoteRequest, _Mapping]] = ..., KeyDown: _Optional[_Union[_remote_pb2.RemoteRequest, _Mapping]] = ..., GateOpen: _Optional[_Union[_gate_pb2.GateRequest, _Mapping]] = ..., GateClose: _Optional[_Union[_gate_pb2.GateRequest, _Mapping]] = ..., GateCycle: _Optional[_Union[_gate_pb2.GateRequest, _Mapping]] = ..., StatusCheck: _Optional[_Union[_status_pb2.StatusCheckRequest, _Mapping]] = ..., GetStructure: _Optional[_Union[_structure_pb2.StructureRequest, _Mapping]] = ...) -> None: ...

class CommandReplyData(_message.Message):
    __slots__ = ["AddonList", "AddonAddThermostat", "WalkNodes", "ReadLogs", "FollowLogs", "BatteryGet", "ColorSet", "ConfigurationList", "ConfigurationGet", "ConfigurationSet", "ThermostatModeSet", "ThermostatModeSupGet", "ThermostatSetpointSet", "ThermostatFanModeSet", "DevicesList", "FirmwareUpload", "FirmwareUpgrade", "FirmwareUpdate", "FirmwareLatestVersion", "Reboot", "Restart", "StartSupport", "StopSupport", "Info", "LevelGet", "LevelGetStep", "LevelSet", "LevelUp", "LevelDown", "LevelIncrease", "LevelDecrease", "LockSet", "MeterGet", "MeterReset", "RollerShutterOpen", "RollerShutterClose", "RollerShutterSet", "SirenGetTones", "SirenPlayTone", "SirenPlayDefaultTone", "SirenGetDefaultTone", "SirenSetDefaultTone", "SirenGetVolume", "SirenSetVolume", "SwitchOn", "SwitchOff", "TemperatureGet", "WiFiQuery", "WiFiScan", "WiFiConnect", "ZigbeeInclude", "ZigbeeExclude", "ZigbeeGetNodes", "ZWaveInclude", "ZWaveExclude", "ZWaveAbort", "ZWaveReadNodes", "ZWaveUpdate", "ZWaveUpdateNode", "ZWaveReset", "ZWaveListEntries", "ZWaveAddEntry", "ZWaveRemoveEntry", "ZWaveNotificationItems", "ZWaveTest", "ZWaveHeal", "ZWaveReplaceFailed", "ZWaveRemoveFailed", "ZWaveHealthCheck", "ZWaveReadNode", "CarbonMonoxideGet", "EnableAdvertising", "DisableAdvertising", "UltravioletGet", "KeyUp", "KeyDown", "GateOpen", "GateClose", "GateCycle", "StatusCheck", "GetStructure"]
    ADDONLIST_FIELD_NUMBER: _ClassVar[int]
    ADDONADDTHERMOSTAT_FIELD_NUMBER: _ClassVar[int]
    WALKNODES_FIELD_NUMBER: _ClassVar[int]
    READLOGS_FIELD_NUMBER: _ClassVar[int]
    FOLLOWLOGS_FIELD_NUMBER: _ClassVar[int]
    BATTERYGET_FIELD_NUMBER: _ClassVar[int]
    COLORSET_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONLIST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONGET_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONSET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATMODESET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATMODESUPGET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATSETPOINTSET_FIELD_NUMBER: _ClassVar[int]
    THERMOSTATFANMODESET_FIELD_NUMBER: _ClassVar[int]
    DEVICESLIST_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREUPLOAD_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREUPGRADE_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREUPDATE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARELATESTVERSION_FIELD_NUMBER: _ClassVar[int]
    REBOOT_FIELD_NUMBER: _ClassVar[int]
    RESTART_FIELD_NUMBER: _ClassVar[int]
    STARTSUPPORT_FIELD_NUMBER: _ClassVar[int]
    STOPSUPPORT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    LEVELGET_FIELD_NUMBER: _ClassVar[int]
    LEVELGETSTEP_FIELD_NUMBER: _ClassVar[int]
    LEVELSET_FIELD_NUMBER: _ClassVar[int]
    LEVELUP_FIELD_NUMBER: _ClassVar[int]
    LEVELDOWN_FIELD_NUMBER: _ClassVar[int]
    LEVELINCREASE_FIELD_NUMBER: _ClassVar[int]
    LEVELDECREASE_FIELD_NUMBER: _ClassVar[int]
    LOCKSET_FIELD_NUMBER: _ClassVar[int]
    METERGET_FIELD_NUMBER: _ClassVar[int]
    METERRESET_FIELD_NUMBER: _ClassVar[int]
    ROLLERSHUTTEROPEN_FIELD_NUMBER: _ClassVar[int]
    ROLLERSHUTTERCLOSE_FIELD_NUMBER: _ClassVar[int]
    ROLLERSHUTTERSET_FIELD_NUMBER: _ClassVar[int]
    SIRENGETTONES_FIELD_NUMBER: _ClassVar[int]
    SIRENPLAYTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENPLAYDEFAULTTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENGETDEFAULTTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENSETDEFAULTTONE_FIELD_NUMBER: _ClassVar[int]
    SIRENGETVOLUME_FIELD_NUMBER: _ClassVar[int]
    SIRENSETVOLUME_FIELD_NUMBER: _ClassVar[int]
    SWITCHON_FIELD_NUMBER: _ClassVar[int]
    SWITCHOFF_FIELD_NUMBER: _ClassVar[int]
    TEMPERATUREGET_FIELD_NUMBER: _ClassVar[int]
    WIFIQUERY_FIELD_NUMBER: _ClassVar[int]
    WIFISCAN_FIELD_NUMBER: _ClassVar[int]
    WIFICONNECT_FIELD_NUMBER: _ClassVar[int]
    ZIGBEEINCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZIGBEEEXCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZIGBEEGETNODES_FIELD_NUMBER: _ClassVar[int]
    ZWAVEINCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZWAVEEXCLUDE_FIELD_NUMBER: _ClassVar[int]
    ZWAVEABORT_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREADNODES_FIELD_NUMBER: _ClassVar[int]
    ZWAVEUPDATE_FIELD_NUMBER: _ClassVar[int]
    ZWAVEUPDATENODE_FIELD_NUMBER: _ClassVar[int]
    ZWAVERESET_FIELD_NUMBER: _ClassVar[int]
    ZWAVELISTENTRIES_FIELD_NUMBER: _ClassVar[int]
    ZWAVEADDENTRY_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREMOVEENTRY_FIELD_NUMBER: _ClassVar[int]
    ZWAVENOTIFICATIONITEMS_FIELD_NUMBER: _ClassVar[int]
    ZWAVETEST_FIELD_NUMBER: _ClassVar[int]
    ZWAVEHEAL_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREPLACEFAILED_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREMOVEFAILED_FIELD_NUMBER: _ClassVar[int]
    ZWAVEHEALTHCHECK_FIELD_NUMBER: _ClassVar[int]
    ZWAVEREADNODE_FIELD_NUMBER: _ClassVar[int]
    CARBONMONOXIDEGET_FIELD_NUMBER: _ClassVar[int]
    ENABLEADVERTISING_FIELD_NUMBER: _ClassVar[int]
    DISABLEADVERTISING_FIELD_NUMBER: _ClassVar[int]
    ULTRAVIOLETGET_FIELD_NUMBER: _ClassVar[int]
    KEYUP_FIELD_NUMBER: _ClassVar[int]
    KEYDOWN_FIELD_NUMBER: _ClassVar[int]
    GATEOPEN_FIELD_NUMBER: _ClassVar[int]
    GATECLOSE_FIELD_NUMBER: _ClassVar[int]
    GATECYCLE_FIELD_NUMBER: _ClassVar[int]
    STATUSCHECK_FIELD_NUMBER: _ClassVar[int]
    GETSTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    AddonList: _addon_pb2.AddonListResponse
    AddonAddThermostat: _addon_pb2.AddonAddResponse
    WalkNodes: _admin_pb2.WalkNodesResponse
    ReadLogs: _admin_pb2.LogsChunk
    FollowLogs: _admin_pb2.LogsChunk
    BatteryGet: _battery_pb2.BatteryGetResponse
    ColorSet: _color_pb2.ColorResponse
    ConfigurationList: _configuration_pb2.ConfigurationListResponse
    ConfigurationGet: _configuration_pb2.ConfigurationGetResponse
    ConfigurationSet: _configuration_pb2.ConfigurationSetResponse
    ThermostatModeSet: _thermostat_pb2.ThermostatResponse
    ThermostatModeSupGet: _thermostat_pb2.ThermostatModeSupGetResponse
    ThermostatSetpointSet: _thermostat_pb2.ThermostatResponse
    ThermostatFanModeSet: _thermostat_pb2.ThermostatResponse
    DevicesList: _devices_pb2.DevicesListResponse
    FirmwareUpload: _firmware_pb2.FirmwareChunkAck
    FirmwareUpgrade: _firmware_pb2.FirmwareUpgradeAck
    FirmwareUpdate: _firmware_pb2.FirmwareUpdateResponse
    FirmwareLatestVersion: _firmware_pb2.FirmwareLatestVersionResponse
    Reboot: _gateway_pb2.RebootResponse
    Restart: _gateway_pb2.RestartResponse
    StartSupport: _gateway_pb2.SupportResponse
    StopSupport: _gateway_pb2.SupportResponse
    Info: _info_pb2.InfoResponse
    LevelGet: _level_pb2.LevelGetResponse
    LevelGetStep: _level_pb2.LevelGetResponse
    LevelSet: _level_pb2.LevelResponse
    LevelUp: _level_pb2.LevelResponse
    LevelDown: _level_pb2.LevelResponse
    LevelIncrease: _level_pb2.LevelResponse
    LevelDecrease: _level_pb2.LevelResponse
    LockSet: _lock_pb2.LockResponse
    MeterGet: _meter_pb2.MeterGetResponse
    MeterReset: _meter_pb2.MeterResetResponse
    RollerShutterOpen: _roller_shutter_pb2.RollerShutterResponse
    RollerShutterClose: _roller_shutter_pb2.RollerShutterResponse
    RollerShutterSet: _roller_shutter_pb2.RollerShutterResponse
    SirenGetTones: _siren_pb2.SirenGetTonesResponse
    SirenPlayTone: _siren_pb2.SirenPlayToneResponse
    SirenPlayDefaultTone: _siren_pb2.SirenPlayDefaultToneResponse
    SirenGetDefaultTone: _siren_pb2.SirenGetDefaultToneResponse
    SirenSetDefaultTone: _siren_pb2.SirenSetDefaultToneResponse
    SirenGetVolume: _siren_pb2.SirenGetVolumeResponse
    SirenSetVolume: _siren_pb2.SirenSetVolumeResponse
    SwitchOn: _switch_pb2.SwitchResponse
    SwitchOff: _switch_pb2.SwitchResponse
    TemperatureGet: _temperature_pb2.TemperatureGetResponse
    WiFiQuery: _wifi_pb2.WiFiQueryResponse
    WiFiScan: _wifi_pb2.WiFiScanResponse
    WiFiConnect: _wifi_pb2.WiFiConnectResponse
    ZigbeeInclude: _zigbee_pb2.ZigbeeIncludeResponse
    ZigbeeExclude: _zigbee_pb2.ZigbeeExcludeResponse
    ZigbeeGetNodes: _zigbee_pb2.ZigbeeNodesResponse
    ZWaveInclude: _zwave_pb2.ZWaveIncludeStatus
    ZWaveExclude: _zwave_pb2.ZWaveExcludeStatus
    ZWaveAbort: _zwave_pb2.ZWaveAbortResponse
    ZWaveReadNodes: _zwave_pb2.ZWaveNodesResponse
    ZWaveUpdate: _zwave_pb2.ZWaveUpdateStatus
    ZWaveUpdateNode: _zwave_pb2.ZWaveUpdateNodeResponse
    ZWaveReset: _zwave_pb2.ZWaveResetResponse
    ZWaveListEntries: _zwave_pb2.ZWaveListEntriesResponse
    ZWaveAddEntry: _zwave_pb2.ZWaveAddEntryResponse
    ZWaveRemoveEntry: _zwave_pb2.ZWaveRemoveEntryResponse
    ZWaveNotificationItems: _zwave_pb2.ZWaveNotificationItemsResponse
    ZWaveTest: _zwave_pb2.ZWaveTestResponse
    ZWaveHeal: _zwave_pb2.ZWaveHealResponse
    ZWaveReplaceFailed: _zwave_pb2.ZWaveReplaceFailedResponse
    ZWaveRemoveFailed: _zwave_pb2.ZWaveRemoveFailedResponse
    ZWaveHealthCheck: _zwave_pb2.ZWaveHealthCheckStatus
    ZWaveReadNode: _zwave_pb2.ZWaveNodeResponse
    CarbonMonoxideGet: _carbon_monoxide_pb2.CarbonMonoxideGetResponse
    EnableAdvertising: _ble_pb2.AdvertisingResponse
    DisableAdvertising: _ble_pb2.AdvertisingResponse
    UltravioletGet: _ultraviolet_pb2.UltravioletGetResponse
    KeyUp: _remote_pb2.RemoteResponse
    KeyDown: _remote_pb2.RemoteResponse
    GateOpen: _gate_pb2.GateResponse
    GateClose: _gate_pb2.GateResponse
    GateCycle: _gate_pb2.GateResponse
    StatusCheck: _status_pb2.StatusCheckResponse
    GetStructure: _structure_pb2.StructureResponse
    def __init__(self, AddonList: _Optional[_Union[_addon_pb2.AddonListResponse, _Mapping]] = ..., AddonAddThermostat: _Optional[_Union[_addon_pb2.AddonAddResponse, _Mapping]] = ..., WalkNodes: _Optional[_Union[_admin_pb2.WalkNodesResponse, _Mapping]] = ..., ReadLogs: _Optional[_Union[_admin_pb2.LogsChunk, _Mapping]] = ..., FollowLogs: _Optional[_Union[_admin_pb2.LogsChunk, _Mapping]] = ..., BatteryGet: _Optional[_Union[_battery_pb2.BatteryGetResponse, _Mapping]] = ..., ColorSet: _Optional[_Union[_color_pb2.ColorResponse, _Mapping]] = ..., ConfigurationList: _Optional[_Union[_configuration_pb2.ConfigurationListResponse, _Mapping]] = ..., ConfigurationGet: _Optional[_Union[_configuration_pb2.ConfigurationGetResponse, _Mapping]] = ..., ConfigurationSet: _Optional[_Union[_configuration_pb2.ConfigurationSetResponse, _Mapping]] = ..., ThermostatModeSet: _Optional[_Union[_thermostat_pb2.ThermostatResponse, _Mapping]] = ..., ThermostatModeSupGet: _Optional[_Union[_thermostat_pb2.ThermostatModeSupGetResponse, _Mapping]] = ..., ThermostatSetpointSet: _Optional[_Union[_thermostat_pb2.ThermostatResponse, _Mapping]] = ..., ThermostatFanModeSet: _Optional[_Union[_thermostat_pb2.ThermostatResponse, _Mapping]] = ..., DevicesList: _Optional[_Union[_devices_pb2.DevicesListResponse, _Mapping]] = ..., FirmwareUpload: _Optional[_Union[_firmware_pb2.FirmwareChunkAck, _Mapping]] = ..., FirmwareUpgrade: _Optional[_Union[_firmware_pb2.FirmwareUpgradeAck, _Mapping]] = ..., FirmwareUpdate: _Optional[_Union[_firmware_pb2.FirmwareUpdateResponse, _Mapping]] = ..., FirmwareLatestVersion: _Optional[_Union[_firmware_pb2.FirmwareLatestVersionResponse, _Mapping]] = ..., Reboot: _Optional[_Union[_gateway_pb2.RebootResponse, _Mapping]] = ..., Restart: _Optional[_Union[_gateway_pb2.RestartResponse, _Mapping]] = ..., StartSupport: _Optional[_Union[_gateway_pb2.SupportResponse, _Mapping]] = ..., StopSupport: _Optional[_Union[_gateway_pb2.SupportResponse, _Mapping]] = ..., Info: _Optional[_Union[_info_pb2.InfoResponse, _Mapping]] = ..., LevelGet: _Optional[_Union[_level_pb2.LevelGetResponse, _Mapping]] = ..., LevelGetStep: _Optional[_Union[_level_pb2.LevelGetResponse, _Mapping]] = ..., LevelSet: _Optional[_Union[_level_pb2.LevelResponse, _Mapping]] = ..., LevelUp: _Optional[_Union[_level_pb2.LevelResponse, _Mapping]] = ..., LevelDown: _Optional[_Union[_level_pb2.LevelResponse, _Mapping]] = ..., LevelIncrease: _Optional[_Union[_level_pb2.LevelResponse, _Mapping]] = ..., LevelDecrease: _Optional[_Union[_level_pb2.LevelResponse, _Mapping]] = ..., LockSet: _Optional[_Union[_lock_pb2.LockResponse, _Mapping]] = ..., MeterGet: _Optional[_Union[_meter_pb2.MeterGetResponse, _Mapping]] = ..., MeterReset: _Optional[_Union[_meter_pb2.MeterResetResponse, _Mapping]] = ..., RollerShutterOpen: _Optional[_Union[_roller_shutter_pb2.RollerShutterResponse, _Mapping]] = ..., RollerShutterClose: _Optional[_Union[_roller_shutter_pb2.RollerShutterResponse, _Mapping]] = ..., RollerShutterSet: _Optional[_Union[_roller_shutter_pb2.RollerShutterResponse, _Mapping]] = ..., SirenGetTones: _Optional[_Union[_siren_pb2.SirenGetTonesResponse, _Mapping]] = ..., SirenPlayTone: _Optional[_Union[_siren_pb2.SirenPlayToneResponse, _Mapping]] = ..., SirenPlayDefaultTone: _Optional[_Union[_siren_pb2.SirenPlayDefaultToneResponse, _Mapping]] = ..., SirenGetDefaultTone: _Optional[_Union[_siren_pb2.SirenGetDefaultToneResponse, _Mapping]] = ..., SirenSetDefaultTone: _Optional[_Union[_siren_pb2.SirenSetDefaultToneResponse, _Mapping]] = ..., SirenGetVolume: _Optional[_Union[_siren_pb2.SirenGetVolumeResponse, _Mapping]] = ..., SirenSetVolume: _Optional[_Union[_siren_pb2.SirenSetVolumeResponse, _Mapping]] = ..., SwitchOn: _Optional[_Union[_switch_pb2.SwitchResponse, _Mapping]] = ..., SwitchOff: _Optional[_Union[_switch_pb2.SwitchResponse, _Mapping]] = ..., TemperatureGet: _Optional[_Union[_temperature_pb2.TemperatureGetResponse, _Mapping]] = ..., WiFiQuery: _Optional[_Union[_wifi_pb2.WiFiQueryResponse, _Mapping]] = ..., WiFiScan: _Optional[_Union[_wifi_pb2.WiFiScanResponse, _Mapping]] = ..., WiFiConnect: _Optional[_Union[_wifi_pb2.WiFiConnectResponse, _Mapping]] = ..., ZigbeeInclude: _Optional[_Union[_zigbee_pb2.ZigbeeIncludeResponse, _Mapping]] = ..., ZigbeeExclude: _Optional[_Union[_zigbee_pb2.ZigbeeExcludeResponse, _Mapping]] = ..., ZigbeeGetNodes: _Optional[_Union[_zigbee_pb2.ZigbeeNodesResponse, _Mapping]] = ..., ZWaveInclude: _Optional[_Union[_zwave_pb2.ZWaveIncludeStatus, _Mapping]] = ..., ZWaveExclude: _Optional[_Union[_zwave_pb2.ZWaveExcludeStatus, _Mapping]] = ..., ZWaveAbort: _Optional[_Union[_zwave_pb2.ZWaveAbortResponse, _Mapping]] = ..., ZWaveReadNodes: _Optional[_Union[_zwave_pb2.ZWaveNodesResponse, _Mapping]] = ..., ZWaveUpdate: _Optional[_Union[_zwave_pb2.ZWaveUpdateStatus, _Mapping]] = ..., ZWaveUpdateNode: _Optional[_Union[_zwave_pb2.ZWaveUpdateNodeResponse, _Mapping]] = ..., ZWaveReset: _Optional[_Union[_zwave_pb2.ZWaveResetResponse, _Mapping]] = ..., ZWaveListEntries: _Optional[_Union[_zwave_pb2.ZWaveListEntriesResponse, _Mapping]] = ..., ZWaveAddEntry: _Optional[_Union[_zwave_pb2.ZWaveAddEntryResponse, _Mapping]] = ..., ZWaveRemoveEntry: _Optional[_Union[_zwave_pb2.ZWaveRemoveEntryResponse, _Mapping]] = ..., ZWaveNotificationItems: _Optional[_Union[_zwave_pb2.ZWaveNotificationItemsResponse, _Mapping]] = ..., ZWaveTest: _Optional[_Union[_zwave_pb2.ZWaveTestResponse, _Mapping]] = ..., ZWaveHeal: _Optional[_Union[_zwave_pb2.ZWaveHealResponse, _Mapping]] = ..., ZWaveReplaceFailed: _Optional[_Union[_zwave_pb2.ZWaveReplaceFailedResponse, _Mapping]] = ..., ZWaveRemoveFailed: _Optional[_Union[_zwave_pb2.ZWaveRemoveFailedResponse, _Mapping]] = ..., ZWaveHealthCheck: _Optional[_Union[_zwave_pb2.ZWaveHealthCheckStatus, _Mapping]] = ..., ZWaveReadNode: _Optional[_Union[_zwave_pb2.ZWaveNodeResponse, _Mapping]] = ..., CarbonMonoxideGet: _Optional[_Union[_carbon_monoxide_pb2.CarbonMonoxideGetResponse, _Mapping]] = ..., EnableAdvertising: _Optional[_Union[_ble_pb2.AdvertisingResponse, _Mapping]] = ..., DisableAdvertising: _Optional[_Union[_ble_pb2.AdvertisingResponse, _Mapping]] = ..., UltravioletGet: _Optional[_Union[_ultraviolet_pb2.UltravioletGetResponse, _Mapping]] = ..., KeyUp: _Optional[_Union[_remote_pb2.RemoteResponse, _Mapping]] = ..., KeyDown: _Optional[_Union[_remote_pb2.RemoteResponse, _Mapping]] = ..., GateOpen: _Optional[_Union[_gate_pb2.GateResponse, _Mapping]] = ..., GateClose: _Optional[_Union[_gate_pb2.GateResponse, _Mapping]] = ..., GateCycle: _Optional[_Union[_gate_pb2.GateResponse, _Mapping]] = ..., StatusCheck: _Optional[_Union[_status_pb2.StatusCheckResponse, _Mapping]] = ..., GetStructure: _Optional[_Union[_structure_pb2.StructureResponse, _Mapping]] = ...) -> None: ...
