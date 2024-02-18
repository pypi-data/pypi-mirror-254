# AUTO GENERATED ON 2024-01-31 AT 17:52:22
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import ctypes
import pytest

from awkward_cpp.cpu_kernels import lib

def test_unit_cpuawkward_ListOffsetArrayU32_toRegularArray_1():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromoffsets = [0, 1, 2, 3]
    fromoffsets = (ctypes.c_uint32*len(fromoffsets))(*fromoffsets)
    offsetslength = 4
    funcC = getattr(lib, 'awkward_ListOffsetArrayU32_toRegularArray')
    ret_pass = funcC(size, fromoffsets, offsetslength)
    pytest_size = [1]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_unit_cpuawkward_ListOffsetArrayU32_toRegularArray_2():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromoffsets = [0, 2, 4]
    fromoffsets = (ctypes.c_uint32*len(fromoffsets))(*fromoffsets)
    offsetslength = 3
    funcC = getattr(lib, 'awkward_ListOffsetArrayU32_toRegularArray')
    ret_pass = funcC(size, fromoffsets, offsetslength)
    pytest_size = [2]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_unit_cpuawkward_ListOffsetArrayU32_toRegularArray_3():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromoffsets = [0, 2, 4, 6]
    fromoffsets = (ctypes.c_uint32*len(fromoffsets))(*fromoffsets)
    offsetslength = 4
    funcC = getattr(lib, 'awkward_ListOffsetArrayU32_toRegularArray')
    ret_pass = funcC(size, fromoffsets, offsetslength)
    pytest_size = [2]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_unit_cpuawkward_ListOffsetArrayU32_toRegularArray_4():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromoffsets = [0, 4]
    fromoffsets = (ctypes.c_uint32*len(fromoffsets))(*fromoffsets)
    offsetslength = 2
    funcC = getattr(lib, 'awkward_ListOffsetArrayU32_toRegularArray')
    ret_pass = funcC(size, fromoffsets, offsetslength)
    pytest_size = [4]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

def test_unit_cpuawkward_ListOffsetArrayU32_toRegularArray_5():
    size = [123]
    size = (ctypes.c_int64*len(size))(*size)
    fromoffsets = [0, 5, 10]
    fromoffsets = (ctypes.c_uint32*len(fromoffsets))(*fromoffsets)
    offsetslength = 3
    funcC = getattr(lib, 'awkward_ListOffsetArrayU32_toRegularArray')
    ret_pass = funcC(size, fromoffsets, offsetslength)
    pytest_size = [5]
    assert size[:len(pytest_size)] == pytest.approx(pytest_size)
    assert not ret_pass.str

