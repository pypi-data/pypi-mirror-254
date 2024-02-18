from aiovemmio import accelerometer_pb2 as _accelerometer_pb2
from aiovemmio import color_pb2 as _color_pb2
from aiovemmio import metadata_pb2 as _metadata_pb2
from aiovemmio import power_source_pb2 as _power_source_pb2
from aiovemmio import thermostat_pb2 as _thermostat_pb2
from aiovemmio import units_pb2 as _units_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DevicesListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DevicesListResponse(_message.Message):
    __slots__ = ["devices"]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ["name", "metadata", "capabilities", "i18n", "group"]
    class Group(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        OTHER: _ClassVar[Device.Group]
        CLIMATE: _ClassVar[Device.Group]
        SECURITY: _ClassVar[Device.Group]
        POWER: _ClassVar[Device.Group]
        ROLLER_SHUTTERS: _ClassVar[Device.Group]
        CAMERAS: _ClassVar[Device.Group]
        DOORBELLS: _ClassVar[Device.Group]
        GATEWAYS: _ClassVar[Device.Group]
        LIGHTS: _ClassVar[Device.Group]
        GATES: _ClassVar[Device.Group]
        SOUND: _ClassVar[Device.Group]
    OTHER: Device.Group
    CLIMATE: Device.Group
    SECURITY: Device.Group
    POWER: Device.Group
    ROLLER_SHUTTERS: Device.Group
    CAMERAS: Device.Group
    DOORBELLS: Device.Group
    GATEWAYS: Device.Group
    LIGHTS: Device.Group
    GATES: Device.Group
    SOUND: Device.Group
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    I18N_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: _metadata_pb2.DeviceMetadata
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    i18n: str
    group: Device.Group
    def __init__(self, name: _Optional[str] = ..., metadata: _Optional[_Union[_metadata_pb2.DeviceMetadata, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]] = ..., i18n: _Optional[str] = ..., group: _Optional[_Union[Device.Group, str]] = ...) -> None: ...

class Capability(_message.Message):
    __slots__ = ["switch", "power_meter", "gas_meter", "water_meter", "open_close", "smoke_detector", "motion_detector", "flood_detector", "carbon_monoxide_detector", "thermostat", "temperature", "humidity", "illumination", "direction", "tamper", "emergency", "door", "tap_tap", "color", "level", "battery", "lock", "remote", "power_source", "roller_shutter", "configuration", "doorbell", "siren", "accelerometer", "seismic", "carbon_dioxide_detector", "voltage", "ultraviolet"]
    SWITCH_FIELD_NUMBER: _ClassVar[int]
    POWER_METER_FIELD_NUMBER: _ClassVar[int]
    GAS_METER_FIELD_NUMBER: _ClassVar[int]
    WATER_METER_FIELD_NUMBER: _ClassVar[int]
    OPEN_CLOSE_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTOR_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTOR_FIELD_NUMBER: _ClassVar[int]
    FLOOD_DETECTOR_FIELD_NUMBER: _ClassVar[int]
    CARBON_MONOXIDE_DETECTOR_FIELD_NUMBER: _ClassVar[int]
    THERMOSTAT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TAMPER_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_FIELD_NUMBER: _ClassVar[int]
    DOOR_FIELD_NUMBER: _ClassVar[int]
    TAP_TAP_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    POWER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DOORBELL_FIELD_NUMBER: _ClassVar[int]
    SIREN_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_FIELD_NUMBER: _ClassVar[int]
    CARBON_DIOXIDE_DETECTOR_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    ULTRAVIOLET_FIELD_NUMBER: _ClassVar[int]
    switch: SwitchCapability
    power_meter: MeterCapability
    gas_meter: MeterCapability
    water_meter: MeterCapability
    open_close: OpenCloseCapability
    smoke_detector: SmokeDetectorCapability
    motion_detector: MotionDetectorCapability
    flood_detector: FloodDetectorCapability
    carbon_monoxide_detector: CarbonMonoxideDetectorCapability
    thermostat: ThermostatCapability
    temperature: TemperatureCapability
    humidity: HumidityCapability
    illumination: IlluminationCapability
    direction: DirectionCapability
    tamper: TamperCapability
    emergency: EmergencyCapability
    door: DoorCapability
    tap_tap: TapTapCapability
    color: ColorCapability
    level: LevelCapability
    battery: BatteryCapability
    lock: LockCapability
    remote: RemoteCapability
    power_source: PowerSourceCapability
    roller_shutter: RollerShutterCapability
    configuration: ConfigurationCapability
    doorbell: DoorbellCapability
    siren: SirenCapability
    accelerometer: AccelerometerCapability
    seismic: SeismicCapability
    carbon_dioxide_detector: CarbonDioxideDetectorCapability
    voltage: VoltageCapability
    ultraviolet: UltravioletCapability
    def __init__(self, switch: _Optional[_Union[SwitchCapability, _Mapping]] = ..., power_meter: _Optional[_Union[MeterCapability, _Mapping]] = ..., gas_meter: _Optional[_Union[MeterCapability, _Mapping]] = ..., water_meter: _Optional[_Union[MeterCapability, _Mapping]] = ..., open_close: _Optional[_Union[OpenCloseCapability, _Mapping]] = ..., smoke_detector: _Optional[_Union[SmokeDetectorCapability, _Mapping]] = ..., motion_detector: _Optional[_Union[MotionDetectorCapability, _Mapping]] = ..., flood_detector: _Optional[_Union[FloodDetectorCapability, _Mapping]] = ..., carbon_monoxide_detector: _Optional[_Union[CarbonMonoxideDetectorCapability, _Mapping]] = ..., thermostat: _Optional[_Union[ThermostatCapability, _Mapping]] = ..., temperature: _Optional[_Union[TemperatureCapability, _Mapping]] = ..., humidity: _Optional[_Union[HumidityCapability, _Mapping]] = ..., illumination: _Optional[_Union[IlluminationCapability, _Mapping]] = ..., direction: _Optional[_Union[DirectionCapability, _Mapping]] = ..., tamper: _Optional[_Union[TamperCapability, _Mapping]] = ..., emergency: _Optional[_Union[EmergencyCapability, _Mapping]] = ..., door: _Optional[_Union[DoorCapability, _Mapping]] = ..., tap_tap: _Optional[_Union[TapTapCapability, _Mapping]] = ..., color: _Optional[_Union[ColorCapability, _Mapping]] = ..., level: _Optional[_Union[LevelCapability, _Mapping]] = ..., battery: _Optional[_Union[BatteryCapability, _Mapping]] = ..., lock: _Optional[_Union[LockCapability, _Mapping]] = ..., remote: _Optional[_Union[RemoteCapability, _Mapping]] = ..., power_source: _Optional[_Union[PowerSourceCapability, _Mapping]] = ..., roller_shutter: _Optional[_Union[RollerShutterCapability, _Mapping]] = ..., configuration: _Optional[_Union[ConfigurationCapability, _Mapping]] = ..., doorbell: _Optional[_Union[DoorbellCapability, _Mapping]] = ..., siren: _Optional[_Union[SirenCapability, _Mapping]] = ..., accelerometer: _Optional[_Union[AccelerometerCapability, _Mapping]] = ..., seismic: _Optional[_Union[SeismicCapability, _Mapping]] = ..., carbon_dioxide_detector: _Optional[_Union[CarbonDioxideDetectorCapability, _Mapping]] = ..., voltage: _Optional[_Union[VoltageCapability, _Mapping]] = ..., ultraviolet: _Optional[_Union[UltravioletCapability, _Mapping]] = ...) -> None: ...

class SwitchCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MeterCapability(_message.Message):
    __slots__ = ["units", "reset"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    reset: bool
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ..., reset: bool = ...) -> None: ...

class OpenCloseCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SmokeDetectorCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MotionDetectorCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FloodDetectorCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CarbonMonoxideDetectorCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class CarbonDioxideDetectorCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ThermostatCapability(_message.Message):
    __slots__ = ["ranges"]
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[_thermostat_pb2.ThermostatSetpointRange]
    def __init__(self, ranges: _Optional[_Iterable[_Union[_thermostat_pb2.ThermostatSetpointRange, _Mapping]]] = ...) -> None: ...

class TemperatureCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class HumidityCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class IlluminationCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class DirectionCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class TamperCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EmergencyCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DoorCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TapTapCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ColorCapability(_message.Message):
    __slots__ = ["components"]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    components: _containers.RepeatedScalarFieldContainer[_color_pb2.ColorComponent]
    def __init__(self, components: _Optional[_Iterable[_Union[_color_pb2.ColorComponent, str]]] = ...) -> None: ...

class LevelCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class BatteryCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LockCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoteCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PowerSourceCapability(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedScalarFieldContainer[_power_source_pb2.PowerSourceEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_power_source_pb2.PowerSourceEvent, str]]] = ...) -> None: ...

class RollerShutterCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConfigurationCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DoorbellCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SirenCapability(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AccelerometerCapability(_message.Message):
    __slots__ = ["axes"]
    class Axis(_message.Message):
        __slots__ = ["axis", "units"]
        AXIS_FIELD_NUMBER: _ClassVar[int]
        UNITS_FIELD_NUMBER: _ClassVar[int]
        axis: _accelerometer_pb2.AccelerometerAxis
        units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
        def __init__(self, axis: _Optional[_Union[_accelerometer_pb2.AccelerometerAxis, str]] = ..., units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...
    AXES_FIELD_NUMBER: _ClassVar[int]
    axes: _containers.RepeatedCompositeFieldContainer[AccelerometerCapability.Axis]
    def __init__(self, axes: _Optional[_Iterable[_Union[AccelerometerCapability.Axis, _Mapping]]] = ...) -> None: ...

class SeismicCapability(_message.Message):
    __slots__ = ["intensity", "magnitude"]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    intensity: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    magnitude: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, intensity: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ..., magnitude: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class VoltageCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...

class UltravioletCapability(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[_units_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_units_pb2.Unit, str]]] = ...) -> None: ...
