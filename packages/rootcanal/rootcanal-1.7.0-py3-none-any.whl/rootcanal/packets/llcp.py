# File generated from <stdin>, with the command:
#  ./third_party/pdl/pdl-compiler/scripts/generate_python_backend.py --output py/src/rootcanal/packets/llcp.py
# /!\ Do not edit by hand.
from dataclasses import dataclass, field, fields
from typing import Optional, List, Tuple
import enum
import inspect
import math

@dataclass
class Packet:
    payload: Optional[bytes] = field(repr=False, default_factory=bytes, compare=False)

    @classmethod
    def parse_all(cls, span: bytes) -> 'Packet':
        packet, remain = getattr(cls, 'parse')(span)
        if len(remain) > 0:
            raise Exception('Unexpected parsing remainder')
        return packet

    @property
    def size(self) -> int:
        pass

    def show(self, prefix: str = ''):
        print(f'{self.__class__.__name__}')

        def print_val(p: str, pp: str, name: str, align: int, typ, val):
            if name == 'payload':
                pass

            # Scalar fields.
            elif typ is int:
                print(f'{p}{name:{align}} = {val} (0x{val:x})')

            # Byte fields.
            elif typ is bytes:
                print(f'{p}{name:{align}} = [', end='')
                line = ''
                n_pp = ''
                for (idx, b) in enumerate(val):
                    if idx > 0 and idx % 8 == 0:
                        print(f'{n_pp}{line}')
                        line = ''
                        n_pp = pp + (' ' * (align + 4))
                    line += f' {b:02x}'
                print(f'{n_pp}{line} ]')

            # Enum fields.
            elif inspect.isclass(typ) and issubclass(typ, enum.IntEnum):
                print(f'{p}{name:{align}} = {typ.__name__}::{val.name} (0x{val:x})')

            # Struct fields.
            elif inspect.isclass(typ) and issubclass(typ, globals().get('Packet')):
                print(f'{p}{name:{align}} = ', end='')
                val.show(prefix=pp)

            # Array fields.
            elif getattr(typ, '__origin__', None) == list:
                print(f'{p}{name:{align}}')
                last = len(val) - 1
                align = 5
                for (idx, elt) in enumerate(val):
                    n_p  = pp + ('├── ' if idx != last else '└── ')
                    n_pp = pp + ('│   ' if idx != last else '    ')
                    print_val(n_p, n_pp, f'[{idx}]', align, typ.__args__[0], val[idx])

            # Custom fields.
            elif inspect.isclass(typ):
                print(f'{p}{name:{align}} = {repr(val)}')

            else:
                print(f'{p}{name:{align}} = ##{typ}##')

        last = len(fields(self)) - 1
        align = max(len(f.name) for f in fields(self) if f.name != 'payload')

        for (idx, f) in enumerate(fields(self)):
            p  = prefix + ('├── ' if idx != last else '└── ')
            pp = prefix + ('│   ' if idx != last else '    ')
            val = getattr(self, f.name)

            print_val(p, pp, f.name, align, f.type, val)

class Opcode(enum.IntEnum):
    LL_CONNECTION_UPDATE_IND = 0x0
    LL_CHANNEL_MAP_IND = 0x1
    LL_TERMINATE_IND = 0x2
    LL_ENC_REQ = 0x3
    LL_ENC_RSP = 0x4
    LL_START_ENC_REQ = 0x5
    LL_START_ENC_RSP = 0x6
    LL_UNKNOWN_RSP = 0x7
    LL_FEATURE_REQ = 0x8
    LL_FEATURE_RSP = 0x9
    LL_PAUSE_ENC_REQ = 0xa
    LL_PAUSE_ENC_RSP = 0xb
    LL_VERSION_IND = 0xc
    LL_REJECT_IND = 0xd
    LL_PERIPHERAL_FEATURE_REQ = 0xe
    LL_CONNECTION_PARAM_REQ = 0xf
    LL_CONNECTION_PARAM_RSP = 0x10
    LL_REJECT_EXT_IND = 0x11
    LL_PING_REQ = 0x12
    LL_PING_RSP = 0x13
    LL_LENGTH_REQ = 0x14
    LL_LENGTH_RSP = 0x15
    LL_PHY_REQ = 0x16
    LL_PHY_RSP = 0x17
    LL_PHY_UPDATE_IND = 0x18
    LL_MIN_USED_CHANNELS_IND = 0x19
    LL_CTE_REQ = 0x1a
    LL_CTE_RSP = 0x1b
    LL_PERIODIC_SYNC_IND = 0x1c
    LL_CLOCK_ACCURACY_REQ = 0x1d
    LL_CLOCK_ACCURACY_RSP = 0x1e
    LL_CIS_REQ = 0x1f
    LL_CIS_RSP = 0x20
    LL_CIS_IND = 0x21
    LL_CIS_TERMINATE_IND = 0x22
    LL_POWER_CONTROL_REQ = 0x23
    LL_POWER_CONTROL_RSP = 0x24
    LL_POWER_CHANGE_IND = 0x25
    LL_SUBRATE_REQ = 0x26
    LL_SUBRATE_IND = 0x27
    LL_CHANNEL_REPORTING_IND = 0x28
    LL_CHANNEL_STATUS_IND = 0x29

@dataclass
class LlcpPacket(Packet):
    opcode: Opcode = field(kw_only=True, default=Opcode.LL_CONNECTION_UPDATE_IND)

    def __post_init__(self):
        pass

    @staticmethod
    def parse(span: bytes) -> Tuple['LlcpPacket', bytes]:
        fields = {'payload': None}
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['opcode'] = Opcode(span[0])
        span = span[1:]
        payload = span
        span = bytes([])
        fields['payload'] = payload
        try:
            return ConnectionUpdateInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ChannelMapInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return TerminateInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return EncReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return EncRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return StartEncReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return StartEncRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return UnknownRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return FeatureReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return FeatureRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PauseEncReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PauseEncRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return VersionInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return RejectInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PeripheralFeatureReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ConnectionParamReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ConnectionParamRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return RejectExtInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PingReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PingRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LengthReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LengthRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PhyReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PhyRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PhyUpdateInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return MinUsedChannelsInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CteReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CteRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PeriodicSyncInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ClockAccuracyReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ClockAccuracyRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CisReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CisRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CisInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CisTerminateInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PowerControlReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PowerControlRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PowerChangeInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return SubrateReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return SubrateInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ChannelReportingInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ChannelStatusInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        return LlcpPacket(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.opcode << 0))
        _span.extend(payload or self.payload or [])
        return bytes(_span)

    @property
    def size(self) -> int:
        return len(self.payload) + 1

@dataclass
class ConnectionUpdateInd(LlcpPacket):
    window_size: int = field(kw_only=True, default=0)
    window_offset: int = field(kw_only=True, default=0)
    interval: int = field(kw_only=True, default=0)
    latency: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)
    instant: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CONNECTION_UPDATE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ConnectionUpdateInd', bytes]:
        if fields['opcode'] != Opcode.LL_CONNECTION_UPDATE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 11:
            raise Exception('Invalid packet size')
        fields['window_size'] = span[0]
        value_ = int.from_bytes(span[1:3], byteorder='little')
        fields['window_offset'] = value_
        value_ = int.from_bytes(span[3:5], byteorder='little')
        fields['interval'] = value_
        value_ = int.from_bytes(span[5:7], byteorder='little')
        fields['latency'] = value_
        value_ = int.from_bytes(span[7:9], byteorder='little')
        fields['timeout'] = value_
        value_ = int.from_bytes(span[9:11], byteorder='little')
        fields['instant'] = value_
        span = span[11:]
        return ConnectionUpdateInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.window_size > 255:
            print(f"Invalid value for field ConnectionUpdateInd::window_size: {self.window_size} > 255; the value will be truncated")
            self.window_size &= 255
        _span.append((self.window_size << 0))
        if self.window_offset > 65535:
            print(f"Invalid value for field ConnectionUpdateInd::window_offset: {self.window_offset} > 65535; the value will be truncated")
            self.window_offset &= 65535
        _span.extend(int.to_bytes((self.window_offset << 0), length=2, byteorder='little'))
        if self.interval > 65535:
            print(f"Invalid value for field ConnectionUpdateInd::interval: {self.interval} > 65535; the value will be truncated")
            self.interval &= 65535
        _span.extend(int.to_bytes((self.interval << 0), length=2, byteorder='little'))
        if self.latency > 65535:
            print(f"Invalid value for field ConnectionUpdateInd::latency: {self.latency} > 65535; the value will be truncated")
            self.latency &= 65535
        _span.extend(int.to_bytes((self.latency << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field ConnectionUpdateInd::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        if self.instant > 65535:
            print(f"Invalid value for field ConnectionUpdateInd::instant: {self.instant} > 65535; the value will be truncated")
            self.instant &= 65535
        _span.extend(int.to_bytes((self.instant << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 11

@dataclass
class ChannelMapInd(LlcpPacket):
    channel_map: int = field(kw_only=True, default=0)
    instant: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CHANNEL_MAP_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ChannelMapInd', bytes]:
        if fields['opcode'] != Opcode.LL_CHANNEL_MAP_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 7:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:5], byteorder='little')
        fields['channel_map'] = value_
        value_ = int.from_bytes(span[5:7], byteorder='little')
        fields['instant'] = value_
        span = span[7:]
        return ChannelMapInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.channel_map > 1099511627775:
            print(f"Invalid value for field ChannelMapInd::channel_map: {self.channel_map} > 1099511627775; the value will be truncated")
            self.channel_map &= 1099511627775
        _span.extend(int.to_bytes((self.channel_map << 0), length=5, byteorder='little'))
        if self.instant > 65535:
            print(f"Invalid value for field ChannelMapInd::instant: {self.instant} > 65535; the value will be truncated")
            self.instant &= 65535
        _span.extend(int.to_bytes((self.instant << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 7

@dataclass
class TerminateInd(LlcpPacket):
    error_code: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_TERMINATE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['TerminateInd', bytes]:
        if fields['opcode'] != Opcode.LL_TERMINATE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['error_code'] = span[0]
        span = span[1:]
        return TerminateInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.error_code > 255:
            print(f"Invalid value for field TerminateInd::error_code: {self.error_code} > 255; the value will be truncated")
            self.error_code &= 255
        _span.append((self.error_code << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class EncReq(LlcpPacket):
    rand: int = field(kw_only=True, default=0)
    ediv: int = field(kw_only=True, default=0)
    skd_c: int = field(kw_only=True, default=0)
    iv_c: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_ENC_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['EncReq', bytes]:
        if fields['opcode'] != Opcode.LL_ENC_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 20:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['rand'] = value_
        value_ = int.from_bytes(span[8:10], byteorder='little')
        fields['ediv'] = value_
        value_ = int.from_bytes(span[10:18], byteorder='little')
        fields['skd_c'] = value_
        value_ = int.from_bytes(span[18:20], byteorder='little')
        fields['iv_c'] = value_
        span = span[20:]
        return EncReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.rand > 18446744073709551615:
            print(f"Invalid value for field EncReq::rand: {self.rand} > 18446744073709551615; the value will be truncated")
            self.rand &= 18446744073709551615
        _span.extend(int.to_bytes((self.rand << 0), length=8, byteorder='little'))
        if self.ediv > 65535:
            print(f"Invalid value for field EncReq::ediv: {self.ediv} > 65535; the value will be truncated")
            self.ediv &= 65535
        _span.extend(int.to_bytes((self.ediv << 0), length=2, byteorder='little'))
        if self.skd_c > 18446744073709551615:
            print(f"Invalid value for field EncReq::skd_c: {self.skd_c} > 18446744073709551615; the value will be truncated")
            self.skd_c &= 18446744073709551615
        _span.extend(int.to_bytes((self.skd_c << 0), length=8, byteorder='little'))
        if self.iv_c > 65535:
            print(f"Invalid value for field EncReq::iv_c: {self.iv_c} > 65535; the value will be truncated")
            self.iv_c &= 65535
        _span.extend(int.to_bytes((self.iv_c << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 20

@dataclass
class EncRsp(LlcpPacket):
    skd_p: int = field(kw_only=True, default=0)
    iv_p: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_ENC_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['EncRsp', bytes]:
        if fields['opcode'] != Opcode.LL_ENC_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 10:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['skd_p'] = value_
        value_ = int.from_bytes(span[8:10], byteorder='little')
        fields['iv_p'] = value_
        span = span[10:]
        return EncRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.skd_p > 18446744073709551615:
            print(f"Invalid value for field EncRsp::skd_p: {self.skd_p} > 18446744073709551615; the value will be truncated")
            self.skd_p &= 18446744073709551615
        _span.extend(int.to_bytes((self.skd_p << 0), length=8, byteorder='little'))
        if self.iv_p > 65535:
            print(f"Invalid value for field EncRsp::iv_p: {self.iv_p} > 65535; the value will be truncated")
            self.iv_p &= 65535
        _span.extend(int.to_bytes((self.iv_p << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 10

@dataclass
class StartEncReq(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_START_ENC_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['StartEncReq', bytes]:
        if fields['opcode'] != Opcode.LL_START_ENC_REQ:
            raise Exception("Invalid constraint field values")
        return StartEncReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class StartEncRsp(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_START_ENC_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['StartEncRsp', bytes]:
        if fields['opcode'] != Opcode.LL_START_ENC_RSP:
            raise Exception("Invalid constraint field values")
        return StartEncRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class UnknownRsp(LlcpPacket):
    unknown_type: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_UNKNOWN_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['UnknownRsp', bytes]:
        if fields['opcode'] != Opcode.LL_UNKNOWN_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['unknown_type'] = span[0]
        span = span[1:]
        return UnknownRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.unknown_type > 255:
            print(f"Invalid value for field UnknownRsp::unknown_type: {self.unknown_type} > 255; the value will be truncated")
            self.unknown_type &= 255
        _span.append((self.unknown_type << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class FeatureReq(LlcpPacket):
    feature_set: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_FEATURE_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['FeatureReq', bytes]:
        if fields['opcode'] != Opcode.LL_FEATURE_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['feature_set'] = value_
        span = span[8:]
        return FeatureReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.feature_set > 18446744073709551615:
            print(f"Invalid value for field FeatureReq::feature_set: {self.feature_set} > 18446744073709551615; the value will be truncated")
            self.feature_set &= 18446744073709551615
        _span.extend(int.to_bytes((self.feature_set << 0), length=8, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class FeatureRsp(LlcpPacket):
    feature_set: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_FEATURE_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['FeatureRsp', bytes]:
        if fields['opcode'] != Opcode.LL_FEATURE_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['feature_set'] = value_
        span = span[8:]
        return FeatureRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.feature_set > 18446744073709551615:
            print(f"Invalid value for field FeatureRsp::feature_set: {self.feature_set} > 18446744073709551615; the value will be truncated")
            self.feature_set &= 18446744073709551615
        _span.extend(int.to_bytes((self.feature_set << 0), length=8, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class PauseEncReq(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_PAUSE_ENC_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PauseEncReq', bytes]:
        if fields['opcode'] != Opcode.LL_PAUSE_ENC_REQ:
            raise Exception("Invalid constraint field values")
        return PauseEncReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class PauseEncRsp(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_PAUSE_ENC_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PauseEncRsp', bytes]:
        if fields['opcode'] != Opcode.LL_PAUSE_ENC_RSP:
            raise Exception("Invalid constraint field values")
        return PauseEncRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class VersionInd(LlcpPacket):
    version: int = field(kw_only=True, default=0)
    company_identifier: int = field(kw_only=True, default=0)
    subversion: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_VERSION_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['VersionInd', bytes]:
        if fields['opcode'] != Opcode.LL_VERSION_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 5:
            raise Exception('Invalid packet size')
        fields['version'] = span[0]
        value_ = int.from_bytes(span[1:3], byteorder='little')
        fields['company_identifier'] = value_
        value_ = int.from_bytes(span[3:5], byteorder='little')
        fields['subversion'] = value_
        span = span[5:]
        return VersionInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.version > 255:
            print(f"Invalid value for field VersionInd::version: {self.version} > 255; the value will be truncated")
            self.version &= 255
        _span.append((self.version << 0))
        if self.company_identifier > 65535:
            print(f"Invalid value for field VersionInd::company_identifier: {self.company_identifier} > 65535; the value will be truncated")
            self.company_identifier &= 65535
        _span.extend(int.to_bytes((self.company_identifier << 0), length=2, byteorder='little'))
        if self.subversion > 65535:
            print(f"Invalid value for field VersionInd::subversion: {self.subversion} > 65535; the value will be truncated")
            self.subversion &= 65535
        _span.extend(int.to_bytes((self.subversion << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 5

@dataclass
class RejectInd(LlcpPacket):
    error_code: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_REJECT_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['RejectInd', bytes]:
        if fields['opcode'] != Opcode.LL_REJECT_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['error_code'] = value_
        span = span[2:]
        return RejectInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.error_code > 65535:
            print(f"Invalid value for field RejectInd::error_code: {self.error_code} > 65535; the value will be truncated")
            self.error_code &= 65535
        _span.extend(int.to_bytes((self.error_code << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class PeripheralFeatureReq(LlcpPacket):
    feature_set: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_PERIPHERAL_FEATURE_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PeripheralFeatureReq', bytes]:
        if fields['opcode'] != Opcode.LL_PERIPHERAL_FEATURE_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['feature_set'] = value_
        span = span[8:]
        return PeripheralFeatureReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.feature_set > 18446744073709551615:
            print(f"Invalid value for field PeripheralFeatureReq::feature_set: {self.feature_set} > 18446744073709551615; the value will be truncated")
            self.feature_set &= 18446744073709551615
        _span.extend(int.to_bytes((self.feature_set << 0), length=8, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class ConnectionParamReq(LlcpPacket):
    interval_min: int = field(kw_only=True, default=0)
    interval_max: int = field(kw_only=True, default=0)
    latency: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)
    preferred_periodicity: int = field(kw_only=True, default=0)
    reference_conn_event_count: int = field(kw_only=True, default=0)
    offset0: int = field(kw_only=True, default=0)
    offset1: int = field(kw_only=True, default=0)
    offset2: int = field(kw_only=True, default=0)
    offset3: int = field(kw_only=True, default=0)
    offset4: int = field(kw_only=True, default=0)
    offset5: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CONNECTION_PARAM_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ConnectionParamReq', bytes]:
        if fields['opcode'] != Opcode.LL_CONNECTION_PARAM_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 23:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['interval_min'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['interval_max'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['timeout'] = value_
        fields['preferred_periodicity'] = span[8]
        value_ = int.from_bytes(span[9:11], byteorder='little')
        fields['reference_conn_event_count'] = value_
        value_ = int.from_bytes(span[11:13], byteorder='little')
        fields['offset0'] = value_
        value_ = int.from_bytes(span[13:15], byteorder='little')
        fields['offset1'] = value_
        value_ = int.from_bytes(span[15:17], byteorder='little')
        fields['offset2'] = value_
        value_ = int.from_bytes(span[17:19], byteorder='little')
        fields['offset3'] = value_
        value_ = int.from_bytes(span[19:21], byteorder='little')
        fields['offset4'] = value_
        value_ = int.from_bytes(span[21:23], byteorder='little')
        fields['offset5'] = value_
        span = span[23:]
        return ConnectionParamReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.interval_min > 65535:
            print(f"Invalid value for field ConnectionParamReq::interval_min: {self.interval_min} > 65535; the value will be truncated")
            self.interval_min &= 65535
        _span.extend(int.to_bytes((self.interval_min << 0), length=2, byteorder='little'))
        if self.interval_max > 65535:
            print(f"Invalid value for field ConnectionParamReq::interval_max: {self.interval_max} > 65535; the value will be truncated")
            self.interval_max &= 65535
        _span.extend(int.to_bytes((self.interval_max << 0), length=2, byteorder='little'))
        if self.latency > 65535:
            print(f"Invalid value for field ConnectionParamReq::latency: {self.latency} > 65535; the value will be truncated")
            self.latency &= 65535
        _span.extend(int.to_bytes((self.latency << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field ConnectionParamReq::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        if self.preferred_periodicity > 255:
            print(f"Invalid value for field ConnectionParamReq::preferred_periodicity: {self.preferred_periodicity} > 255; the value will be truncated")
            self.preferred_periodicity &= 255
        _span.append((self.preferred_periodicity << 0))
        if self.reference_conn_event_count > 65535:
            print(f"Invalid value for field ConnectionParamReq::reference_conn_event_count: {self.reference_conn_event_count} > 65535; the value will be truncated")
            self.reference_conn_event_count &= 65535
        _span.extend(int.to_bytes((self.reference_conn_event_count << 0), length=2, byteorder='little'))
        if self.offset0 > 65535:
            print(f"Invalid value for field ConnectionParamReq::offset0: {self.offset0} > 65535; the value will be truncated")
            self.offset0 &= 65535
        _span.extend(int.to_bytes((self.offset0 << 0), length=2, byteorder='little'))
        if self.offset1 > 65535:
            print(f"Invalid value for field ConnectionParamReq::offset1: {self.offset1} > 65535; the value will be truncated")
            self.offset1 &= 65535
        _span.extend(int.to_bytes((self.offset1 << 0), length=2, byteorder='little'))
        if self.offset2 > 65535:
            print(f"Invalid value for field ConnectionParamReq::offset2: {self.offset2} > 65535; the value will be truncated")
            self.offset2 &= 65535
        _span.extend(int.to_bytes((self.offset2 << 0), length=2, byteorder='little'))
        if self.offset3 > 65535:
            print(f"Invalid value for field ConnectionParamReq::offset3: {self.offset3} > 65535; the value will be truncated")
            self.offset3 &= 65535
        _span.extend(int.to_bytes((self.offset3 << 0), length=2, byteorder='little'))
        if self.offset4 > 65535:
            print(f"Invalid value for field ConnectionParamReq::offset4: {self.offset4} > 65535; the value will be truncated")
            self.offset4 &= 65535
        _span.extend(int.to_bytes((self.offset4 << 0), length=2, byteorder='little'))
        if self.offset5 > 65535:
            print(f"Invalid value for field ConnectionParamReq::offset5: {self.offset5} > 65535; the value will be truncated")
            self.offset5 &= 65535
        _span.extend(int.to_bytes((self.offset5 << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 23

@dataclass
class ConnectionParamRsp(LlcpPacket):
    interval_min: int = field(kw_only=True, default=0)
    interval_max: int = field(kw_only=True, default=0)
    latency: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)
    preferred_periodicity: int = field(kw_only=True, default=0)
    reference_conn_event_count: int = field(kw_only=True, default=0)
    offset0: int = field(kw_only=True, default=0)
    offset1: int = field(kw_only=True, default=0)
    offset2: int = field(kw_only=True, default=0)
    offset3: int = field(kw_only=True, default=0)
    offset4: int = field(kw_only=True, default=0)
    offset5: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CONNECTION_PARAM_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ConnectionParamRsp', bytes]:
        if fields['opcode'] != Opcode.LL_CONNECTION_PARAM_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 23:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['interval_min'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['interval_max'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['timeout'] = value_
        fields['preferred_periodicity'] = span[8]
        value_ = int.from_bytes(span[9:11], byteorder='little')
        fields['reference_conn_event_count'] = value_
        value_ = int.from_bytes(span[11:13], byteorder='little')
        fields['offset0'] = value_
        value_ = int.from_bytes(span[13:15], byteorder='little')
        fields['offset1'] = value_
        value_ = int.from_bytes(span[15:17], byteorder='little')
        fields['offset2'] = value_
        value_ = int.from_bytes(span[17:19], byteorder='little')
        fields['offset3'] = value_
        value_ = int.from_bytes(span[19:21], byteorder='little')
        fields['offset4'] = value_
        value_ = int.from_bytes(span[21:23], byteorder='little')
        fields['offset5'] = value_
        span = span[23:]
        return ConnectionParamRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.interval_min > 65535:
            print(f"Invalid value for field ConnectionParamRsp::interval_min: {self.interval_min} > 65535; the value will be truncated")
            self.interval_min &= 65535
        _span.extend(int.to_bytes((self.interval_min << 0), length=2, byteorder='little'))
        if self.interval_max > 65535:
            print(f"Invalid value for field ConnectionParamRsp::interval_max: {self.interval_max} > 65535; the value will be truncated")
            self.interval_max &= 65535
        _span.extend(int.to_bytes((self.interval_max << 0), length=2, byteorder='little'))
        if self.latency > 65535:
            print(f"Invalid value for field ConnectionParamRsp::latency: {self.latency} > 65535; the value will be truncated")
            self.latency &= 65535
        _span.extend(int.to_bytes((self.latency << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field ConnectionParamRsp::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        if self.preferred_periodicity > 255:
            print(f"Invalid value for field ConnectionParamRsp::preferred_periodicity: {self.preferred_periodicity} > 255; the value will be truncated")
            self.preferred_periodicity &= 255
        _span.append((self.preferred_periodicity << 0))
        if self.reference_conn_event_count > 65535:
            print(f"Invalid value for field ConnectionParamRsp::reference_conn_event_count: {self.reference_conn_event_count} > 65535; the value will be truncated")
            self.reference_conn_event_count &= 65535
        _span.extend(int.to_bytes((self.reference_conn_event_count << 0), length=2, byteorder='little'))
        if self.offset0 > 65535:
            print(f"Invalid value for field ConnectionParamRsp::offset0: {self.offset0} > 65535; the value will be truncated")
            self.offset0 &= 65535
        _span.extend(int.to_bytes((self.offset0 << 0), length=2, byteorder='little'))
        if self.offset1 > 65535:
            print(f"Invalid value for field ConnectionParamRsp::offset1: {self.offset1} > 65535; the value will be truncated")
            self.offset1 &= 65535
        _span.extend(int.to_bytes((self.offset1 << 0), length=2, byteorder='little'))
        if self.offset2 > 65535:
            print(f"Invalid value for field ConnectionParamRsp::offset2: {self.offset2} > 65535; the value will be truncated")
            self.offset2 &= 65535
        _span.extend(int.to_bytes((self.offset2 << 0), length=2, byteorder='little'))
        if self.offset3 > 65535:
            print(f"Invalid value for field ConnectionParamRsp::offset3: {self.offset3} > 65535; the value will be truncated")
            self.offset3 &= 65535
        _span.extend(int.to_bytes((self.offset3 << 0), length=2, byteorder='little'))
        if self.offset4 > 65535:
            print(f"Invalid value for field ConnectionParamRsp::offset4: {self.offset4} > 65535; the value will be truncated")
            self.offset4 &= 65535
        _span.extend(int.to_bytes((self.offset4 << 0), length=2, byteorder='little'))
        if self.offset5 > 65535:
            print(f"Invalid value for field ConnectionParamRsp::offset5: {self.offset5} > 65535; the value will be truncated")
            self.offset5 &= 65535
        _span.extend(int.to_bytes((self.offset5 << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 23

@dataclass
class RejectExtInd(LlcpPacket):
    reject_opcode: int = field(kw_only=True, default=0)
    error_code: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_REJECT_EXT_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['RejectExtInd', bytes]:
        if fields['opcode'] != Opcode.LL_REJECT_EXT_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['reject_opcode'] = span[0]
        fields['error_code'] = span[1]
        span = span[2:]
        return RejectExtInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.reject_opcode > 255:
            print(f"Invalid value for field RejectExtInd::reject_opcode: {self.reject_opcode} > 255; the value will be truncated")
            self.reject_opcode &= 255
        _span.append((self.reject_opcode << 0))
        if self.error_code > 255:
            print(f"Invalid value for field RejectExtInd::error_code: {self.error_code} > 255; the value will be truncated")
            self.error_code &= 255
        _span.append((self.error_code << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class PingReq(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_PING_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PingReq', bytes]:
        if fields['opcode'] != Opcode.LL_PING_REQ:
            raise Exception("Invalid constraint field values")
        return PingReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class PingRsp(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_PING_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PingRsp', bytes]:
        if fields['opcode'] != Opcode.LL_PING_RSP:
            raise Exception("Invalid constraint field values")
        return PingRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class LengthReq(LlcpPacket):
    max_rx_octets: int = field(kw_only=True, default=0)
    max_rx_time: int = field(kw_only=True, default=0)
    max_tx_octets: int = field(kw_only=True, default=0)
    max_tx_time: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_LENGTH_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LengthReq', bytes]:
        if fields['opcode'] != Opcode.LL_LENGTH_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['max_rx_octets'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['max_rx_time'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['max_tx_octets'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['max_tx_time'] = value_
        span = span[8:]
        return LengthReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.max_rx_octets > 65535:
            print(f"Invalid value for field LengthReq::max_rx_octets: {self.max_rx_octets} > 65535; the value will be truncated")
            self.max_rx_octets &= 65535
        _span.extend(int.to_bytes((self.max_rx_octets << 0), length=2, byteorder='little'))
        if self.max_rx_time > 65535:
            print(f"Invalid value for field LengthReq::max_rx_time: {self.max_rx_time} > 65535; the value will be truncated")
            self.max_rx_time &= 65535
        _span.extend(int.to_bytes((self.max_rx_time << 0), length=2, byteorder='little'))
        if self.max_tx_octets > 65535:
            print(f"Invalid value for field LengthReq::max_tx_octets: {self.max_tx_octets} > 65535; the value will be truncated")
            self.max_tx_octets &= 65535
        _span.extend(int.to_bytes((self.max_tx_octets << 0), length=2, byteorder='little'))
        if self.max_tx_time > 65535:
            print(f"Invalid value for field LengthReq::max_tx_time: {self.max_tx_time} > 65535; the value will be truncated")
            self.max_tx_time &= 65535
        _span.extend(int.to_bytes((self.max_tx_time << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class LengthRsp(LlcpPacket):
    max_rx_octets: int = field(kw_only=True, default=0)
    max_rx_time: int = field(kw_only=True, default=0)
    max_tx_octets: int = field(kw_only=True, default=0)
    max_tx_time: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_LENGTH_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LengthRsp', bytes]:
        if fields['opcode'] != Opcode.LL_LENGTH_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['max_rx_octets'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['max_rx_time'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['max_tx_octets'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['max_tx_time'] = value_
        span = span[8:]
        return LengthRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.max_rx_octets > 65535:
            print(f"Invalid value for field LengthRsp::max_rx_octets: {self.max_rx_octets} > 65535; the value will be truncated")
            self.max_rx_octets &= 65535
        _span.extend(int.to_bytes((self.max_rx_octets << 0), length=2, byteorder='little'))
        if self.max_rx_time > 65535:
            print(f"Invalid value for field LengthRsp::max_rx_time: {self.max_rx_time} > 65535; the value will be truncated")
            self.max_rx_time &= 65535
        _span.extend(int.to_bytes((self.max_rx_time << 0), length=2, byteorder='little'))
        if self.max_tx_octets > 65535:
            print(f"Invalid value for field LengthRsp::max_tx_octets: {self.max_tx_octets} > 65535; the value will be truncated")
            self.max_tx_octets &= 65535
        _span.extend(int.to_bytes((self.max_tx_octets << 0), length=2, byteorder='little'))
        if self.max_tx_time > 65535:
            print(f"Invalid value for field LengthRsp::max_tx_time: {self.max_tx_time} > 65535; the value will be truncated")
            self.max_tx_time &= 65535
        _span.extend(int.to_bytes((self.max_tx_time << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class PhyReq(LlcpPacket):
    tx_phys: int = field(kw_only=True, default=0)
    rx_phys: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_PHY_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PhyReq', bytes]:
        if fields['opcode'] != Opcode.LL_PHY_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['tx_phys'] = span[0]
        fields['rx_phys'] = span[1]
        span = span[2:]
        return PhyReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.tx_phys > 255:
            print(f"Invalid value for field PhyReq::tx_phys: {self.tx_phys} > 255; the value will be truncated")
            self.tx_phys &= 255
        _span.append((self.tx_phys << 0))
        if self.rx_phys > 255:
            print(f"Invalid value for field PhyReq::rx_phys: {self.rx_phys} > 255; the value will be truncated")
            self.rx_phys &= 255
        _span.append((self.rx_phys << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class PhyRsp(LlcpPacket):
    tx_phys: int = field(kw_only=True, default=0)
    rx_phys: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_PHY_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PhyRsp', bytes]:
        if fields['opcode'] != Opcode.LL_PHY_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['tx_phys'] = span[0]
        fields['rx_phys'] = span[1]
        span = span[2:]
        return PhyRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.tx_phys > 255:
            print(f"Invalid value for field PhyRsp::tx_phys: {self.tx_phys} > 255; the value will be truncated")
            self.tx_phys &= 255
        _span.append((self.tx_phys << 0))
        if self.rx_phys > 255:
            print(f"Invalid value for field PhyRsp::rx_phys: {self.rx_phys} > 255; the value will be truncated")
            self.rx_phys &= 255
        _span.append((self.rx_phys << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class PhyUpdateInd(LlcpPacket):
    phy_c_to_p: int = field(kw_only=True, default=0)
    phy_p_to_c: int = field(kw_only=True, default=0)
    instant: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_PHY_UPDATE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PhyUpdateInd', bytes]:
        if fields['opcode'] != Opcode.LL_PHY_UPDATE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['phy_c_to_p'] = span[0]
        fields['phy_p_to_c'] = span[1]
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['instant'] = value_
        span = span[4:]
        return PhyUpdateInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.phy_c_to_p > 255:
            print(f"Invalid value for field PhyUpdateInd::phy_c_to_p: {self.phy_c_to_p} > 255; the value will be truncated")
            self.phy_c_to_p &= 255
        _span.append((self.phy_c_to_p << 0))
        if self.phy_p_to_c > 255:
            print(f"Invalid value for field PhyUpdateInd::phy_p_to_c: {self.phy_p_to_c} > 255; the value will be truncated")
            self.phy_p_to_c &= 255
        _span.append((self.phy_p_to_c << 0))
        if self.instant > 65535:
            print(f"Invalid value for field PhyUpdateInd::instant: {self.instant} > 65535; the value will be truncated")
            self.instant &= 65535
        _span.extend(int.to_bytes((self.instant << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4

@dataclass
class MinUsedChannelsInd(LlcpPacket):
    phys: int = field(kw_only=True, default=0)
    min_used_channels: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_MIN_USED_CHANNELS_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['MinUsedChannelsInd', bytes]:
        if fields['opcode'] != Opcode.LL_MIN_USED_CHANNELS_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['phys'] = span[0]
        fields['min_used_channels'] = span[1]
        span = span[2:]
        return MinUsedChannelsInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.phys > 255:
            print(f"Invalid value for field MinUsedChannelsInd::phys: {self.phys} > 255; the value will be truncated")
            self.phys &= 255
        _span.append((self.phys << 0))
        if self.min_used_channels > 255:
            print(f"Invalid value for field MinUsedChannelsInd::min_used_channels: {self.min_used_channels} > 255; the value will be truncated")
            self.min_used_channels &= 255
        _span.append((self.min_used_channels << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class CteReq(LlcpPacket):
    min_cte_len_req: int = field(kw_only=True, default=0)
    cte_type_req: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CTE_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CteReq', bytes]:
        if fields['opcode'] != Opcode.LL_CTE_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['min_cte_len_req'] = (span[0] >> 0) & 0x1f
        fields['cte_type_req'] = (span[0] >> 6) & 0x3
        span = span[1:]
        return CteReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.min_cte_len_req > 31:
            print(f"Invalid value for field CteReq::min_cte_len_req: {self.min_cte_len_req} > 31; the value will be truncated")
            self.min_cte_len_req &= 31
        if self.cte_type_req > 3:
            print(f"Invalid value for field CteReq::cte_type_req: {self.cte_type_req} > 3; the value will be truncated")
            self.cte_type_req &= 3
        _value = (
            (self.min_cte_len_req << 0) |
            (self.cte_type_req << 6)
        )
        _span.append(_value)
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class CteRsp(LlcpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.LL_CTE_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CteRsp', bytes]:
        if fields['opcode'] != Opcode.LL_CTE_RSP:
            raise Exception("Invalid constraint field values")
        return CteRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class PeriodicSyncInd(LlcpPacket):
    id: int = field(kw_only=True, default=0)
    sync_info: bytearray = field(kw_only=True, default_factory=bytearray)
    conn_event_count: int = field(kw_only=True, default=0)
    last_pa_event_counter: int = field(kw_only=True, default=0)
    sid: int = field(kw_only=True, default=0)
    atype: int = field(kw_only=True, default=0)
    sca: int = field(kw_only=True, default=0)
    phy: int = field(kw_only=True, default=0)
    adva: int = field(kw_only=True, default=0)
    sync_conn_event_count: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_PERIODIC_SYNC_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PeriodicSyncInd', bytes]:
        if fields['opcode'] != Opcode.LL_PERIODIC_SYNC_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['id'] = value_
        span = span[2:]
        if len(span) < 18:
            raise Exception('Invalid packet size')
        fields['sync_info'] = list(span[:18])
        span = span[18:]
        if len(span) < 14:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['conn_event_count'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['last_pa_event_counter'] = value_
        fields['sid'] = (span[4] >> 0) & 0xf
        fields['atype'] = (span[4] >> 4) & 0x1
        fields['sca'] = (span[4] >> 5) & 0x7
        fields['phy'] = span[5]
        value_ = int.from_bytes(span[6:12], byteorder='little')
        fields['adva'] = value_
        value_ = int.from_bytes(span[12:14], byteorder='little')
        fields['sync_conn_event_count'] = value_
        span = span[14:]
        return PeriodicSyncInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.id > 65535:
            print(f"Invalid value for field PeriodicSyncInd::id: {self.id} > 65535; the value will be truncated")
            self.id &= 65535
        _span.extend(int.to_bytes((self.id << 0), length=2, byteorder='little'))
        _span.extend(self.sync_info)
        if self.conn_event_count > 65535:
            print(f"Invalid value for field PeriodicSyncInd::conn_event_count: {self.conn_event_count} > 65535; the value will be truncated")
            self.conn_event_count &= 65535
        _span.extend(int.to_bytes((self.conn_event_count << 0), length=2, byteorder='little'))
        if self.last_pa_event_counter > 65535:
            print(f"Invalid value for field PeriodicSyncInd::last_pa_event_counter: {self.last_pa_event_counter} > 65535; the value will be truncated")
            self.last_pa_event_counter &= 65535
        _span.extend(int.to_bytes((self.last_pa_event_counter << 0), length=2, byteorder='little'))
        if self.sid > 15:
            print(f"Invalid value for field PeriodicSyncInd::sid: {self.sid} > 15; the value will be truncated")
            self.sid &= 15
        if self.atype > 1:
            print(f"Invalid value for field PeriodicSyncInd::atype: {self.atype} > 1; the value will be truncated")
            self.atype &= 1
        if self.sca > 7:
            print(f"Invalid value for field PeriodicSyncInd::sca: {self.sca} > 7; the value will be truncated")
            self.sca &= 7
        _value = (
            (self.sid << 0) |
            (self.atype << 4) |
            (self.sca << 5)
        )
        _span.append(_value)
        if self.phy > 255:
            print(f"Invalid value for field PeriodicSyncInd::phy: {self.phy} > 255; the value will be truncated")
            self.phy &= 255
        _span.append((self.phy << 0))
        if self.adva > 281474976710655:
            print(f"Invalid value for field PeriodicSyncInd::adva: {self.adva} > 281474976710655; the value will be truncated")
            self.adva &= 281474976710655
        _span.extend(int.to_bytes((self.adva << 0), length=6, byteorder='little'))
        if self.sync_conn_event_count > 65535:
            print(f"Invalid value for field PeriodicSyncInd::sync_conn_event_count: {self.sync_conn_event_count} > 65535; the value will be truncated")
            self.sync_conn_event_count &= 65535
        _span.extend(int.to_bytes((self.sync_conn_event_count << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 34

@dataclass
class ClockAccuracyReq(LlcpPacket):
    sca: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CLOCK_ACCURACY_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ClockAccuracyReq', bytes]:
        if fields['opcode'] != Opcode.LL_CLOCK_ACCURACY_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['sca'] = span[0]
        span = span[1:]
        return ClockAccuracyReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.sca > 255:
            print(f"Invalid value for field ClockAccuracyReq::sca: {self.sca} > 255; the value will be truncated")
            self.sca &= 255
        _span.append((self.sca << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class ClockAccuracyRsp(LlcpPacket):
    sca: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CLOCK_ACCURACY_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ClockAccuracyRsp', bytes]:
        if fields['opcode'] != Opcode.LL_CLOCK_ACCURACY_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['sca'] = span[0]
        span = span[1:]
        return ClockAccuracyRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.sca > 255:
            print(f"Invalid value for field ClockAccuracyRsp::sca: {self.sca} > 255; the value will be truncated")
            self.sca &= 255
        _span.append((self.sca << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class CisReq(LlcpPacket):
    cig_id: int = field(kw_only=True, default=0)
    cis_id: int = field(kw_only=True, default=0)
    phy_c_to_p: int = field(kw_only=True, default=0)
    phy_p_to_c: int = field(kw_only=True, default=0)
    framed: int = field(kw_only=True, default=0)
    max_sdu_c_to_p: int = field(kw_only=True, default=0)
    max_sdu_p_to_c: int = field(kw_only=True, default=0)
    sdu_interval_c_to_p: int = field(kw_only=True, default=0)
    sdu_interval_p_to_c: int = field(kw_only=True, default=0)
    max_pdu_c_to_p: int = field(kw_only=True, default=0)
    max_pdu_p_to_c: int = field(kw_only=True, default=0)
    nse: int = field(kw_only=True, default=0)
    sub_interval: int = field(kw_only=True, default=0)
    bn_p_to_c: int = field(kw_only=True, default=0)
    bn_c_to_p: int = field(kw_only=True, default=0)
    ft_c_to_p: int = field(kw_only=True, default=0)
    ft_p_to_c: int = field(kw_only=True, default=0)
    iso_interval: int = field(kw_only=True, default=0)
    cis_offset_min: int = field(kw_only=True, default=0)
    cis_offset_max: int = field(kw_only=True, default=0)
    conn_event_count: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CIS_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CisReq', bytes]:
        if fields['opcode'] != Opcode.LL_CIS_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 35:
            raise Exception('Invalid packet size')
        fields['cig_id'] = span[0]
        fields['cis_id'] = span[1]
        fields['phy_c_to_p'] = span[2]
        fields['phy_p_to_c'] = span[3]
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['framed'] = (value_ >> 0) & 0x1
        fields['max_sdu_c_to_p'] = (value_ >> 4) & 0xfff
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['max_sdu_p_to_c'] = (value_ >> 4) & 0xfff
        value_ = int.from_bytes(span[8:11], byteorder='little')
        fields['sdu_interval_c_to_p'] = (value_ >> 4) & 0xfffff
        value_ = int.from_bytes(span[11:14], byteorder='little')
        fields['sdu_interval_p_to_c'] = (value_ >> 4) & 0xfffff
        value_ = int.from_bytes(span[14:16], byteorder='little')
        fields['max_pdu_c_to_p'] = value_
        value_ = int.from_bytes(span[16:18], byteorder='little')
        fields['max_pdu_p_to_c'] = value_
        fields['nse'] = span[18]
        value_ = int.from_bytes(span[19:22], byteorder='little')
        fields['sub_interval'] = value_
        fields['bn_p_to_c'] = (span[22] >> 0) & 0xf
        fields['bn_c_to_p'] = (span[22] >> 4) & 0xf
        fields['ft_c_to_p'] = span[23]
        fields['ft_p_to_c'] = span[24]
        value_ = int.from_bytes(span[25:27], byteorder='little')
        fields['iso_interval'] = value_
        value_ = int.from_bytes(span[27:30], byteorder='little')
        fields['cis_offset_min'] = value_
        value_ = int.from_bytes(span[30:33], byteorder='little')
        fields['cis_offset_max'] = value_
        value_ = int.from_bytes(span[33:35], byteorder='little')
        fields['conn_event_count'] = value_
        span = span[35:]
        return CisReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.cig_id > 255:
            print(f"Invalid value for field CisReq::cig_id: {self.cig_id} > 255; the value will be truncated")
            self.cig_id &= 255
        _span.append((self.cig_id << 0))
        if self.cis_id > 255:
            print(f"Invalid value for field CisReq::cis_id: {self.cis_id} > 255; the value will be truncated")
            self.cis_id &= 255
        _span.append((self.cis_id << 0))
        if self.phy_c_to_p > 255:
            print(f"Invalid value for field CisReq::phy_c_to_p: {self.phy_c_to_p} > 255; the value will be truncated")
            self.phy_c_to_p &= 255
        _span.append((self.phy_c_to_p << 0))
        if self.phy_p_to_c > 255:
            print(f"Invalid value for field CisReq::phy_p_to_c: {self.phy_p_to_c} > 255; the value will be truncated")
            self.phy_p_to_c &= 255
        _span.append((self.phy_p_to_c << 0))
        if self.framed > 1:
            print(f"Invalid value for field CisReq::framed: {self.framed} > 1; the value will be truncated")
            self.framed &= 1
        if self.max_sdu_c_to_p > 4095:
            print(f"Invalid value for field CisReq::max_sdu_c_to_p: {self.max_sdu_c_to_p} > 4095; the value will be truncated")
            self.max_sdu_c_to_p &= 4095
        _value = (
            (self.framed << 0) |
            (self.max_sdu_c_to_p << 4)
        )
        _span.extend(int.to_bytes(_value, length=2, byteorder='little'))
        if self.max_sdu_p_to_c > 4095:
            print(f"Invalid value for field CisReq::max_sdu_p_to_c: {self.max_sdu_p_to_c} > 4095; the value will be truncated")
            self.max_sdu_p_to_c &= 4095
        _span.extend(int.to_bytes((self.max_sdu_p_to_c << 4), length=2, byteorder='little'))
        if self.sdu_interval_c_to_p > 1048575:
            print(f"Invalid value for field CisReq::sdu_interval_c_to_p: {self.sdu_interval_c_to_p} > 1048575; the value will be truncated")
            self.sdu_interval_c_to_p &= 1048575
        _span.extend(int.to_bytes((self.sdu_interval_c_to_p << 4), length=3, byteorder='little'))
        if self.sdu_interval_p_to_c > 1048575:
            print(f"Invalid value for field CisReq::sdu_interval_p_to_c: {self.sdu_interval_p_to_c} > 1048575; the value will be truncated")
            self.sdu_interval_p_to_c &= 1048575
        _span.extend(int.to_bytes((self.sdu_interval_p_to_c << 4), length=3, byteorder='little'))
        if self.max_pdu_c_to_p > 65535:
            print(f"Invalid value for field CisReq::max_pdu_c_to_p: {self.max_pdu_c_to_p} > 65535; the value will be truncated")
            self.max_pdu_c_to_p &= 65535
        _span.extend(int.to_bytes((self.max_pdu_c_to_p << 0), length=2, byteorder='little'))
        if self.max_pdu_p_to_c > 65535:
            print(f"Invalid value for field CisReq::max_pdu_p_to_c: {self.max_pdu_p_to_c} > 65535; the value will be truncated")
            self.max_pdu_p_to_c &= 65535
        _span.extend(int.to_bytes((self.max_pdu_p_to_c << 0), length=2, byteorder='little'))
        if self.nse > 255:
            print(f"Invalid value for field CisReq::nse: {self.nse} > 255; the value will be truncated")
            self.nse &= 255
        _span.append((self.nse << 0))
        if self.sub_interval > 16777215:
            print(f"Invalid value for field CisReq::sub_interval: {self.sub_interval} > 16777215; the value will be truncated")
            self.sub_interval &= 16777215
        _span.extend(int.to_bytes((self.sub_interval << 0), length=3, byteorder='little'))
        if self.bn_p_to_c > 15:
            print(f"Invalid value for field CisReq::bn_p_to_c: {self.bn_p_to_c} > 15; the value will be truncated")
            self.bn_p_to_c &= 15
        if self.bn_c_to_p > 15:
            print(f"Invalid value for field CisReq::bn_c_to_p: {self.bn_c_to_p} > 15; the value will be truncated")
            self.bn_c_to_p &= 15
        _value = (
            (self.bn_p_to_c << 0) |
            (self.bn_c_to_p << 4)
        )
        _span.append(_value)
        if self.ft_c_to_p > 255:
            print(f"Invalid value for field CisReq::ft_c_to_p: {self.ft_c_to_p} > 255; the value will be truncated")
            self.ft_c_to_p &= 255
        _span.append((self.ft_c_to_p << 0))
        if self.ft_p_to_c > 255:
            print(f"Invalid value for field CisReq::ft_p_to_c: {self.ft_p_to_c} > 255; the value will be truncated")
            self.ft_p_to_c &= 255
        _span.append((self.ft_p_to_c << 0))
        if self.iso_interval > 65535:
            print(f"Invalid value for field CisReq::iso_interval: {self.iso_interval} > 65535; the value will be truncated")
            self.iso_interval &= 65535
        _span.extend(int.to_bytes((self.iso_interval << 0), length=2, byteorder='little'))
        if self.cis_offset_min > 16777215:
            print(f"Invalid value for field CisReq::cis_offset_min: {self.cis_offset_min} > 16777215; the value will be truncated")
            self.cis_offset_min &= 16777215
        _span.extend(int.to_bytes((self.cis_offset_min << 0), length=3, byteorder='little'))
        if self.cis_offset_max > 16777215:
            print(f"Invalid value for field CisReq::cis_offset_max: {self.cis_offset_max} > 16777215; the value will be truncated")
            self.cis_offset_max &= 16777215
        _span.extend(int.to_bytes((self.cis_offset_max << 0), length=3, byteorder='little'))
        if self.conn_event_count > 65535:
            print(f"Invalid value for field CisReq::conn_event_count: {self.conn_event_count} > 65535; the value will be truncated")
            self.conn_event_count &= 65535
        _span.extend(int.to_bytes((self.conn_event_count << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 35

@dataclass
class CisRsp(LlcpPacket):
    cis_offset_min: int = field(kw_only=True, default=0)
    cis_offset_max: int = field(kw_only=True, default=0)
    conn_event_count: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CIS_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CisRsp', bytes]:
        if fields['opcode'] != Opcode.LL_CIS_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:3], byteorder='little')
        fields['cis_offset_min'] = value_
        value_ = int.from_bytes(span[3:6], byteorder='little')
        fields['cis_offset_max'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['conn_event_count'] = value_
        span = span[8:]
        return CisRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.cis_offset_min > 16777215:
            print(f"Invalid value for field CisRsp::cis_offset_min: {self.cis_offset_min} > 16777215; the value will be truncated")
            self.cis_offset_min &= 16777215
        _span.extend(int.to_bytes((self.cis_offset_min << 0), length=3, byteorder='little'))
        if self.cis_offset_max > 16777215:
            print(f"Invalid value for field CisRsp::cis_offset_max: {self.cis_offset_max} > 16777215; the value will be truncated")
            self.cis_offset_max &= 16777215
        _span.extend(int.to_bytes((self.cis_offset_max << 0), length=3, byteorder='little'))
        if self.conn_event_count > 65535:
            print(f"Invalid value for field CisRsp::conn_event_count: {self.conn_event_count} > 65535; the value will be truncated")
            self.conn_event_count &= 65535
        _span.extend(int.to_bytes((self.conn_event_count << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class CisInd(LlcpPacket):
    aa: int = field(kw_only=True, default=0)
    cis_offset: int = field(kw_only=True, default=0)
    cig_sync_delay: int = field(kw_only=True, default=0)
    cis_sync_delay: int = field(kw_only=True, default=0)
    conn_event_count: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CIS_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CisInd', bytes]:
        if fields['opcode'] != Opcode.LL_CIS_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 15:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:4], byteorder='little')
        fields['aa'] = value_
        value_ = int.from_bytes(span[4:7], byteorder='little')
        fields['cis_offset'] = value_
        value_ = int.from_bytes(span[7:10], byteorder='little')
        fields['cig_sync_delay'] = value_
        value_ = int.from_bytes(span[10:13], byteorder='little')
        fields['cis_sync_delay'] = value_
        value_ = int.from_bytes(span[13:15], byteorder='little')
        fields['conn_event_count'] = value_
        span = span[15:]
        return CisInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.aa > 4294967295:
            print(f"Invalid value for field CisInd::aa: {self.aa} > 4294967295; the value will be truncated")
            self.aa &= 4294967295
        _span.extend(int.to_bytes((self.aa << 0), length=4, byteorder='little'))
        if self.cis_offset > 16777215:
            print(f"Invalid value for field CisInd::cis_offset: {self.cis_offset} > 16777215; the value will be truncated")
            self.cis_offset &= 16777215
        _span.extend(int.to_bytes((self.cis_offset << 0), length=3, byteorder='little'))
        if self.cig_sync_delay > 16777215:
            print(f"Invalid value for field CisInd::cig_sync_delay: {self.cig_sync_delay} > 16777215; the value will be truncated")
            self.cig_sync_delay &= 16777215
        _span.extend(int.to_bytes((self.cig_sync_delay << 0), length=3, byteorder='little'))
        if self.cis_sync_delay > 16777215:
            print(f"Invalid value for field CisInd::cis_sync_delay: {self.cis_sync_delay} > 16777215; the value will be truncated")
            self.cis_sync_delay &= 16777215
        _span.extend(int.to_bytes((self.cis_sync_delay << 0), length=3, byteorder='little'))
        if self.conn_event_count > 65535:
            print(f"Invalid value for field CisInd::conn_event_count: {self.conn_event_count} > 65535; the value will be truncated")
            self.conn_event_count &= 65535
        _span.extend(int.to_bytes((self.conn_event_count << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 15

@dataclass
class CisTerminateInd(LlcpPacket):
    cig_id: int = field(kw_only=True, default=0)
    cis_id: int = field(kw_only=True, default=0)
    error_code: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CIS_TERMINATE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CisTerminateInd', bytes]:
        if fields['opcode'] != Opcode.LL_CIS_TERMINATE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['cig_id'] = span[0]
        fields['cis_id'] = span[1]
        fields['error_code'] = span[2]
        span = span[3:]
        return CisTerminateInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.cig_id > 255:
            print(f"Invalid value for field CisTerminateInd::cig_id: {self.cig_id} > 255; the value will be truncated")
            self.cig_id &= 255
        _span.append((self.cig_id << 0))
        if self.cis_id > 255:
            print(f"Invalid value for field CisTerminateInd::cis_id: {self.cis_id} > 255; the value will be truncated")
            self.cis_id &= 255
        _span.append((self.cis_id << 0))
        if self.error_code > 255:
            print(f"Invalid value for field CisTerminateInd::error_code: {self.error_code} > 255; the value will be truncated")
            self.error_code &= 255
        _span.append((self.error_code << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 3

@dataclass
class PowerControlReq(LlcpPacket):
    phy: int = field(kw_only=True, default=0)
    delta: int = field(kw_only=True, default=0)
    tx_power: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_POWER_CONTROL_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PowerControlReq', bytes]:
        if fields['opcode'] != Opcode.LL_POWER_CONTROL_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['phy'] = span[0]
        fields['delta'] = span[1]
        fields['tx_power'] = span[2]
        span = span[3:]
        return PowerControlReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.phy > 255:
            print(f"Invalid value for field PowerControlReq::phy: {self.phy} > 255; the value will be truncated")
            self.phy &= 255
        _span.append((self.phy << 0))
        if self.delta > 255:
            print(f"Invalid value for field PowerControlReq::delta: {self.delta} > 255; the value will be truncated")
            self.delta &= 255
        _span.append((self.delta << 0))
        if self.tx_power > 255:
            print(f"Invalid value for field PowerControlReq::tx_power: {self.tx_power} > 255; the value will be truncated")
            self.tx_power &= 255
        _span.append((self.tx_power << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 3

@dataclass
class PowerControlRsp(LlcpPacket):
    min: int = field(kw_only=True, default=0)
    max: int = field(kw_only=True, default=0)
    delta: int = field(kw_only=True, default=0)
    tx_power: int = field(kw_only=True, default=0)
    apr: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_POWER_CONTROL_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PowerControlRsp', bytes]:
        if fields['opcode'] != Opcode.LL_POWER_CONTROL_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['min'] = (span[0] >> 0) & 0x1
        fields['max'] = (span[0] >> 1) & 0x1
        fields['delta'] = span[1]
        fields['tx_power'] = span[2]
        fields['apr'] = span[3]
        span = span[4:]
        return PowerControlRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.min > 1:
            print(f"Invalid value for field PowerControlRsp::min: {self.min} > 1; the value will be truncated")
            self.min &= 1
        if self.max > 1:
            print(f"Invalid value for field PowerControlRsp::max: {self.max} > 1; the value will be truncated")
            self.max &= 1
        _value = (
            (self.min << 0) |
            (self.max << 1)
        )
        _span.append(_value)
        if self.delta > 255:
            print(f"Invalid value for field PowerControlRsp::delta: {self.delta} > 255; the value will be truncated")
            self.delta &= 255
        _span.append((self.delta << 0))
        if self.tx_power > 255:
            print(f"Invalid value for field PowerControlRsp::tx_power: {self.tx_power} > 255; the value will be truncated")
            self.tx_power &= 255
        _span.append((self.tx_power << 0))
        if self.apr > 255:
            print(f"Invalid value for field PowerControlRsp::apr: {self.apr} > 255; the value will be truncated")
            self.apr &= 255
        _span.append((self.apr << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4

@dataclass
class PowerChangeInd(LlcpPacket):
    phy: int = field(kw_only=True, default=0)
    min: int = field(kw_only=True, default=0)
    max: int = field(kw_only=True, default=0)
    delta: int = field(kw_only=True, default=0)
    tx_power: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_POWER_CHANGE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PowerChangeInd', bytes]:
        if fields['opcode'] != Opcode.LL_POWER_CHANGE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['phy'] = span[0]
        fields['min'] = (span[1] >> 0) & 0x1
        fields['max'] = (span[1] >> 1) & 0x1
        fields['delta'] = span[2]
        fields['tx_power'] = span[3]
        span = span[4:]
        return PowerChangeInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.phy > 255:
            print(f"Invalid value for field PowerChangeInd::phy: {self.phy} > 255; the value will be truncated")
            self.phy &= 255
        _span.append((self.phy << 0))
        if self.min > 1:
            print(f"Invalid value for field PowerChangeInd::min: {self.min} > 1; the value will be truncated")
            self.min &= 1
        if self.max > 1:
            print(f"Invalid value for field PowerChangeInd::max: {self.max} > 1; the value will be truncated")
            self.max &= 1
        _value = (
            (self.min << 0) |
            (self.max << 1)
        )
        _span.append(_value)
        if self.delta > 255:
            print(f"Invalid value for field PowerChangeInd::delta: {self.delta} > 255; the value will be truncated")
            self.delta &= 255
        _span.append((self.delta << 0))
        if self.tx_power > 255:
            print(f"Invalid value for field PowerChangeInd::tx_power: {self.tx_power} > 255; the value will be truncated")
            self.tx_power &= 255
        _span.append((self.tx_power << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4

@dataclass
class SubrateReq(LlcpPacket):
    subrate_factor_min: int = field(kw_only=True, default=0)
    subrate_factor_max: int = field(kw_only=True, default=0)
    max_latency: int = field(kw_only=True, default=0)
    continuation_number: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_SUBRATE_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['SubrateReq', bytes]:
        if fields['opcode'] != Opcode.LL_SUBRATE_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 10:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['subrate_factor_min'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['subrate_factor_max'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['max_latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['continuation_number'] = value_
        value_ = int.from_bytes(span[8:10], byteorder='little')
        fields['timeout'] = value_
        span = span[10:]
        return SubrateReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.subrate_factor_min > 65535:
            print(f"Invalid value for field SubrateReq::subrate_factor_min: {self.subrate_factor_min} > 65535; the value will be truncated")
            self.subrate_factor_min &= 65535
        _span.extend(int.to_bytes((self.subrate_factor_min << 0), length=2, byteorder='little'))
        if self.subrate_factor_max > 65535:
            print(f"Invalid value for field SubrateReq::subrate_factor_max: {self.subrate_factor_max} > 65535; the value will be truncated")
            self.subrate_factor_max &= 65535
        _span.extend(int.to_bytes((self.subrate_factor_max << 0), length=2, byteorder='little'))
        if self.max_latency > 65535:
            print(f"Invalid value for field SubrateReq::max_latency: {self.max_latency} > 65535; the value will be truncated")
            self.max_latency &= 65535
        _span.extend(int.to_bytes((self.max_latency << 0), length=2, byteorder='little'))
        if self.continuation_number > 65535:
            print(f"Invalid value for field SubrateReq::continuation_number: {self.continuation_number} > 65535; the value will be truncated")
            self.continuation_number &= 65535
        _span.extend(int.to_bytes((self.continuation_number << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field SubrateReq::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 10

@dataclass
class SubrateInd(LlcpPacket):
    subrate_factor: int = field(kw_only=True, default=0)
    subrate_base_event: int = field(kw_only=True, default=0)
    latency: int = field(kw_only=True, default=0)
    continuation_number: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_SUBRATE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['SubrateInd', bytes]:
        if fields['opcode'] != Opcode.LL_SUBRATE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 10:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['subrate_factor'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['subrate_base_event'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['continuation_number'] = value_
        value_ = int.from_bytes(span[8:10], byteorder='little')
        fields['timeout'] = value_
        span = span[10:]
        return SubrateInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.subrate_factor > 65535:
            print(f"Invalid value for field SubrateInd::subrate_factor: {self.subrate_factor} > 65535; the value will be truncated")
            self.subrate_factor &= 65535
        _span.extend(int.to_bytes((self.subrate_factor << 0), length=2, byteorder='little'))
        if self.subrate_base_event > 65535:
            print(f"Invalid value for field SubrateInd::subrate_base_event: {self.subrate_base_event} > 65535; the value will be truncated")
            self.subrate_base_event &= 65535
        _span.extend(int.to_bytes((self.subrate_base_event << 0), length=2, byteorder='little'))
        if self.latency > 65535:
            print(f"Invalid value for field SubrateInd::latency: {self.latency} > 65535; the value will be truncated")
            self.latency &= 65535
        _span.extend(int.to_bytes((self.latency << 0), length=2, byteorder='little'))
        if self.continuation_number > 65535:
            print(f"Invalid value for field SubrateInd::continuation_number: {self.continuation_number} > 65535; the value will be truncated")
            self.continuation_number &= 65535
        _span.extend(int.to_bytes((self.continuation_number << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field SubrateInd::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 10

@dataclass
class ChannelReportingInd(LlcpPacket):
    enable: int = field(kw_only=True, default=0)
    min_spacing: int = field(kw_only=True, default=0)
    max_delay: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.LL_CHANNEL_REPORTING_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ChannelReportingInd', bytes]:
        if fields['opcode'] != Opcode.LL_CHANNEL_REPORTING_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['enable'] = span[0]
        fields['min_spacing'] = span[1]
        fields['max_delay'] = span[2]
        span = span[3:]
        return ChannelReportingInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.enable > 255:
            print(f"Invalid value for field ChannelReportingInd::enable: {self.enable} > 255; the value will be truncated")
            self.enable &= 255
        _span.append((self.enable << 0))
        if self.min_spacing > 255:
            print(f"Invalid value for field ChannelReportingInd::min_spacing: {self.min_spacing} > 255; the value will be truncated")
            self.min_spacing &= 255
        _span.append((self.min_spacing << 0))
        if self.max_delay > 255:
            print(f"Invalid value for field ChannelReportingInd::max_delay: {self.max_delay} > 255; the value will be truncated")
            self.max_delay &= 255
        _span.append((self.max_delay << 0))
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 3

@dataclass
class ChannelStatusInd(LlcpPacket):
    channel_classification: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.LL_CHANNEL_STATUS_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ChannelStatusInd', bytes]:
        if fields['opcode'] != Opcode.LL_CHANNEL_STATUS_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 10:
            raise Exception('Invalid packet size')
        fields['channel_classification'] = list(span[:10])
        span = span[10:]
        return ChannelStatusInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.channel_classification)
        return LlcpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 10
