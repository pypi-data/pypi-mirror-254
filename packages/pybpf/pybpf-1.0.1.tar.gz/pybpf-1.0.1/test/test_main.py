import pytest
import os

from pybpf import bpf
from pybpf.bpf_header import BPFHeader, InterleaveType, CompressionType, CoordinateSpaceType

BPF_PATH = os.path.join(os.path.dirname(os.getcwd()), r"data/autzen-utm-chipped-25-v3.bpf")
BPF_PATH_ZLIB = os.path.join(os.path.dirname(os.getcwd()), r"data/autzen-utm-chipped-25-v3-deflate.bpf")
BPF_PATH_ZLIB_INTERLEAVED = os.path.join(os.path.dirname(os.getcwd()),
                                         r"data/autzen-utm-chipped-25-v3-deflate-interleaved.bpf")
BPF_PATH_ZLIB_SEGREGATED = os.path.join(os.path.dirname(os.getcwd()),
                                        r"data/autzen-utm-chipped-25-v3-deflate-segregated.bpf")

DIMENSIONS_CHECK = {
    "X": {
        "offset": 494494.275,
        "min": 493994.8700012207,
        "max": 494993.6799987793
    },
    "Y": {
        "offset": 4878123.32,
        "min": 4877429.619987793,
        "max": 4878817.020012207
    },
    "Z": {
        "offset": -0.0,
        "min": 123.93000030517578,
        "max": 178.72999572753906
    },
    "Intensity": {
        "offset": 0.0,
        "min": 0.0,
        "max": 254.0
    },
    "Redown 1": {
        "offset": 0.0,
        "min": 39.0,
        "max": 249.0
    },
    "Greenn 2": {
        "offset": 0.0,
        "min": 57.0,
        "max": 239.0
    },
    "Bluewn 3": {
        "offset": 0.0,
        "min": 56.0,
        "max": 249.0
    },
    "Return Number": {
        "offset": 0.0,
        "min": 1.0,
        "max": 4.0
    },
    "Number of Returns": {
        "offset": 0.0,
        "min": 1.0,
        "max": 4.0
    },
    "Return Information": {
        "offset": 0.0,
        "min": 9.0,
        "max": 100.0
    },
    "Classification": {
        "offset": 0.0,
        "min": 1.0,
        "max": 2.0
    },
}


@pytest.fixture
def bpf_file() -> tuple[bpf.BPF, BPFHeader]:
    bpf_file = bpf.BPF(BPF_PATH)
    bpf_header = bpf_file.get_header()
    return bpf_file, bpf_header


@pytest.fixture
def bpf_file_zlib() -> tuple[bpf.BPF, BPFHeader]:
    bpf_file = bpf.BPF(BPF_PATH_ZLIB)
    bpf_header = bpf_file.get_header()
    return bpf_file, bpf_header


@pytest.fixture
def bpf_file_zlib_interleaved() -> tuple[bpf.BPF, BPFHeader]:
    bpf_file = bpf.BPF(BPF_PATH_ZLIB_INTERLEAVED)
    bpf_header = bpf_file.get_header()
    return bpf_file, bpf_header


@pytest.fixture
def bpf_file_zlib_segregated() -> tuple[bpf.BPF, BPFHeader]:
    bpf_file = bpf.BPF(BPF_PATH_ZLIB_SEGREGATED)
    bpf_header = bpf_file.get_header()
    return bpf_file, bpf_header


def test_point_count_test(bpf_file):
    assert bpf_file[1].point_count == 1065


def test_format_version(bpf_file):
    assert bpf_file[1].format_version == 3


def test_interleave_type(bpf_file, bpf_file_zlib, bpf_file_zlib_interleaved, bpf_file_zlib_segregated):
    assert bpf_file[1].interleave_type is InterleaveType.NON_INTERLEAVED
    assert bpf_file_zlib[1].interleave_type is InterleaveType.NON_INTERLEAVED
    assert bpf_file_zlib_interleaved[1].interleave_type is InterleaveType.INTERLEAVED
    assert bpf_file_zlib_segregated[1].interleave_type is InterleaveType.BYTE_SEGREGATED


def test_compression_type(bpf_file, bpf_file_zlib, bpf_file_zlib_interleaved, bpf_file_zlib_segregated):
    assert bpf_file[1].compression_type is CompressionType.NONE
    assert bpf_file_zlib[1].compression_type is CompressionType.ZLIB_DEFLATE_ALGORITHM
    assert bpf_file_zlib_interleaved[1].compression_type is CompressionType.ZLIB_DEFLATE_ALGORITHM
    assert bpf_file_zlib_segregated[1].compression_type is CompressionType.ZLIB_DEFLATE_ALGORITHM


def test_dimensions(bpf_file):
    assert bpf_file[1].dimension_count == 11
    dimensions = bpf_file[1].get_dimensions()
    for dim in dimensions:
        assert dim.label() in DIMENSIONS_CHECK
        assert dim.offset() == DIMENSIONS_CHECK[dim.label()]["offset"]
        assert dim.minimum() == DIMENSIONS_CHECK[dim.label()]["min"]
        assert dim.maximum() == DIMENSIONS_CHECK[dim.label()]["max"]


def test_header_len(bpf_file):
    assert bpf_file[1].length == 792


def test_has_ulem(bpf_file):
    assert bpf_file[1].has_ulem() is False


def test_transformation_matrix(bpf_file):
    assert bpf_file[1].transformation_matrix.shape == (4, 4)


def test_coordinates_space(bpf_file):
    assert bpf_file[1].coordinates_space_type is CoordinateSpaceType.UTM
    assert bpf_file[1].coordinates_space_id == 10


def test_point_spacing(bpf_file):
    assert bpf_file[1].point_spacing == 0.0


def test_start_end_time(bpf_file):
    assert bpf_file[1].start_time == -1.0
    assert bpf_file[1].start_time == -1.0


def test_read_file(bpf_file, bpf_file_zlib, bpf_file_zlib_interleaved, bpf_file_zlib_segregated):
    data = [
        bpf_file[0].read(),
        bpf_file_zlib[0].read(),
        bpf_file_zlib_interleaved[0].read(),
        bpf_file_zlib_segregated[0].read()
    ]
    for file_data in data:
        for dimension in file_data:
            assert len(file_data[dimension]) == 1065
            assert min(file_data[dimension]) == DIMENSIONS_CHECK[dimension]["min"]
            assert max(file_data[dimension]) == DIMENSIONS_CHECK[dimension]["max"]
