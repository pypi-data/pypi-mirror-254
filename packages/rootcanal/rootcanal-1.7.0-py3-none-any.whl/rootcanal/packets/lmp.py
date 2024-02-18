# File generated from <stdin>, with the command:
#  ./third_party/pdl/pdl-compiler/scripts/generate_python_backend.py --output py/src/rootcanal/packets/lmp.py
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
    NAME_REQ = 0x1
    NAME_RES = 0x2
    ACCEPTED = 0x3
    NOT_ACCEPTED = 0x4
    CLK_OFFSET_REQ = 0x5
    CLK_OFFSET_RES = 0x6
    DETACH = 0x7
    IN_RAND = 0x8
    COMB_KEY = 0x9
    UNIT_KEY = 0xa
    AU_RAND = 0xb
    SRES = 0xc
    TEMP_RAND = 0xd
    TEMP_KEY = 0xe
    ENCRYPTION_MODE_REQ = 0xf
    ENCRYPTION_KEY_SIZE_REQ = 0x10
    START_ENCRYPTION_REQ = 0x11
    STOP_ENCRYPTION_REQ = 0x12
    SWITCH_REQ = 0x13
    HOLD = 0x14
    HOLD_REQ = 0x15
    SNIFF_REQ = 0x17
    UNSNIFF_REQ = 0x18
    INCR_POWER_REQ = 0x1f
    DECR_POWER_REQ = 0x20
    MAX_POWER = 0x21
    MIN_POWER = 0x22
    AUTO_RATE = 0x23
    PREFERRED_RATE = 0x24
    VERSION_REQ = 0x25
    VERSION_RES = 0x26
    FEATURES_REQ = 0x27
    FEATURES_RES = 0x28
    QUALITY_OF_SERVICE = 0x29
    QUALITY_OF_SERVICE_REQ = 0x2a
    SCO_LINK_REQ = 0x2b
    REMOVE_SCO_LINK_REQ = 0x2c
    MAX_SLOT = 0x2d
    MAX_SLOT_REQ = 0x2e
    TIMING_ACCURACY_REQ = 0x2f
    TIMING_ACCURACY_RES = 0x30
    SETYP_COMPLETE = 0x31
    USE_SEMI_PERMANENT_KEY = 0x32
    HOST_CONNECTION_REQ = 0x33
    SLOT_OFFSET = 0x34
    PAGE_MODE_REQ = 0x35
    PAGE_SCAN_MODE_REQ = 0x36
    SUPERVISION_TIMEOUT = 0x37
    TEST_ACTIVATE = 0x38
    TEST_CONTROL = 0x39
    ENCRYPTION_KEY_SIZE_MASK_REQ = 0x3a
    ENCRYPTION_KEY_SIZE_MASK_RES = 0x3b
    SET_AFH = 0x3c
    ENCAPSULATED_HEADER = 0x3d
    ENCAPSULATED_PAYLOAD = 0x3e
    SIMPLE_PAIRING_CONFIRM = 0x3f
    SIMPLE_PAIRING_NUMBER = 0x40
    DHKEY_CHECK = 0x41
    PAUSE_ENCRYPTION_AES_REQ = 0x42
    ESCAPED = 0x7f

class ExtendedOpcode(enum.IntEnum):
    ACCEPTED = 0x1
    NOT_ACCEPTED = 0x2
    FEATURES_REQ = 0x3
    FEATURES_RES = 0x4
    CLK_ADJ = 0x5
    CLK_ADJ_ACK = 0x6
    CLK_ADJ_REQ = 0x7
    PACKET_TYPE_TABLE_REQ = 0xb
    ESCO_LINK_REQ = 0xc
    REMOVE_ESCO_LINK_REQ = 0xd
    CHANNEL_CLASSIFICATION_REQ = 0x10
    CHANNEL_CLASSIFICATION = 0x11
    SNIFF_SUBRATING_REQ = 0x15
    SNIFF_SUBRATING_RES = 0x16
    PAUSE_ENCRYPTION_REQ = 0x17
    RESUME_ENCRYPTION_REQ = 0x18
    IO_CAPABILITY_REQ = 0x19
    IO_CAPABILITY_RES = 0x1a
    NUMERIC_COMPARISON_FAILED = 0x1b
    PASSKEY_FAILED = 0x1c
    OOB_FAILED = 0x1d
    KEYPRESS_NOTIFICATION = 0x1e
    POWER_CONTROL_REQ = 0x1f
    POWER_CONTROL_RES = 0x20
    PING_REQ = 0x21
    PING_RES = 0x22
    SAM_SET_TYPE0 = 0x23
    SAM_DEFINE_MAP = 0x24
    SAM_SWITCH = 0x25

@dataclass
class LmpPacket(Packet):
    transaction_id: int = field(kw_only=True, default=0)
    opcode: Opcode = field(kw_only=True, default=Opcode.NAME_REQ)

    def __post_init__(self):
        pass

    @staticmethod
    def parse(span: bytes) -> Tuple['LmpPacket', bytes]:
        fields = {'payload': None}
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['transaction_id'] = (span[0] >> 0) & 0x1
        fields['opcode'] = Opcode((span[0] >> 1) & 0x7f)
        span = span[1:]
        payload = span
        span = bytes([])
        fields['payload'] = payload
        try:
            return ExtendedPacket.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return Accepted.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return NotAccepted.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return EncapsulatedHeader.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return EncapsulatedPayload.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return SimplePairingConfirm.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return SimplePairingNumber.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return DhkeyCheck.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return AuRand.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return Sres.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return InRand.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return CombKey.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return EncryptionModeReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return EncryptionKeySizeReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return StartEncryptionReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return StopEncryptionReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        return LmpPacket(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.transaction_id > 1:
            print(f"Invalid value for field LmpPacket::transaction_id: {self.transaction_id} > 1; the value will be truncated")
            self.transaction_id &= 1
        _value = (
            (self.transaction_id << 0) |
            (self.opcode << 1)
        )
        _span.append(_value)
        _span.extend(payload or self.payload or [])
        return bytes(_span)

    @property
    def size(self) -> int:
        return len(self.payload) + 1

@dataclass
class ExtendedPacket(LmpPacket):
    extended_opcode: ExtendedOpcode = field(kw_only=True, default=ExtendedOpcode.ACCEPTED)

    def __post_init__(self):
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['ExtendedPacket', bytes]:
        if fields['opcode'] != Opcode.ESCAPED:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['extended_opcode'] = ExtendedOpcode(span[0])
        span = span[1:]
        payload = span
        span = bytes([])
        fields['payload'] = payload
        try:
            return AcceptedExt.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return NotAcceptedExt.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return IoCapabilityReq.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return IoCapabilityRes.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return NumericComparisonFailed.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return PasskeyFailed.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return KeypressNotification.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return FeaturesReqExt.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        try:
            return FeaturesResExt.parse(fields.copy(), payload)
        except Exception as exn:
            pass
        return ExtendedPacket(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.extended_opcode << 0))
        _span.extend(payload or self.payload or [])
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return len(self.payload) + 1

@dataclass
class Accepted(LmpPacket):
    accepted_opcode: Opcode = field(kw_only=True, default=Opcode.NAME_REQ)

    def __post_init__(self):
        self.opcode = Opcode.ACCEPTED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Accepted', bytes]:
        if fields['opcode'] != Opcode.ACCEPTED:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['accepted_opcode'] = Opcode((span[0] >> 0) & 0x7f)
        if (span[0] >> 7) & 0x1 != 0x0:
            raise Exception('Unexpected fixed field value')
        span = span[1:]
        return Accepted(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _value = (
            (self.accepted_opcode << 0) |
            (0 << 7)
        )
        _span.append(_value)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class NotAccepted(LmpPacket):
    not_accepted_opcode: Opcode = field(kw_only=True, default=Opcode.NAME_REQ)
    error_code: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.NOT_ACCEPTED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['NotAccepted', bytes]:
        if fields['opcode'] != Opcode.NOT_ACCEPTED:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['not_accepted_opcode'] = Opcode((span[0] >> 0) & 0x7f)
        if (span[0] >> 7) & 0x1 != 0x0:
            raise Exception('Unexpected fixed field value')
        fields['error_code'] = span[1]
        span = span[2:]
        return NotAccepted(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _value = (
            (self.not_accepted_opcode << 0) |
            (0 << 7)
        )
        _span.append(_value)
        if self.error_code > 255:
            print(f"Invalid value for field NotAccepted::error_code: {self.error_code} > 255; the value will be truncated")
            self.error_code &= 255
        _span.append((self.error_code << 0))
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class AcceptedExt(ExtendedPacket):
    accepted_opcode: ExtendedOpcode = field(kw_only=True, default=ExtendedOpcode.ACCEPTED)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.ACCEPTED
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['AcceptedExt', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.ACCEPTED:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['accepted_opcode'] = ExtendedOpcode(span[0])
        span = span[1:]
        return AcceptedExt(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.accepted_opcode << 0))
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class NotAcceptedExt(ExtendedPacket):
    not_accepted_opcode: ExtendedOpcode = field(kw_only=True, default=ExtendedOpcode.ACCEPTED)
    error_code: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.NOT_ACCEPTED
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['NotAcceptedExt', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.NOT_ACCEPTED:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['not_accepted_opcode'] = ExtendedOpcode(span[0])
        fields['error_code'] = span[1]
        span = span[2:]
        return NotAcceptedExt(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.append((self.not_accepted_opcode << 0))
        if self.error_code > 255:
            print(f"Invalid value for field NotAcceptedExt::error_code: {self.error_code} > 255; the value will be truncated")
            self.error_code &= 255
        _span.append((self.error_code << 0))
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 2

@dataclass
class IoCapabilityReq(ExtendedPacket):
    io_capabilities: int = field(kw_only=True, default=0)
    oob_authentication_data: int = field(kw_only=True, default=0)
    authentication_requirement: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.IO_CAPABILITY_REQ
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['IoCapabilityReq', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.IO_CAPABILITY_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['io_capabilities'] = span[0]
        fields['oob_authentication_data'] = span[1]
        fields['authentication_requirement'] = span[2]
        span = span[3:]
        return IoCapabilityReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.io_capabilities > 255:
            print(f"Invalid value for field IoCapabilityReq::io_capabilities: {self.io_capabilities} > 255; the value will be truncated")
            self.io_capabilities &= 255
        _span.append((self.io_capabilities << 0))
        if self.oob_authentication_data > 255:
            print(f"Invalid value for field IoCapabilityReq::oob_authentication_data: {self.oob_authentication_data} > 255; the value will be truncated")
            self.oob_authentication_data &= 255
        _span.append((self.oob_authentication_data << 0))
        if self.authentication_requirement > 255:
            print(f"Invalid value for field IoCapabilityReq::authentication_requirement: {self.authentication_requirement} > 255; the value will be truncated")
            self.authentication_requirement &= 255
        _span.append((self.authentication_requirement << 0))
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 3

@dataclass
class IoCapabilityRes(ExtendedPacket):
    io_capabilities: int = field(kw_only=True, default=0)
    oob_authentication_data: int = field(kw_only=True, default=0)
    authentication_requirement: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.IO_CAPABILITY_RES
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['IoCapabilityRes', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.IO_CAPABILITY_RES:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['io_capabilities'] = span[0]
        fields['oob_authentication_data'] = span[1]
        fields['authentication_requirement'] = span[2]
        span = span[3:]
        return IoCapabilityRes(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.io_capabilities > 255:
            print(f"Invalid value for field IoCapabilityRes::io_capabilities: {self.io_capabilities} > 255; the value will be truncated")
            self.io_capabilities &= 255
        _span.append((self.io_capabilities << 0))
        if self.oob_authentication_data > 255:
            print(f"Invalid value for field IoCapabilityRes::oob_authentication_data: {self.oob_authentication_data} > 255; the value will be truncated")
            self.oob_authentication_data &= 255
        _span.append((self.oob_authentication_data << 0))
        if self.authentication_requirement > 255:
            print(f"Invalid value for field IoCapabilityRes::authentication_requirement: {self.authentication_requirement} > 255; the value will be truncated")
            self.authentication_requirement &= 255
        _span.append((self.authentication_requirement << 0))
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 3

@dataclass
class EncapsulatedHeader(LmpPacket):
    major_type: int = field(kw_only=True, default=0)
    minor_type: int = field(kw_only=True, default=0)
    payload_length: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.ENCAPSULATED_HEADER

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['EncapsulatedHeader', bytes]:
        if fields['opcode'] != Opcode.ENCAPSULATED_HEADER:
            raise Exception("Invalid constraint field values")
        if len(span) < 3:
            raise Exception('Invalid packet size')
        fields['major_type'] = span[0]
        fields['minor_type'] = span[1]
        fields['payload_length'] = span[2]
        span = span[3:]
        return EncapsulatedHeader(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.major_type > 255:
            print(f"Invalid value for field EncapsulatedHeader::major_type: {self.major_type} > 255; the value will be truncated")
            self.major_type &= 255
        _span.append((self.major_type << 0))
        if self.minor_type > 255:
            print(f"Invalid value for field EncapsulatedHeader::minor_type: {self.minor_type} > 255; the value will be truncated")
            self.minor_type &= 255
        _span.append((self.minor_type << 0))
        if self.payload_length > 255:
            print(f"Invalid value for field EncapsulatedHeader::payload_length: {self.payload_length} > 255; the value will be truncated")
            self.payload_length &= 255
        _span.append((self.payload_length << 0))
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 3

@dataclass
class EncapsulatedPayload(LmpPacket):
    data: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.ENCAPSULATED_PAYLOAD

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['EncapsulatedPayload', bytes]:
        if fields['opcode'] != Opcode.ENCAPSULATED_PAYLOAD:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['data'] = list(span[:16])
        span = span[16:]
        return EncapsulatedPayload(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.data)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class SimplePairingConfirm(LmpPacket):
    commitment_value: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.SIMPLE_PAIRING_CONFIRM

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['SimplePairingConfirm', bytes]:
        if fields['opcode'] != Opcode.SIMPLE_PAIRING_CONFIRM:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['commitment_value'] = list(span[:16])
        span = span[16:]
        return SimplePairingConfirm(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.commitment_value)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class SimplePairingNumber(LmpPacket):
    nonce: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.SIMPLE_PAIRING_NUMBER

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['SimplePairingNumber', bytes]:
        if fields['opcode'] != Opcode.SIMPLE_PAIRING_NUMBER:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['nonce'] = list(span[:16])
        span = span[16:]
        return SimplePairingNumber(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.nonce)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class DhkeyCheck(LmpPacket):
    confirmation_value: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.DHKEY_CHECK

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['DhkeyCheck', bytes]:
        if fields['opcode'] != Opcode.DHKEY_CHECK:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['confirmation_value'] = list(span[:16])
        span = span[16:]
        return DhkeyCheck(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.confirmation_value)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class AuRand(LmpPacket):
    random_number: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.AU_RAND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['AuRand', bytes]:
        if fields['opcode'] != Opcode.AU_RAND:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['random_number'] = list(span[:16])
        span = span[16:]
        return AuRand(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.random_number)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class Sres(LmpPacket):
    authentication_rsp: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.SRES

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['Sres', bytes]:
        if fields['opcode'] != Opcode.SRES:
            raise Exception("Invalid constraint field values")
        if len(span) < 4:
            raise Exception('Invalid packet size')
        fields['authentication_rsp'] = list(span[:4])
        span = span[4:]
        return Sres(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.authentication_rsp)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 4

@dataclass
class NumericComparisonFailed(ExtendedPacket):
    

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.NUMERIC_COMPARISON_FAILED
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['NumericComparisonFailed', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.NUMERIC_COMPARISON_FAILED:
            raise Exception("Invalid constraint field values")
        return NumericComparisonFailed(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class PasskeyFailed(ExtendedPacket):
    

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.PASSKEY_FAILED
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['PasskeyFailed', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.PASSKEY_FAILED:
            raise Exception("Invalid constraint field values")
        return PasskeyFailed(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class KeypressNotification(ExtendedPacket):
    notification_type: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.KEYPRESS_NOTIFICATION
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['KeypressNotification', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.KEYPRESS_NOTIFICATION:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['notification_type'] = span[0]
        span = span[1:]
        return KeypressNotification(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.notification_type > 255:
            print(f"Invalid value for field KeypressNotification::notification_type: {self.notification_type} > 255; the value will be truncated")
            self.notification_type &= 255
        _span.append((self.notification_type << 0))
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class InRand(LmpPacket):
    random_number: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.IN_RAND

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['InRand', bytes]:
        if fields['opcode'] != Opcode.IN_RAND:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['random_number'] = list(span[:16])
        span = span[16:]
        return InRand(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.random_number)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class CombKey(LmpPacket):
    random_number: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.COMB_KEY

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['CombKey', bytes]:
        if fields['opcode'] != Opcode.COMB_KEY:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['random_number'] = list(span[:16])
        span = span[16:]
        return CombKey(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.random_number)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class EncryptionModeReq(LmpPacket):
    encryption_mode: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.ENCRYPTION_MODE_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['EncryptionModeReq', bytes]:
        if fields['opcode'] != Opcode.ENCRYPTION_MODE_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['encryption_mode'] = span[0]
        span = span[1:]
        return EncryptionModeReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.encryption_mode > 255:
            print(f"Invalid value for field EncryptionModeReq::encryption_mode: {self.encryption_mode} > 255; the value will be truncated")
            self.encryption_mode &= 255
        _span.append((self.encryption_mode << 0))
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class EncryptionKeySizeReq(LmpPacket):
    key_size: int = field(kw_only=True, default=0)

    def __post_init__(self):
        self.opcode = Opcode.ENCRYPTION_KEY_SIZE_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['EncryptionKeySizeReq', bytes]:
        if fields['opcode'] != Opcode.ENCRYPTION_KEY_SIZE_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 1:
            raise Exception('Invalid packet size')
        fields['key_size'] = span[0]
        span = span[1:]
        return EncryptionKeySizeReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.key_size > 255:
            print(f"Invalid value for field EncryptionKeySizeReq::key_size: {self.key_size} > 255; the value will be truncated")
            self.key_size &= 255
        _span.append((self.key_size << 0))
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 1

@dataclass
class StartEncryptionReq(LmpPacket):
    random_number: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.opcode = Opcode.START_ENCRYPTION_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['StartEncryptionReq', bytes]:
        if fields['opcode'] != Opcode.START_ENCRYPTION_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 16:
            raise Exception('Invalid packet size')
        fields['random_number'] = list(span[:16])
        span = span[16:]
        return StartEncryptionReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        _span.extend(self.random_number)
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 16

@dataclass
class StopEncryptionReq(LmpPacket):
    

    def __post_init__(self):
        self.opcode = Opcode.STOP_ENCRYPTION_REQ

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['StopEncryptionReq', bytes]:
        if fields['opcode'] != Opcode.STOP_ENCRYPTION_REQ:
            raise Exception("Invalid constraint field values")
        return StopEncryptionReq(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        return LmpPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 0

@dataclass
class FeaturesReqExt(ExtendedPacket):
    features_page: int = field(kw_only=True, default=0)
    max_supported_page: int = field(kw_only=True, default=0)
    extended_features: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.FEATURES_REQ
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['FeaturesReqExt', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.FEATURES_REQ:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['features_page'] = span[0]
        fields['max_supported_page'] = span[1]
        span = span[2:]
        if len(span) < 8:
            raise Exception('Invalid packet size')
        fields['extended_features'] = list(span[:8])
        span = span[8:]
        return FeaturesReqExt(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.features_page > 255:
            print(f"Invalid value for field FeaturesReqExt::features_page: {self.features_page} > 255; the value will be truncated")
            self.features_page &= 255
        _span.append((self.features_page << 0))
        if self.max_supported_page > 255:
            print(f"Invalid value for field FeaturesReqExt::max_supported_page: {self.max_supported_page} > 255; the value will be truncated")
            self.max_supported_page &= 255
        _span.append((self.max_supported_page << 0))
        _span.extend(self.extended_features)
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 10

@dataclass
class FeaturesResExt(ExtendedPacket):
    features_page: int = field(kw_only=True, default=0)
    max_supported_page: int = field(kw_only=True, default=0)
    extended_features: bytearray = field(kw_only=True, default_factory=bytearray)

    def __post_init__(self):
        self.extended_opcode = ExtendedOpcode.FEATURES_RES
        self.opcode = Opcode.ESCAPED

    @staticmethod
    def parse(fields: dict, span: bytes) -> Tuple['FeaturesResExt', bytes]:
        if fields['extended_opcode'] != ExtendedOpcode.FEATURES_RES:
            raise Exception("Invalid constraint field values")
        if len(span) < 2:
            raise Exception('Invalid packet size')
        fields['features_page'] = span[0]
        fields['max_supported_page'] = span[1]
        span = span[2:]
        if len(span) < 8:
            raise Exception('Invalid packet size')
        fields['extended_features'] = list(span[:8])
        span = span[8:]
        return FeaturesResExt(**fields), span

    def serialize(self, payload: bytes = None) -> bytes:
        _span = bytearray()
        if self.features_page > 255:
            print(f"Invalid value for field FeaturesResExt::features_page: {self.features_page} > 255; the value will be truncated")
            self.features_page &= 255
        _span.append((self.features_page << 0))
        if self.max_supported_page > 255:
            print(f"Invalid value for field FeaturesResExt::max_supported_page: {self.max_supported_page} > 255; the value will be truncated")
            self.max_supported_page &= 255
        _span.append((self.max_supported_page << 0))
        _span.extend(self.extended_features)
        return ExtendedPacket.serialize(self, payload = bytes(_span))

    @property
    def size(self) -> int:
        return 10
