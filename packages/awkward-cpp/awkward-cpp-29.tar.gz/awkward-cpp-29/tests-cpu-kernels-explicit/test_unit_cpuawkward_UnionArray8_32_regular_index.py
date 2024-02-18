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

def test_unit_cpuawkward_UnionArray8_32_regular_index_1():
    current = [123, 123]
    current = (ctypes.c_int32*len(current))(*current)
    toindex = [123, 123, 123, 123, 123, 123]
    toindex = (ctypes.c_int32*len(toindex))(*toindex)
    fromtags = [0, 1, 0, 1, 0, 1]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 6
    size = 2
    funcC = getattr(lib, 'awkward_UnionArray8_32_regular_index')
    ret_pass = funcC(toindex, current, size, fromtags, length)
    pytest_current = [3, 3]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)
    pytest_toindex = [0, 0, 1, 1, 2, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    assert not ret_pass.str

def test_unit_cpuawkward_UnionArray8_32_regular_index_2():
    current = [123, 123]
    current = (ctypes.c_int32*len(current))(*current)
    toindex = [123, 123, 123, 123]
    toindex = (ctypes.c_int32*len(toindex))(*toindex)
    fromtags = [1, 0, 1, 1]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 4
    size = 2
    funcC = getattr(lib, 'awkward_UnionArray8_32_regular_index')
    ret_pass = funcC(toindex, current, size, fromtags, length)
    pytest_current = [1, 3]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)
    pytest_toindex = [0, 0, 1, 2]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    assert not ret_pass.str

def test_unit_cpuawkward_UnionArray8_32_regular_index_3():
    current = [123, 123]
    current = (ctypes.c_int32*len(current))(*current)
    toindex = [123, 123, 123, 123, 123, 123, 123, 123]
    toindex = (ctypes.c_int32*len(toindex))(*toindex)
    fromtags = [1, 1, 0, 0, 1, 0, 1, 1]
    fromtags = (ctypes.c_int8*len(fromtags))(*fromtags)
    length = 8
    size = 2
    funcC = getattr(lib, 'awkward_UnionArray8_32_regular_index')
    ret_pass = funcC(toindex, current, size, fromtags, length)
    pytest_current = [3, 5]
    assert current[:len(pytest_current)] == pytest.approx(pytest_current)
    pytest_toindex = [0, 1, 0, 1, 2, 2, 3, 4]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    assert not ret_pass.str

