# File generated from <stdin>, with the command:
#  ./third_party/pdl/pdl-compiler/scripts/generate_python_backend.py --custom-type-location ..bluetooth --output py/src/rootcanal/packets/ll.py
# /!\ Do not edit by hand.

from ..bluetooth import Address
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

if (not callable(getattr(Address, 'parse', None)) or
    not callable(getattr(Address, 'parse_all', None))):
    raise Exception('The custom field type Address does not implement the parse method')

class PacketType(enum.IntEnum):
    UNKNOWN = 0x0
    ACL = 0x1
    SCO = 0x2
    LE_CONNECTED_ISOCHRONOUS_PDU = 0x3
    LE_BROADCAST_ISOCHRONOUS_PDU = 0x4
    DISCONNECT = 0x5
    INQUIRY = 0x6
    INQUIRY_RESPONSE = 0x7
    LE_LEGACY_ADVERTISING_PDU = 0xb
    LE_EXTENDED_ADVERTISING_PDU = 0x37
    LE_PERIODIC_ADVERTISING_PDU = 0x40
    LE_CONNECT = 0xc
    LE_CONNECT_COMPLETE = 0xd
    LE_SCAN = 0xe
    LE_SCAN_RESPONSE = 0xf
    PAGE = 0x10
    PAGE_RESPONSE = 0x11
    PAGE_REJECT = 0x12
    READ_CLOCK_OFFSET = 0x13
    READ_CLOCK_OFFSET_RESPONSE = 0x14
    READ_REMOTE_SUPPORTED_FEATURES = 0x15
    READ_REMOTE_SUPPORTED_FEATURES_RESPONSE = 0x16
    READ_REMOTE_LMP_FEATURES = 0x17
    READ_REMOTE_LMP_FEATURES_RESPONSE = 0x18
    READ_REMOTE_EXTENDED_FEATURES = 0x19
    READ_REMOTE_EXTENDED_FEATURES_RESPONSE = 0x1a
    READ_REMOTE_VERSION_INFORMATION = 0x1b
    READ_REMOTE_VERSION_INFORMATION_RESPONSE = 0x1c
    REMOTE_NAME_REQUEST = 0x1d
    REMOTE_NAME_REQUEST_RESPONSE = 0x1e
    LE_ENCRYPT_CONNECTION = 0x20
    LE_ENCRYPT_CONNECTION_RESPONSE = 0x21
    LE_READ_REMOTE_FEATURES = 0x2c
    LE_READ_REMOTE_FEATURES_RESPONSE = 0x2d
    LE_CONNECTION_PARAMETER_REQUEST = 0x2e
    LE_CONNECTION_PARAMETER_UPDATE = 0x2f
    SCO_CONNECTION_REQUEST = 0x30
    SCO_CONNECTION_RESPONSE = 0x31
    SCO_DISCONNECT = 0x32
    LMP = 0x34
    LLCP = 0x41
    PING_REQUEST = 0x35
    PING_RESPONSE = 0x36
    ROLE_SWITCH_REQUEST = 0x38
    ROLE_SWITCH_RESPONSE = 0x39
    LL_PHY_REQ = 0x50
    LL_PHY_RSP = 0x51
    LL_PHY_UPDATE_IND = 0x52

@dataclass
class LinkLayerPacket(Packet):
    type: PacketType = field(kw_only=True, default=PacketType.UNKNOWN)
    source_address: Address = field(kw_only=True, default_factory=Address)
    destination_address: Address = field(kw_only=True, default_factory=Address)

    def __post_init__(self):
        pass

    @staticmethod
    def parse(span: bytes) -> Tuple['LinkLayerPacket', bytes]:
        fields = {'payload': None}
        if len(span) < 13:
            raise Exception('Invalid packet size')
        fields['type'] = PacketType(span[0])
        fields['source_address'] = Address.parse_all(span[1:7])
        fields['destination_address'] = Address.parse_all(span[7:13])
        span = span[13:]
        payload = span
        span = bytes([])
        fields['payload'] = payload
        try:
            return Acl.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeConnectedIsochronousPdu.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeBroadcastIsochronousPdu.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return Disconnect.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return Inquiry.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return BasicInquiryResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeLegacyAdvertisingPdu.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeExtendedAdvertisingPdu.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LePeriodicAdvertisingPdu.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeConnect.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeConnectComplete.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeScan.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeScanResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return Page.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PageResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PageReject.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadClockOffset.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadClockOffsetResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteSupportedFeatures.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteSupportedFeaturesResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteLmpFeatures.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteLmpFeaturesResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteExtendedFeatures.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteExtendedFeaturesResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteVersionInformation.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ReadRemoteVersionInformationResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return RemoteNameRequest.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return RemoteNameRequestResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeEncryptConnection.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeEncryptConnectionResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeReadRemoteFeatures.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeReadRemoteFeaturesResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeConnectionParameterRequest.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LeConnectionParameterUpdate.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ScoConnectionRequest.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ScoConnectionResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ScoDisconnect.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PingRequest.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PingResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return RoleSwitchRequest.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return RoleSwitchResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LlPhyReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LlPhyRsp.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return LlPhyUpdateInd.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        return LinkLayerPacket(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.type << 0))
        _span.extend(self.source_address.serialize())
        _span.extend(self.destination_address.serialize())
        _span.extend(payload or self.payload or [])
        return bytes(_span)

    @property
    def size(self) -> int:
        return len(self.payload) + 13

@dataclass
class Acl(LinkLayerPacket):
    packet_boundary_flag: int = field(kw_only=True, default=0)
    broadcast_flag: int = field(kw_only=True, default=0)
    data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.ACL

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Acl', bytes]:
        if fields['type'] != PacketType.ACL:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['packet_boundary_flag'] = span[0]
        fields['broadcast_flag'] = span[1]
        span = span[2:]
        fields['data'] = list(span)
        span = bytes()
        return Acl(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.packet_boundary_flag > 255:
            print(f"Invalid value for field Acl::packet_boundary_flag: {self.packet_boundary_flag} > 255; the value will be truncated")
            self.packet_boundary_flag &= 255
        _span.append((self.packet_boundary_flag << 0))
        if self.broadcast_flag > 255:
            print(f"Invalid value for field Acl::broadcast_flag: {self.broadcast_flag} > 255; the value will be truncated")
            self.broadcast_flag &= 255
        _span.append((self.broadcast_flag << 0))
        _span.extend(self.data)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.data) * 1 + 2

@dataclass
class Sco(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.SCO

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Sco', bytes]:
        if fields['type'] != PacketType.SCO:
            raise Exception("Invalid constraint field values")
        payload = span
        span = bytes([])
        fields['payload'] = payload
        return Sco(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(payload or self.payload or [])
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.payload)

@dataclass
class LeConnectedIsochronousPdu(LinkLayerPacket):
    cig_id: int = field(kw_only=True, default=0)
    cis_id: int = field(kw_only=True, default=0)
    sequence_number: int = field(kw_only=True, default=0)
    data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_CONNECTED_ISOCHRONOUS_PDU

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeConnectedIsochronousPdu', bytes]:
        if fields['type'] != PacketType.LE_CONNECTED_ISOCHRONOUS_PDU:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['cig_id'] = span[0]
        fields['cis_id'] = span[1]
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['sequence_number'] = value_
        span = span[4:]
        fields['data'] = list(span)
        span = bytes()
        return LeConnectedIsochronousPdu(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.cig_id > 255:
            print(f"Invalid value for field LeConnectedIsochronousPdu::cig_id: {self.cig_id} > 255; the value will be truncated")
            self.cig_id &= 255
        _span.append((self.cig_id << 0))
        if self.cis_id > 255:
            print(f"Invalid value for field LeConnectedIsochronousPdu::cis_id: {self.cis_id} > 255; the value will be truncated")
            self.cis_id &= 255
        _span.append((self.cis_id << 0))
        if self.sequence_number > 65535:
            print(f"Invalid value for field LeConnectedIsochronousPdu::sequence_number: {self.sequence_number} > 65535; the value will be truncated")
            self.sequence_number &= 65535
        _span.extend(int.to_bytes((self.sequence_number << 0), length=2, byteorder='little'))
        _span.extend(self.data)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.data) * 1 + 4

@dataclass
class LeBroadcastIsochronousPdu(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.LE_BROADCAST_ISOCHRONOUS_PDU

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeBroadcastIsochronousPdu', bytes]:
        if fields['type'] != PacketType.LE_BROADCAST_ISOCHRONOUS_PDU:
            raise Exception("Invalid constraint field values")
        return LeBroadcastIsochronousPdu(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class Disconnect(LinkLayerPacket):
    reason: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.DISCONNECT

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Disconnect', bytes]:
        if fields['type'] != PacketType.DISCONNECT:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['reason'] = span[0]
        span = span[1:]
        return Disconnect(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.reason > 255:
            print(f"Invalid value for field Disconnect::reason: {self.reason} > 255; the value will be truncated")
            self.reason &= 255
        _span.append((self.reason << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

class InquiryState(enum.IntEnum):
    STANDBY = 0x0
    INQUIRY = 0x1

class InquiryType(enum.IntEnum):
    STANDARD = 0x0
    RSSI = 0x1
    EXTENDED = 0x2

@dataclass
class Inquiry(LinkLayerPacket):
    inquiry_type: InquiryType = field(kw_only=True, default=InquiryType.STANDARD)
    lap: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.INQUIRY

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Inquiry', bytes]:
        if fields['type'] != PacketType.INQUIRY:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['inquiry_type'] = InquiryType(span[0])
        fields['lap'] = span[1]
        span = span[2:]
        return Inquiry(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.inquiry_type << 0))
        if self.lap > 255:
            print(f"Invalid value for field Inquiry::lap: {self.lap} > 255; the value will be truncated")
            self.lap &= 255
        _span.append((self.lap << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class BasicInquiryResponse(LinkLayerPacket):
    inquiry_type: InquiryType = field(kw_only=True, default=InquiryType.STANDARD)
    page_scan_repetition_mode: int = field(kw_only=True, default=0)
    class_of_device: int = field(kw_only=True, default=0)
    clock_offset: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.INQUIRY_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['BasicInquiryResponse', bytes]:
        if fields['type'] != PacketType.INQUIRY_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 7:
            raise Exception('Invalid packet size')
        fields['inquiry_type'] = InquiryType(span[0])
        fields['page_scan_repetition_mode'] = span[1]
        value_ = int.from_bytes(span[2:5], byteorder='little')
        fields['class_of_device'] = value_
        value_ = int.from_bytes(span[5:7], byteorder='little')
        fields['clock_offset'] = (value_ >> 0) & 0x7fff
        span = span[7:]
        payload = span
        span = bytes([])
        fields['payload'] = payload
        try:
            return InquiryResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return InquiryResponseWithRssi.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return ExtendedInquiryResponse.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        return BasicInquiryResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.inquiry_type << 0))
        if self.page_scan_repetition_mode > 255:
            print(f"Invalid value for field BasicInquiryResponse::page_scan_repetition_mode: {self.page_scan_repetition_mode} > 255; the value will be truncated")
            self.page_scan_repetition_mode &= 255
        _span.append((self.page_scan_repetition_mode << 0))
        if self.class_of_device > 16777215:
            print(f"Invalid value for field BasicInquiryResponse::class_of_device: {self.class_of_device} > 16777215; the value will be truncated")
            self.class_of_device &= 16777215
        _span.extend(int.to_bytes((self.class_of_device << 0), length=3, byteorder='little'))
        if self.clock_offset > 32767:
            print(f"Invalid value for field BasicInquiryResponse::clock_offset: {self.clock_offset} > 32767; the value will be truncated")
            self.clock_offset &= 32767
        _span.extend(int.to_bytes((self.clock_offset << 0), length=2, byteorder='little'))
        _span.extend(payload or self.payload or [])
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.payload) + 7

@dataclass
class InquiryResponse(BasicInquiryResponse):
    

    def __post_init__(self):
        self.inquiry_type = InquiryType.STANDARD
        self.type = PacketType.INQUIRY_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['InquiryResponse', bytes]:
        if fields['inquiry_type'] != InquiryType.STANDARD:
            raise Exception("Invalid constraint field values")
        return InquiryResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return BasicInquiryResponse.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class InquiryResponseWithRssi(BasicInquiryResponse):
    rssi: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.inquiry_type = InquiryType.RSSI
        self.type = PacketType.INQUIRY_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['InquiryResponseWithRssi', bytes]:
        if fields['inquiry_type'] != InquiryType.RSSI:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['rssi'] = span[0]
        span = span[1:]
        return InquiryResponseWithRssi(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.rssi > 255:
            print(f"Invalid value for field InquiryResponseWithRssi::rssi: {self.rssi} > 255; the value will be truncated")
            self.rssi &= 255
        _span.append((self.rssi << 0))
        return BasicInquiryResponse.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class ExtendedInquiryResponse(BasicInquiryResponse):
    rssi: int = field(kw_only=True, default=0)
    extended_inquiry_response: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.inquiry_type = InquiryType.EXTENDED
        self.type = PacketType.INQUIRY_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ExtendedInquiryResponse', bytes]:
        if fields['inquiry_type'] != InquiryType.EXTENDED:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['rssi'] = span[0]
        span = span[1:]
        if len(span) < 240:
            raise Exception('Invalid packet size')
        fields['extended_inquiry_response'] = list(span[:240])
        span = span[240:]
        return ExtendedInquiryResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.rssi > 255:
            print(f"Invalid value for field ExtendedInquiryResponse::rssi: {self.rssi} > 255; the value will be truncated")
            self.rssi &= 255
        _span.append((self.rssi << 0))
        _span.extend(self.extended_inquiry_response)
        return BasicInquiryResponse.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 241

class AddressType(enum.IntEnum):
    PUBLIC = 0x0
    RANDOM = 0x1
    PUBLIC_IDENTITY = 0x2
    RANDOM_IDENTITY = 0x3

class LegacyAdvertisingType(enum.IntEnum):
    ADV_IND = 0x0
    ADV_DIRECT_IND = 0x1
    ADV_SCAN_IND = 0x2
    ADV_NONCONN_IND = 0x3

@dataclass
class LeLegacyAdvertisingPdu(LinkLayerPacket):
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    target_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    advertising_type: LegacyAdvertisingType = field(kw_only=True, default=LegacyAdvertisingType.ADV_IND)
    advertising_data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_LEGACY_ADVERTISING_PDU

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeLegacyAdvertisingPdu', bytes]:
        if fields['type'] != PacketType.LE_LEGACY_ADVERTISING_PDU:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['advertising_address_type'] = AddressType(span[0])
        fields['target_address_type'] = AddressType(span[1])
        fields['advertising_type'] = LegacyAdvertisingType(span[2])
        span = span[3:]
        fields['advertising_data'] = list(span)
        span = bytes()
        return LeLegacyAdvertisingPdu(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.advertising_address_type << 0))
        _span.append((self.target_address_type << 0))
        _span.append((self.advertising_type << 0))
        _span.extend(self.advertising_data)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.advertising_data) * 1 + 3

class PrimaryPhyType(enum.IntEnum):
    LE_1M = 0x1
    LE_CODED = 0x3

class SecondaryPhyType(enum.IntEnum):
    NO_PACKETS = 0x0
    LE_1M = 0x1
    LE_2M = 0x2
    LE_CODED = 0x3

@dataclass
class LeExtendedAdvertisingPdu(LinkLayerPacket):
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    target_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    connectable: int = field(kw_only=True, default=0)
    scannable: int = field(kw_only=True, default=0)
    directed: int = field(kw_only=True, default=0)
    sid: int = field(kw_only=True, default=0)
    tx_power: int = field(kw_only=True, default=0)
    primary_phy: PrimaryPhyType = field(kw_only=True, default=PrimaryPhyType.LE_1M)
    secondary_phy: SecondaryPhyType = field(kw_only=True, default=SecondaryPhyType.NO_PACKETS)
    periodic_advertising_interval: int = field(kw_only=True, default=0)
    advertising_data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_EXTENDED_ADVERTISING_PDU

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeExtendedAdvertisingPdu', bytes]:
        if fields['type'] != PacketType.LE_EXTENDED_ADVERTISING_PDU:
            raise Exception("Invalid constraint field values")
        if len(span) < 9:
            raise Exception('Invalid packet size')
        fields['advertising_address_type'] = AddressType(span[0])
        fields['target_address_type'] = AddressType(span[1])
        fields['connectable'] = (span[2] >> 0) & 0x1
        fields['scannable'] = (span[2] >> 1) & 0x1
        fields['directed'] = (span[2] >> 2) & 0x1
        fields['sid'] = span[3]
        fields['tx_power'] = span[4]
        fields['primary_phy'] = PrimaryPhyType(span[5])
        fields['secondary_phy'] = SecondaryPhyType(span[6])
        value_ = int.from_bytes(span[7:9], byteorder='little')
        fields['periodic_advertising_interval'] = value_
        span = span[9:]
        fields['advertising_data'] = list(span)
        span = bytes()
        return LeExtendedAdvertisingPdu(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.advertising_address_type << 0))
        _span.append((self.target_address_type << 0))
        if self.connectable > 1:
            print(f"Invalid value for field LeExtendedAdvertisingPdu::connectable: {self.connectable} > 1; the value will be truncated")
            self.connectable &= 1
        if self.scannable > 1:
            print(f"Invalid value for field LeExtendedAdvertisingPdu::scannable: {self.scannable} > 1; the value will be truncated")
            self.scannable &= 1
        if self.directed > 1:
            print(f"Invalid value for field LeExtendedAdvertisingPdu::directed: {self.directed} > 1; the value will be truncated")
            self.directed &= 1
        _value = (
            (self.connectable << 0) |
            (self.scannable << 1) |
            (self.directed << 2)
        )
        _span.append(_value)
        if self.sid > 255:
            print(f"Invalid value for field LeExtendedAdvertisingPdu::sid: {self.sid} > 255; the value will be truncated")
            self.sid &= 255
        _span.append((self.sid << 0))
        if self.tx_power > 255:
            print(f"Invalid value for field LeExtendedAdvertisingPdu::tx_power: {self.tx_power} > 255; the value will be truncated")
            self.tx_power &= 255
        _span.append((self.tx_power << 0))
        _span.append((self.primary_phy << 0))
        _span.append((self.secondary_phy << 0))
        if self.periodic_advertising_interval > 65535:
            print(f"Invalid value for field LeExtendedAdvertisingPdu::periodic_advertising_interval: {self.periodic_advertising_interval} > 65535; the value will be truncated")
            self.periodic_advertising_interval &= 65535
        _span.extend(int.to_bytes((self.periodic_advertising_interval << 0), length=2, byteorder='little'))
        _span.extend(self.advertising_data)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.advertising_data) * 1 + 9

@dataclass
class LePeriodicAdvertisingPdu(LinkLayerPacket):
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    sid: int = field(kw_only=True, default=0)
    tx_power: int = field(kw_only=True, default=0)
    advertising_interval: int = field(kw_only=True, default=0)
    advertising_data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_PERIODIC_ADVERTISING_PDU

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LePeriodicAdvertisingPdu', bytes]:
        if fields['type'] != PacketType.LE_PERIODIC_ADVERTISING_PDU:
            raise Exception("Invalid constraint field values")
        if len(span) < 5:
            raise Exception('Invalid packet size')
        fields['advertising_address_type'] = AddressType(span[0])
        fields['sid'] = span[1]
        fields['tx_power'] = span[2]
        value_ = int.from_bytes(span[3:5], byteorder='little')
        fields['advertising_interval'] = value_
        span = span[5:]
        fields['advertising_data'] = list(span)
        span = bytes()
        return LePeriodicAdvertisingPdu(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.advertising_address_type << 0))
        if self.sid > 255:
            print(f"Invalid value for field LePeriodicAdvertisingPdu::sid: {self.sid} > 255; the value will be truncated")
            self.sid &= 255
        _span.append((self.sid << 0))
        if self.tx_power > 255:
            print(f"Invalid value for field LePeriodicAdvertisingPdu::tx_power: {self.tx_power} > 255; the value will be truncated")
            self.tx_power &= 255
        _span.append((self.tx_power << 0))
        if self.advertising_interval > 65535:
            print(f"Invalid value for field LePeriodicAdvertisingPdu::advertising_interval: {self.advertising_interval} > 65535; the value will be truncated")
            self.advertising_interval &= 65535
        _span.extend(int.to_bytes((self.advertising_interval << 0), length=2, byteorder='little'))
        _span.extend(self.advertising_data)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.advertising_data) * 1 + 5

@dataclass
class LeConnect(LinkLayerPacket):
    initiating_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    conn_interval: int = field(kw_only=True, default=0)
    conn_peripheral_latency: int = field(kw_only=True, default=0)
    conn_supervision_timeout: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LE_CONNECT

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeConnect', bytes]:
        if fields['type'] != PacketType.LE_CONNECT:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        fields['initiating_address_type'] = AddressType(span[0])
        fields['advertising_address_type'] = AddressType(span[1])
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['conn_interval'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['conn_peripheral_latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['conn_supervision_timeout'] = value_
        span = span[8:]
        return LeConnect(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.initiating_address_type << 0))
        _span.append((self.advertising_address_type << 0))
        if self.conn_interval > 65535:
            print(f"Invalid value for field LeConnect::conn_interval: {self.conn_interval} > 65535; the value will be truncated")
            self.conn_interval &= 65535
        _span.extend(int.to_bytes((self.conn_interval << 0), length=2, byteorder='little'))
        if self.conn_peripheral_latency > 65535:
            print(f"Invalid value for field LeConnect::conn_peripheral_latency: {self.conn_peripheral_latency} > 65535; the value will be truncated")
            self.conn_peripheral_latency &= 65535
        _span.extend(int.to_bytes((self.conn_peripheral_latency << 0), length=2, byteorder='little'))
        if self.conn_supervision_timeout > 65535:
            print(f"Invalid value for field LeConnect::conn_supervision_timeout: {self.conn_supervision_timeout} > 65535; the value will be truncated")
            self.conn_supervision_timeout &= 65535
        _span.extend(int.to_bytes((self.conn_supervision_timeout << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class LeConnectComplete(LinkLayerPacket):
    initiating_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    conn_interval: int = field(kw_only=True, default=0)
    conn_peripheral_latency: int = field(kw_only=True, default=0)
    conn_supervision_timeout: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LE_CONNECT_COMPLETE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeConnectComplete', bytes]:
        if fields['type'] != PacketType.LE_CONNECT_COMPLETE:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        fields['initiating_address_type'] = AddressType(span[0])
        fields['advertising_address_type'] = AddressType(span[1])
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['conn_interval'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['conn_peripheral_latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['conn_supervision_timeout'] = value_
        span = span[8:]
        return LeConnectComplete(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.initiating_address_type << 0))
        _span.append((self.advertising_address_type << 0))
        if self.conn_interval > 65535:
            print(f"Invalid value for field LeConnectComplete::conn_interval: {self.conn_interval} > 65535; the value will be truncated")
            self.conn_interval &= 65535
        _span.extend(int.to_bytes((self.conn_interval << 0), length=2, byteorder='little'))
        if self.conn_peripheral_latency > 65535:
            print(f"Invalid value for field LeConnectComplete::conn_peripheral_latency: {self.conn_peripheral_latency} > 65535; the value will be truncated")
            self.conn_peripheral_latency &= 65535
        _span.extend(int.to_bytes((self.conn_peripheral_latency << 0), length=2, byteorder='little'))
        if self.conn_supervision_timeout > 65535:
            print(f"Invalid value for field LeConnectComplete::conn_supervision_timeout: {self.conn_supervision_timeout} > 65535; the value will be truncated")
            self.conn_supervision_timeout &= 65535
        _span.extend(int.to_bytes((self.conn_supervision_timeout << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class LeScan(LinkLayerPacket):
    scanning_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)

    def __post_init__(self):
        self.type = PacketType.LE_SCAN

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeScan', bytes]:
        if fields['type'] != PacketType.LE_SCAN:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['scanning_address_type'] = AddressType(span[0])
        fields['advertising_address_type'] = AddressType(span[1])
        span = span[2:]
        return LeScan(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.scanning_address_type << 0))
        _span.append((self.advertising_address_type << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class LeScanResponse(LinkLayerPacket):
    advertising_address_type: AddressType = field(kw_only=True, default=AddressType.PUBLIC)
    scan_response_data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_SCAN_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeScanResponse', bytes]:
        if fields['type'] != PacketType.LE_SCAN_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['advertising_address_type'] = AddressType(span[0])
        span = span[1:]
        fields['scan_response_data'] = list(span)
        span = bytes()
        return LeScanResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.advertising_address_type << 0))
        _span.extend(self.scan_response_data)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.scan_response_data) * 1 + 1

@dataclass
class Page(LinkLayerPacket):
    class_of_device: int = field(kw_only=True, default=0)
    allow_role_switch: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.PAGE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Page', bytes]:
        if fields['type'] != PacketType.PAGE:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:3], byteorder='little')
        fields['class_of_device'] = value_
        fields['allow_role_switch'] = span[3]
        span = span[4:]
        return Page(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.class_of_device > 16777215:
            print(f"Invalid value for field Page::class_of_device: {self.class_of_device} > 16777215; the value will be truncated")
            self.class_of_device &= 16777215
        _span.extend(int.to_bytes((self.class_of_device << 0), length=3, byteorder='little'))
        if self.allow_role_switch > 255:
            print(f"Invalid value for field Page::allow_role_switch: {self.allow_role_switch} > 255; the value will be truncated")
            self.allow_role_switch &= 255
        _span.append((self.allow_role_switch << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4

@dataclass
class PageResponse(LinkLayerPacket):
    try_role_switch: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.PAGE_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PageResponse', bytes]:
        if fields['type'] != PacketType.PAGE_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['try_role_switch'] = span[0]
        span = span[1:]
        return PageResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.try_role_switch > 255:
            print(f"Invalid value for field PageResponse::try_role_switch: {self.try_role_switch} > 255; the value will be truncated")
            self.try_role_switch &= 255
        _span.append((self.try_role_switch << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class PageReject(LinkLayerPacket):
    reason: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.PAGE_REJECT

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PageReject', bytes]:
        if fields['type'] != PacketType.PAGE_REJECT:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['reason'] = span[0]
        span = span[1:]
        return PageReject(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.reason > 255:
            print(f"Invalid value for field PageReject::reason: {self.reason} > 255; the value will be truncated")
            self.reason &= 255
        _span.append((self.reason << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class ReadClockOffset(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.READ_CLOCK_OFFSET

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadClockOffset', bytes]:
        if fields['type'] != PacketType.READ_CLOCK_OFFSET:
            raise Exception("Invalid constraint field values")
        return ReadClockOffset(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class ReadClockOffsetResponse(LinkLayerPacket):
    offset: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.READ_CLOCK_OFFSET_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadClockOffsetResponse', bytes]:
        if fields['type'] != PacketType.READ_CLOCK_OFFSET_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['offset'] = value_
        span = span[2:]
        return ReadClockOffsetResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.offset > 65535:
            print(f"Invalid value for field ReadClockOffsetResponse::offset: {self.offset} > 65535; the value will be truncated")
            self.offset &= 65535
        _span.extend(int.to_bytes((self.offset << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class ReadRemoteSupportedFeatures(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_SUPPORTED_FEATURES

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteSupportedFeatures', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_SUPPORTED_FEATURES:
            raise Exception("Invalid constraint field values")
        return ReadRemoteSupportedFeatures(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class ReadRemoteSupportedFeaturesResponse(LinkLayerPacket):
    features: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_SUPPORTED_FEATURES_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteSupportedFeaturesResponse', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_SUPPORTED_FEATURES_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['features'] = value_
        span = span[8:]
        return ReadRemoteSupportedFeaturesResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.features > 18446744073709551615:
            print(f"Invalid value for field ReadRemoteSupportedFeaturesResponse::features: {self.features} > 18446744073709551615; the value will be truncated")
            self.features &= 18446744073709551615
        _span.extend(int.to_bytes((self.features << 0), length=8, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class ReadRemoteLmpFeatures(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_LMP_FEATURES

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteLmpFeatures', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_LMP_FEATURES:
            raise Exception("Invalid constraint field values")
        return ReadRemoteLmpFeatures(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class ReadRemoteLmpFeaturesResponse(LinkLayerPacket):
    features: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_LMP_FEATURES_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteLmpFeaturesResponse', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_LMP_FEATURES_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['features'] = value_
        span = span[8:]
        return ReadRemoteLmpFeaturesResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.features > 18446744073709551615:
            print(f"Invalid value for field ReadRemoteLmpFeaturesResponse::features: {self.features} > 18446744073709551615; the value will be truncated")
            self.features &= 18446744073709551615
        _span.extend(int.to_bytes((self.features << 0), length=8, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class ReadRemoteExtendedFeatures(LinkLayerPacket):
    page_number: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_EXTENDED_FEATURES

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteExtendedFeatures', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_EXTENDED_FEATURES:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['page_number'] = span[0]
        span = span[1:]
        return ReadRemoteExtendedFeatures(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.page_number > 255:
            print(f"Invalid value for field ReadRemoteExtendedFeatures::page_number: {self.page_number} > 255; the value will be truncated")
            self.page_number &= 255
        _span.append((self.page_number << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class ReadRemoteExtendedFeaturesResponse(LinkLayerPacket):
    status: int = field(kw_only=True, default=0)
    page_number: int = field(kw_only=True, default=0)
    max_page_number: int = field(kw_only=True, default=0)
    features: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_EXTENDED_FEATURES_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteExtendedFeaturesResponse', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_EXTENDED_FEATURES_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 11:
            raise Exception('Invalid packet size')
        fields['status'] = span[0]
        fields['page_number'] = span[1]
        fields['max_page_number'] = span[2]
        value_ = int.from_bytes(span[3:11], byteorder='little')
        fields['features'] = value_
        span = span[11:]
        return ReadRemoteExtendedFeaturesResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.status > 255:
            print(f"Invalid value for field ReadRemoteExtendedFeaturesResponse::status: {self.status} > 255; the value will be truncated")
            self.status &= 255
        _span.append((self.status << 0))
        if self.page_number > 255:
            print(f"Invalid value for field ReadRemoteExtendedFeaturesResponse::page_number: {self.page_number} > 255; the value will be truncated")
            self.page_number &= 255
        _span.append((self.page_number << 0))
        if self.max_page_number > 255:
            print(f"Invalid value for field ReadRemoteExtendedFeaturesResponse::max_page_number: {self.max_page_number} > 255; the value will be truncated")
            self.max_page_number &= 255
        _span.append((self.max_page_number << 0))
        if self.features > 18446744073709551615:
            print(f"Invalid value for field ReadRemoteExtendedFeaturesResponse::features: {self.features} > 18446744073709551615; the value will be truncated")
            self.features &= 18446744073709551615
        _span.extend(int.to_bytes((self.features << 0), length=8, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 11

@dataclass
class ReadRemoteVersionInformation(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_VERSION_INFORMATION

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteVersionInformation', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_VERSION_INFORMATION:
            raise Exception("Invalid constraint field values")
        return ReadRemoteVersionInformation(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class ReadRemoteVersionInformationResponse(LinkLayerPacket):
    lmp_version: int = field(kw_only=True, default=0)
    lmp_subversion: int = field(kw_only=True, default=0)
    manufacturer_name: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.READ_REMOTE_VERSION_INFORMATION_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ReadRemoteVersionInformationResponse', bytes]:
        if fields['type'] != PacketType.READ_REMOTE_VERSION_INFORMATION_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['lmp_version'] = span[0]
        fields['lmp_subversion'] = span[1]
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['manufacturer_name'] = value_
        span = span[4:]
        return ReadRemoteVersionInformationResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.lmp_version > 255:
            print(f"Invalid value for field ReadRemoteVersionInformationResponse::lmp_version: {self.lmp_version} > 255; the value will be truncated")
            self.lmp_version &= 255
        _span.append((self.lmp_version << 0))
        if self.lmp_subversion > 255:
            print(f"Invalid value for field ReadRemoteVersionInformationResponse::lmp_subversion: {self.lmp_subversion} > 255; the value will be truncated")
            self.lmp_subversion &= 255
        _span.append((self.lmp_subversion << 0))
        if self.manufacturer_name > 65535:
            print(f"Invalid value for field ReadRemoteVersionInformationResponse::manufacturer_name: {self.manufacturer_name} > 65535; the value will be truncated")
            self.manufacturer_name &= 65535
        _span.extend(int.to_bytes((self.manufacturer_name << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4

@dataclass
class RemoteNameRequest(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.REMOTE_NAME_REQUEST

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['RemoteNameRequest', bytes]:
        if fields['type'] != PacketType.REMOTE_NAME_REQUEST:
            raise Exception("Invalid constraint field values")
        return RemoteNameRequest(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class RemoteNameRequestResponse(LinkLayerPacket):
    name: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.REMOTE_NAME_REQUEST_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['RemoteNameRequestResponse', bytes]:
        if fields['type'] != PacketType.REMOTE_NAME_REQUEST_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 248:
            raise Exception('Invalid packet size')
        fields['name'] = list(span[:248])
        span = span[248:]
        return RemoteNameRequestResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.name)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 248

@dataclass
class LeEncryptConnection(LinkLayerPacket):
    rand: bytearray = field(kw_only=True, default_factory=bytearray)
    ediv: int = field(kw_only=True, default=0)
    ltk: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_ENCRYPT_CONNECTION

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeEncryptConnection', bytes]:
        if fields['type'] != PacketType.LE_ENCRYPT_CONNECTION:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        fields['rand'] = list(span[:8])
        span = span[8:]
        if len(span) < 2:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['ediv'] = value_
        span = span[2:]
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['ltk'] = list(span[:16])
        span = span[16:]
        return LeEncryptConnection(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.rand)
        if self.ediv > 65535:
            print(f"Invalid value for field LeEncryptConnection::ediv: {self.ediv} > 65535; the value will be truncated")
            self.ediv &= 65535
        _span.extend(int.to_bytes((self.ediv << 0), length=2, byteorder='little'))
        _span.extend(self.ltk)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 26

@dataclass
class LeEncryptConnectionResponse(LinkLayerPacket):
    rand: bytearray = field(kw_only=True, default_factory=bytearray)
    ediv: int = field(kw_only=True, default=0)
    ltk: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.type = PacketType.LE_ENCRYPT_CONNECTION_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeEncryptConnectionResponse', bytes]:
        if fields['type'] != PacketType.LE_ENCRYPT_CONNECTION_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        fields['rand'] = list(span[:8])
        span = span[8:]
        if len(span) < 2:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['ediv'] = value_
        span = span[2:]
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['ltk'] = list(span[:16])
        span = span[16:]
        return LeEncryptConnectionResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.rand)
        if self.ediv > 65535:
            print(f"Invalid value for field LeEncryptConnectionResponse::ediv: {self.ediv} > 65535; the value will be truncated")
            self.ediv &= 65535
        _span.extend(int.to_bytes((self.ediv << 0), length=2, byteorder='little'))
        _span.extend(self.ltk)
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 26

class PasskeyNotificationType(enum.IntEnum):
    ENTRY_STARTED = 0x0
    DIGIT_ENTERED = 0x1
    DIGIT_ERASED = 0x2
    CLEARED = 0x3
    ENTRY_COMPLETED = 0x4

@dataclass
class LeReadRemoteFeatures(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.LE_READ_REMOTE_FEATURES

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeReadRemoteFeatures', bytes]:
        if fields['type'] != PacketType.LE_READ_REMOTE_FEATURES:
            raise Exception("Invalid constraint field values")
        return LeReadRemoteFeatures(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class LeReadRemoteFeaturesResponse(LinkLayerPacket):
    features: int = field(kw_only=True, default=0)
    status: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LE_READ_REMOTE_FEATURES_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeReadRemoteFeaturesResponse', bytes]:
        if fields['type'] != PacketType.LE_READ_REMOTE_FEATURES_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 9:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:8], byteorder='little')
        fields['features'] = value_
        fields['status'] = span[8]
        span = span[9:]
        return LeReadRemoteFeaturesResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.features > 18446744073709551615:
            print(f"Invalid value for field LeReadRemoteFeaturesResponse::features: {self.features} > 18446744073709551615; the value will be truncated")
            self.features &= 18446744073709551615
        _span.extend(int.to_bytes((self.features << 0), length=8, byteorder='little'))
        if self.status > 255:
            print(f"Invalid value for field LeReadRemoteFeaturesResponse::status: {self.status} > 255; the value will be truncated")
            self.status &= 255
        _span.append((self.status << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 9

@dataclass
class LeConnectionParameterRequest(LinkLayerPacket):
    interval_min: int = field(kw_only=True, default=0)
    interval_max: int = field(kw_only=True, default=0)
    latency: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LE_CONNECTION_PARAMETER_REQUEST

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeConnectionParameterRequest', bytes]:
        if fields['type'] != PacketType.LE_CONNECTION_PARAMETER_REQUEST:
            raise Exception("Invalid constraint field values")
        if len(span) < 8:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:2], byteorder='little')
        fields['interval_min'] = value_
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['interval_max'] = value_
        value_ = int.from_bytes(span[4:6], byteorder='little')
        fields['latency'] = value_
        value_ = int.from_bytes(span[6:8], byteorder='little')
        fields['timeout'] = value_
        span = span[8:]
        return LeConnectionParameterRequest(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.interval_min > 65535:
            print(f"Invalid value for field LeConnectionParameterRequest::interval_min: {self.interval_min} > 65535; the value will be truncated")
            self.interval_min &= 65535
        _span.extend(int.to_bytes((self.interval_min << 0), length=2, byteorder='little'))
        if self.interval_max > 65535:
            print(f"Invalid value for field LeConnectionParameterRequest::interval_max: {self.interval_max} > 65535; the value will be truncated")
            self.interval_max &= 65535
        _span.extend(int.to_bytes((self.interval_max << 0), length=2, byteorder='little'))
        if self.latency > 65535:
            print(f"Invalid value for field LeConnectionParameterRequest::latency: {self.latency} > 65535; the value will be truncated")
            self.latency &= 65535
        _span.extend(int.to_bytes((self.latency << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field LeConnectionParameterRequest::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 8

@dataclass
class LeConnectionParameterUpdate(LinkLayerPacket):
    status: int = field(kw_only=True, default=0)
    interval: int = field(kw_only=True, default=0)
    latency: int = field(kw_only=True, default=0)
    timeout: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LE_CONNECTION_PARAMETER_UPDATE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LeConnectionParameterUpdate', bytes]:
        if fields['type'] != PacketType.LE_CONNECTION_PARAMETER_UPDATE:
            raise Exception("Invalid constraint field values")
        if len(span) < 7:
            raise Exception('Invalid packet size')
        fields['status'] = span[0]
        value_ = int.from_bytes(span[1:3], byteorder='little')
        fields['interval'] = value_
        value_ = int.from_bytes(span[3:5], byteorder='little')
        fields['latency'] = value_
        value_ = int.from_bytes(span[5:7], byteorder='little')
        fields['timeout'] = value_
        span = span[7:]
        return LeConnectionParameterUpdate(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.status > 255:
            print(f"Invalid value for field LeConnectionParameterUpdate::status: {self.status} > 255; the value will be truncated")
            self.status &= 255
        _span.append((self.status << 0))
        if self.interval > 65535:
            print(f"Invalid value for field LeConnectionParameterUpdate::interval: {self.interval} > 65535; the value will be truncated")
            self.interval &= 65535
        _span.extend(int.to_bytes((self.interval << 0), length=2, byteorder='little'))
        if self.latency > 65535:
            print(f"Invalid value for field LeConnectionParameterUpdate::latency: {self.latency} > 65535; the value will be truncated")
            self.latency &= 65535
        _span.extend(int.to_bytes((self.latency << 0), length=2, byteorder='little'))
        if self.timeout > 65535:
            print(f"Invalid value for field LeConnectionParameterUpdate::timeout: {self.timeout} > 65535; the value will be truncated")
            self.timeout &= 65535
        _span.extend(int.to_bytes((self.timeout << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 7

@dataclass
class ScoConnectionRequest(LinkLayerPacket):
    transmit_bandwidth: int = field(kw_only=True, default=0)
    receive_bandwidth: int = field(kw_only=True, default=0)
    max_latency: int = field(kw_only=True, default=0)
    voice_setting: int = field(kw_only=True, default=0)
    retransmission_effort: int = field(kw_only=True, default=0)
    packet_type: int = field(kw_only=True, default=0)
    class_of_device: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.SCO_CONNECTION_REQUEST

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ScoConnectionRequest', bytes]:
        if fields['type'] != PacketType.SCO_CONNECTION_REQUEST:
            raise Exception("Invalid constraint field values")
        if len(span) < 18:
            raise Exception('Invalid packet size')
        value_ = int.from_bytes(span[0:4], byteorder='little')
        fields['transmit_bandwidth'] = value_
        value_ = int.from_bytes(span[4:8], byteorder='little')
        fields['receive_bandwidth'] = value_
        value_ = int.from_bytes(span[8:10], byteorder='little')
        fields['max_latency'] = value_
        value_ = int.from_bytes(span[10:12], byteorder='little')
        fields['voice_setting'] = (value_ >> 0) & 0x3ff
        fields['retransmission_effort'] = span[12]
        value_ = int.from_bytes(span[13:15], byteorder='little')
        fields['packet_type'] = value_
        value_ = int.from_bytes(span[15:18], byteorder='little')
        fields['class_of_device'] = value_
        span = span[18:]
        return ScoConnectionRequest(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.transmit_bandwidth > 4294967295:
            print(f"Invalid value for field ScoConnectionRequest::transmit_bandwidth: {self.transmit_bandwidth} > 4294967295; the value will be truncated")
            self.transmit_bandwidth &= 4294967295
        _span.extend(int.to_bytes((self.transmit_bandwidth << 0), length=4, byteorder='little'))
        if self.receive_bandwidth > 4294967295:
            print(f"Invalid value for field ScoConnectionRequest::receive_bandwidth: {self.receive_bandwidth} > 4294967295; the value will be truncated")
            self.receive_bandwidth &= 4294967295
        _span.extend(int.to_bytes((self.receive_bandwidth << 0), length=4, byteorder='little'))
        if self.max_latency > 65535:
            print(f"Invalid value for field ScoConnectionRequest::max_latency: {self.max_latency} > 65535; the value will be truncated")
            self.max_latency &= 65535
        _span.extend(int.to_bytes((self.max_latency << 0), length=2, byteorder='little'))
        if self.voice_setting > 1023:
            print(f"Invalid value for field ScoConnectionRequest::voice_setting: {self.voice_setting} > 1023; the value will be truncated")
            self.voice_setting &= 1023
        _span.extend(int.to_bytes((self.voice_setting << 0), length=2, byteorder='little'))
        if self.retransmission_effort > 255:
            print(f"Invalid value for field ScoConnectionRequest::retransmission_effort: {self.retransmission_effort} > 255; the value will be truncated")
            self.retransmission_effort &= 255
        _span.append((self.retransmission_effort << 0))
        if self.packet_type > 65535:
            print(f"Invalid value for field ScoConnectionRequest::packet_type: {self.packet_type} > 65535; the value will be truncated")
            self.packet_type &= 65535
        _span.extend(int.to_bytes((self.packet_type << 0), length=2, byteorder='little'))
        if self.class_of_device > 16777215:
            print(f"Invalid value for field ScoConnectionRequest::class_of_device: {self.class_of_device} > 16777215; the value will be truncated")
            self.class_of_device &= 16777215
        _span.extend(int.to_bytes((self.class_of_device << 0), length=3, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 18

@dataclass
class ScoConnectionResponse(LinkLayerPacket):
    status: int = field(kw_only=True, default=0)
    transmission_interval: int = field(kw_only=True, default=0)
    retransmission_window: int = field(kw_only=True, default=0)
    rx_packet_length: int = field(kw_only=True, default=0)
    tx_packet_length: int = field(kw_only=True, default=0)
    air_mode: int = field(kw_only=True, default=0)
    extended: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.SCO_CONNECTION_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ScoConnectionResponse', bytes]:
        if fields['type'] != PacketType.SCO_CONNECTION_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 9:
            raise Exception('Invalid packet size')
        fields['status'] = span[0]
        fields['transmission_interval'] = span[1]
        fields['retransmission_window'] = span[2]
        value_ = int.from_bytes(span[3:5], byteorder='little')
        fields['rx_packet_length'] = value_
        value_ = int.from_bytes(span[5:7], byteorder='little')
        fields['tx_packet_length'] = value_
        fields['air_mode'] = span[7]
        fields['extended'] = (span[8] >> 0) & 0x1
        span = span[9:]
        return ScoConnectionResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.status > 255:
            print(f"Invalid value for field ScoConnectionResponse::status: {self.status} > 255; the value will be truncated")
            self.status &= 255
        _span.append((self.status << 0))
        if self.transmission_interval > 255:
            print(f"Invalid value for field ScoConnectionResponse::transmission_interval: {self.transmission_interval} > 255; the value will be truncated")
            self.transmission_interval &= 255
        _span.append((self.transmission_interval << 0))
        if self.retransmission_window > 255:
            print(f"Invalid value for field ScoConnectionResponse::retransmission_window: {self.retransmission_window} > 255; the value will be truncated")
            self.retransmission_window &= 255
        _span.append((self.retransmission_window << 0))
        if self.rx_packet_length > 65535:
            print(f"Invalid value for field ScoConnectionResponse::rx_packet_length: {self.rx_packet_length} > 65535; the value will be truncated")
            self.rx_packet_length &= 65535
        _span.extend(int.to_bytes((self.rx_packet_length << 0), length=2, byteorder='little'))
        if self.tx_packet_length > 65535:
            print(f"Invalid value for field ScoConnectionResponse::tx_packet_length: {self.tx_packet_length} > 65535; the value will be truncated")
            self.tx_packet_length &= 65535
        _span.extend(int.to_bytes((self.tx_packet_length << 0), length=2, byteorder='little'))
        if self.air_mode > 255:
            print(f"Invalid value for field ScoConnectionResponse::air_mode: {self.air_mode} > 255; the value will be truncated")
            self.air_mode &= 255
        _span.append((self.air_mode << 0))
        if self.extended > 1:
            print(f"Invalid value for field ScoConnectionResponse::extended: {self.extended} > 1; the value will be truncated")
            self.extended &= 1
        _span.append((self.extended << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 9

@dataclass
class ScoDisconnect(LinkLayerPacket):
    reason: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.SCO_DISCONNECT

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ScoDisconnect', bytes]:
        if fields['type'] != PacketType.SCO_DISCONNECT:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['reason'] = span[0]
        span = span[1:]
        return ScoDisconnect(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.reason > 255:
            print(f"Invalid value for field ScoDisconnect::reason: {self.reason} > 255; the value will be truncated")
            self.reason &= 255
        _span.append((self.reason << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class Lmp(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.LMP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Lmp', bytes]:
        if fields['type'] != PacketType.LMP:
            raise Exception("Invalid constraint field values")
        payload = span
        span = bytes([])
        fields['payload'] = payload
        return Lmp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(payload or self.payload or [])
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.payload)

@dataclass
class Llcp(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.LLCP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Llcp', bytes]:
        if fields['type'] != PacketType.LLCP:
            raise Exception("Invalid constraint field values")
        payload = span
        span = bytes([])
        fields['payload'] = payload
        return Llcp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(payload or self.payload or [])
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.payload)

@dataclass
class PingRequest(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.PING_REQUEST

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PingRequest', bytes]:
        if fields['type'] != PacketType.PING_REQUEST:
            raise Exception("Invalid constraint field values")
        return PingRequest(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class PingResponse(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.PING_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PingResponse', bytes]:
        if fields['type'] != PacketType.PING_RESPONSE:
            raise Exception("Invalid constraint field values")
        return PingResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class RoleSwitchRequest(LinkLayerPacket):
    

    def __post_init__(self):
        self.type = PacketType.ROLE_SWITCH_REQUEST

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['RoleSwitchRequest', bytes]:
        if fields['type'] != PacketType.ROLE_SWITCH_REQUEST:
            raise Exception("Invalid constraint field values")
        return RoleSwitchRequest(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class RoleSwitchResponse(LinkLayerPacket):
    status: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.ROLE_SWITCH_RESPONSE

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['RoleSwitchResponse', bytes]:
        if fields['type'] != PacketType.ROLE_SWITCH_RESPONSE:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['status'] = span[0]
        span = span[1:]
        return RoleSwitchResponse(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.status > 255:
            print(f"Invalid value for field RoleSwitchResponse::status: {self.status} > 255; the value will be truncated")
            self.status &= 255
        _span.append((self.status << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class LlPhyReq(LinkLayerPacket):
    tx_phys: int = field(kw_only=True, default=0)
    rx_phys: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LL_PHY_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LlPhyReq', bytes]:
        if fields['type'] != PacketType.LL_PHY_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['tx_phys'] = span[0]
        fields['rx_phys'] = span[1]
        span = span[2:]
        return LlPhyReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.tx_phys > 255:
            print(f"Invalid value for field LlPhyReq::tx_phys: {self.tx_phys} > 255; the value will be truncated")
            self.tx_phys &= 255
        _span.append((self.tx_phys << 0))
        if self.rx_phys > 255:
            print(f"Invalid value for field LlPhyReq::rx_phys: {self.rx_phys} > 255; the value will be truncated")
            self.rx_phys &= 255
        _span.append((self.rx_phys << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class LlPhyRsp(LinkLayerPacket):
    tx_phys: int = field(kw_only=True, default=0)
    rx_phys: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LL_PHY_RSP

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LlPhyRsp', bytes]:
        if fields['type'] != PacketType.LL_PHY_RSP:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['tx_phys'] = span[0]
        fields['rx_phys'] = span[1]
        span = span[2:]
        return LlPhyRsp(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.tx_phys > 255:
            print(f"Invalid value for field LlPhyRsp::tx_phys: {self.tx_phys} > 255; the value will be truncated")
            self.tx_phys &= 255
        _span.append((self.tx_phys << 0))
        if self.rx_phys > 255:
            print(f"Invalid value for field LlPhyRsp::rx_phys: {self.rx_phys} > 255; the value will be truncated")
            self.rx_phys &= 255
        _span.append((self.rx_phys << 0))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class LlPhyUpdateInd(LinkLayerPacket):
    phy_c_to_p: int = field(kw_only=True, default=0)
    phy_p_to_c: int = field(kw_only=True, default=0)
    instant: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.type = PacketType.LL_PHY_UPDATE_IND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['LlPhyUpdateInd', bytes]:
        if fields['type'] != PacketType.LL_PHY_UPDATE_IND:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['phy_c_to_p'] = span[0]
        fields['phy_p_to_c'] = span[1]
        value_ = int.from_bytes(span[2:4], byteorder='little')
        fields['instant'] = value_
        span = span[4:]
        return LlPhyUpdateInd(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.phy_c_to_p > 255:
            print(f"Invalid value for field LlPhyUpdateInd::phy_c_to_p: {self.phy_c_to_p} > 255; the value will be truncated")
            self.phy_c_to_p &= 255
        _span.append((self.phy_c_to_p << 0))
        if self.phy_p_to_c > 255:
            print(f"Invalid value for field LlPhyUpdateInd::phy_p_to_c: {self.phy_p_to_c} > 255; the value will be truncated")
            self.phy_p_to_c &= 255
        _span.append((self.phy_p_to_c << 0))
        if self.instant > 65535:
            print(f"Invalid value for field LlPhyUpdateInd::instant: {self.instant} > 65535; the value will be truncated")
            self.instant &= 65535
        _span.extend(int.to_bytes((self.instant << 0), length=2, byteorder='little'))
        return LinkLayerPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4
