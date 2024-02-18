import struct


class Dimension:
    def __init__(self, dim_bytes, dim_index, dims_count):
        self._dim_bytes = dim_bytes
        self._dim_index = dim_index
        self._dims_count = dims_count

    @classmethod
    def from_bytes(cls, dims_bytes, dims_count) -> list:
        return [cls(dims_bytes, _, dims_count) for _ in range(dims_count)]

    def offset(self) -> float:
        dim_offset = 8 * self._dim_index
        return struct.unpack("<d", self._dim_bytes[dim_offset:dim_offset + 8])[0]

    def minimum(self) -> float:
        minimum_offset = 8 * self._dims_count + 8 * self._dim_index
        return struct.unpack("<d", self._dim_bytes[minimum_offset:minimum_offset + 8])[0]

    def maximum(self) -> float:
        maximum_offset = 16 * self._dims_count + 8 * self._dim_index
        return struct.unpack("<d", self._dim_bytes[maximum_offset:maximum_offset + 8])[0]

    def label(self) -> str:
        label_offset = 24 * self._dims_count + 32 * self._dim_index
        label_chars = struct.unpack("<32c", self._dim_bytes[label_offset:label_offset + 32])
        return "".join([_.decode() if _ != b'\x00' else "" for _ in label_chars])

