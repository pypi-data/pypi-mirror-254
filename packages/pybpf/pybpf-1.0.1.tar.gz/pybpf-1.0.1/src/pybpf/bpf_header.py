import struct
import numpy as np

from enum import Enum
from pybpf.dimension import Dimension
from pybpf.ulem import ULEM


class CoordinateSpaceType(Enum):
    CARTESIAN = 0
    UTM = 1  # Universal Transverse Mercator
    TCR = 2  # Terrestrial Centered Rotational
    ENU = 3  # East North Up


class InterleaveType(Enum):
    NON_INTERLEAVED = 0
    INTERLEAVED = 1
    BYTE_SEGREGATED = 2


class CompressionType(Enum):
    NONE = 0
    UNUSED = 1
    FASTLZ = 2
    ZLIB_DEFLATE_ALGORITHM = 3


class BPFHeader:
    def __init__(self, bpf_io) -> None:
        self.bpf_io = bpf_io
        self.bpf_io.seek(4)
        self._base_header_bytes = self.bpf_io.read(172)
        self._unpack_char = struct.unpack("<4c", self._base_header_bytes[0:4])
        self._unpack_header_len = struct.unpack("<i", self._base_header_bytes[4:8])
        self._unpack_unsigned_int = struct.unpack("<4b", self._base_header_bytes[8:12])
        self._unpack_int = struct.unpack("<3i", self._base_header_bytes[12:24])
        self._unpack_float = struct.unpack("<f", self._base_header_bytes[24:28])
        self._unpack_double = struct.unpack("<18d", self._base_header_bytes[28:172])
        self._sub_header_bytes = self.bpf_io.read(self.dimension_count * 56)
        self._ulem_bundles_bytes = self.bpf_io.read(self.length - self.bpf_io.tell()) if self.bpf_io.tell() < \
                                                                                         self.length else None

    @property
    def length(self) -> int:
        return self._unpack_header_len[0]

    @property
    def format_version(self) -> int:
        return int("".join([c.decode("utf-8") for c in self._unpack_char]))

    @property
    def point_count(self) -> int:
        return self._unpack_int[0]

    @property
    def dimension_count(self) -> int:
        return self._unpack_unsigned_int[0]

    @property
    def point_spacing(self) -> float:
        return self._unpack_float[0]

    @property
    def transformation_matrix(self) -> np.ndarray:
        return np.asarray([_ for _ in self._unpack_double[:16]], dtype=np.float64).reshape((4, 4))

    @property
    def start_time(self) -> float:
        return self._unpack_double[16]

    @property
    def end_time(self) -> float:
        return self._unpack_double[17]

    @property
    def coordinates_space_id(self) -> int:
        return self._unpack_int[2]

    @property
    def coordinates_space_type(self) -> CoordinateSpaceType:
        return CoordinateSpaceType(self._unpack_int[1])

    @property
    def interleave_type(self) -> InterleaveType:
        return InterleaveType(self._unpack_unsigned_int[1])

    @property
    def compression_type(self) -> CompressionType:
        return CompressionType(self._unpack_unsigned_int[2])

    def get_dimensions(self) -> list[Dimension]:
        return Dimension.from_bytes(self._sub_header_bytes, self.dimension_count)

    def has_ulem(self) -> bool:
        if self._ulem_bundles_bytes is None:
            return False

        ulem_chars = struct.unpack("<4c", self._ulem_bundles_bytes[:4])
        ulem_check = "".join([_.decode() if _ != b'\x00' else "" for _ in ulem_chars])
        return ulem_check == "ULEM"

    def get_ulem(self) -> ULEM:
        return ULEM(self._ulem_bundles_bytes[:62]) if self.has_ulem() else None


