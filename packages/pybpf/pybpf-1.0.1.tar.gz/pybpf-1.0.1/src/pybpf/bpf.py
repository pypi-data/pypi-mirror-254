import struct
import zlib
import io

from pybpf.bpf_header import BPFHeader, InterleaveType, CompressionType
from pybpf.exceptions import EmptyFileException, UnknownDataTypeException


class BPF:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.bpf_file = open(file_path, mode="rb")

        if not file_path.endswith(".bpf"):
            raise IOError("Invalid BPF file")

        self.magic_number_bytes = self.bpf_file.read(4)

        if self.magic_number() != "BPF!":
            raise IOError("Invalid BPF file")

        self.header = BPFHeader(self.bpf_file)

    def get_header(self) -> BPFHeader:
        return self.header

    def magic_number(self) -> str:
        magic_number_chars = struct.unpack("<4c", self.magic_number_bytes)
        return "".join([c.decode("utf-8") for c in magic_number_chars])

    def read(self) -> dict:
        if self.header.point_count == 0:
            raise EmptyFileException
        self.bpf_file.seek(self.header.length)
        if self.header.interleave_type is InterleaveType.INTERLEAVED:
            return self._read_ipd()
        elif self.header.interleave_type is InterleaveType.NON_INTERLEAVED:
            return self._read_nipd()
        elif self.header.interleave_type is InterleaveType.BYTE_SEGREGATED:
            return self._read_bsbd()
        else:
            raise UnknownDataTypeException

    def _read_ipd(self) -> dict:
        data = dict.fromkeys([dim.label() for dim in self.header.get_dimensions()])
        if self.header.compression_type in [CompressionType.NONE, CompressionType.UNUSED]:
            for pt in range(self.header.point_count):
                unpack_pt = struct.unpack("<%sf" % str(self.header.dimension_count),
                                          self.bpf_file.read(4 * self.header.dimension_count))
                for i, dim in enumerate(self.header.get_dimensions()):
                    if data[dim.label()] is None:
                        data[dim.label()] = [unpack_pt[i] + dim.offset()]
                    else:
                        data[dim.label()].append(unpack_pt[i] + dim.offset())
        elif self.header.compression_type is CompressionType.ZLIB_DEFLATE_ALGORITHM:
            decompressed_pts = 0
            while decompressed_pts < self.header.point_count:
                ubc, cbc = struct.unpack("<2I", self.bpf_file.read(8))
                chunk_bytes = zlib.decompress(self.bpf_file.read(cbc))
                # TODO: Check the decompressed size (raise exception if the size is incorrect)
                chunk_pts_count = int(ubc / (4 * self.header.dimension_count))
                for i, pt in enumerate(range(chunk_pts_count)):
                    pt_size = self.header.dimension_count * 4
                    pt_offset = self.header.dimension_count * 4 * i
                    unpack_pt = struct.unpack("<%sf" % str(self.header.dimension_count),
                                              chunk_bytes[pt_offset:pt_offset + pt_size])
                    for j, dim in enumerate(self.header.get_dimensions()):
                        if data[dim.label()] is None:
                            data[dim.label()] = [unpack_pt[j] + dim.offset()]
                        else:
                            data[dim.label()].append(unpack_pt[j] + dim.offset())
                    decompressed_pts += 1
        else:
            raise NotImplementedError("Compression format not supported")

        return data

    def _read_nipd(self) -> dict:
        data = dict.fromkeys([dim.label() for dim in self.header.get_dimensions()])
        for i, dim in enumerate(self.header.get_dimensions()):
            if self.header.compression_type in [CompressionType.NONE, CompressionType.UNUSED]:
                unpack_dim = struct.unpack("<%sf" % str(self.header.point_count),
                                           self.bpf_file.read(4 * self.header.point_count))
            elif self.header.compression_type is CompressionType.ZLIB_DEFLATE_ALGORITHM:
                ubc, cbc = struct.unpack("<2I", self.bpf_file.read(8))
                chunk_bytes = zlib.decompress(self.bpf_file.read(cbc))
                unpack_dim = struct.unpack("<%sf" % str(self.header.point_count), chunk_bytes)
            else:
                raise NotImplementedError("Compression format not supported")
            data[dim.label()] = [_ + dim.offset() for _ in unpack_dim]

        return data

    def _read_bsbd(self) -> dict:
        data = dict.fromkeys([dim.label() for dim in self.header.get_dimensions()])
        if self.header.compression_type is [CompressionType.NONE, CompressionType.UNUSED]:
            for i, dim in enumerate(self.header.get_dimensions()):
                dim_bytes = dict.fromkeys([_ for _ in range(4)])
                for idx in range(4):
                    dim_bytes[idx] = self.bpf_file.read(self.header.point_count)
                for pt in range(self.header.point_count):
                    pt_dim = struct.unpack("<f", b"".join([dim_bytes[_][pt:pt+1] for _ in dim_bytes]))
                    if data[dim.label()] is None:
                        data[dim.label()] = [pt_dim[0] + dim.offset()]
                    else:
                        data[dim.label()].append(pt_dim[0] + dim.offset())
        elif self.header.compression_type is CompressionType.ZLIB_DEFLATE_ALGORITHM:
            decompressed_pts = 0
            while decompressed_pts < self.header.point_count:
                data_debug = self.bpf_file.read(8)
                ubc, cbc = struct.unpack("<2I", data_debug)
                uncompressed_data = io.BytesIO(zlib.decompress(self.bpf_file.read(cbc)))
                for i, dim in enumerate(self.header.get_dimensions()):
                    dim_bytes = dict.fromkeys([_ for _ in range(4)])
                    for idx in range(4):
                        dim_bytes[idx] = uncompressed_data.read(self.header.point_count)
                    for pt in range(self.header.point_count):
                        pt_dim = struct.unpack("<f", b"".join([dim_bytes[_][pt:pt + 1] for _ in dim_bytes]))
                        if data[dim.label()] is None:
                            data[dim.label()] = [pt_dim[0] + dim.offset()]
                        else:
                            data[dim.label()].append(pt_dim[0] + dim.offset())
                        decompressed_pts += 1
        else:
            raise NotImplementedError("Compression format not supported")
        return data

    def __del__(self):
        self.bpf_file.close()
