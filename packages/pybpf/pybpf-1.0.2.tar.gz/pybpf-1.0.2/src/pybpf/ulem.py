import struct

from enum import Enum


class PointCloudDataType(Enum):
    LINEAR_MODE = 0,
    PHOTON_COUNTING = 1,
    NON_LIDAR = 2


class ULEM:
    def __init__(self, ulem_bytes):
        self.ulem_bytes = ulem_bytes

    @property
    def magic_number(self) -> str:
        magic_number_chars = struct.unpack("<4c", self.ulem_bytes[:4])
        return "".join([_.decode("utf-8") for _ in magic_number_chars])

    @property
    def frame_count(self) -> int:
        return struct.unpack("<I", self.ulem_bytes[4:8])[0]

    @property
    def year(self) -> int:
        return struct.unpack("<H", self.ulem_bytes[8:10])[0]

    @property
    def month(self) -> int:
        return struct.unpack("<c", self.ulem_bytes[10])[0]

    @property
    def day(self) -> int:
        return struct.unpack("<c", self.ulem_bytes[11])[0]

    @property
    def point_cloud_data_type(self) -> PointCloudDataType:
        return PointCloudDataType(struct.unpack("<H", self.ulem_bytes[12:14])[0])

    @property
    def laser_wavelength(self) -> int:
        return struct.unpack("<H", self.ulem_bytes[14:16])[0]

    @property
    def laser_pulse_frequency(self) -> int:
        return struct.unpack("<H", self.ulem_bytes[16:18])[0]

    @property
    def focal_plane_width(self) -> int:
        return struct.unpack("<H", self.ulem_bytes[18:20])[0]

    @property
    def focal_plane_height(self) -> int:
        return struct.unpack("<H", self.ulem_bytes[20:22])[0]

    @property
    def focal_plane_ifov_width(self) -> float:
        return struct.unpack("<f", self.ulem_bytes[22:26])[0]

    @property
    def focal_plane_ifov_height(self) -> float:
        return struct.unpack("<f", self.ulem_bytes[26:30])[0]

    @property
    def classification_type(self) -> str:
        classif_chars = struct.unpack("<32c", self.ulem_bytes[30:62])
        return "".join([_ if _ != b'\x00' else "" for _ in classif_chars])
