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

def test_unit_cpuawkward_ListArray32_getitem_jagged_descend_64_1():
    tooffsets = [123, 123, 123]
    tooffsets = (ctypes.c_int64*len(tooffsets))(*tooffsets)
    fromstarts = [0, 2]
    fromstarts = (ctypes.c_int32*len(fromstarts))(*fromstarts)
    fromstops = [2, 4]
    fromstops = (ctypes.c_int32*len(fromstops))(*fromstops)
    sliceouterlen = 2
    slicestarts = [0, 2]
    slicestarts = (ctypes.c_int64*len(slicestarts))(*slicestarts)
    slicestops = [2, 4]
    slicestops = (ctypes.c_int64*len(slicestops))(*slicestops)
    funcC = getattr(lib, 'awkward_ListArray32_getitem_jagged_descend_64')
    ret_pass = funcC(tooffsets, slicestarts, slicestops, sliceouterlen, fromstarts, fromstops)
    pytest_tooffsets = [0, 2, 4]
    assert tooffsets[:len(pytest_tooffsets)] == pytest.approx(pytest_tooffsets)
    assert not ret_pass.str

def test_unit_cpuawkward_ListArray32_getitem_jagged_descend_64_2():
    tooffsets = [123, 123, 123, 123, 123]
    tooffsets = (ctypes.c_int64*len(tooffsets))(*tooffsets)
    fromstarts = [0, 3, 3, 4]
    fromstarts = (ctypes.c_int32*len(fromstarts))(*fromstarts)
    fromstops = [3, 3, 4, 5]
    fromstops = (ctypes.c_int32*len(fromstops))(*fromstops)
    sliceouterlen = 4
    slicestarts = [0, 3, 3, 4]
    slicestarts = (ctypes.c_int64*len(slicestarts))(*slicestarts)
    slicestops = [3, 3, 4, 5]
    slicestops = (ctypes.c_int64*len(slicestops))(*slicestops)
    funcC = getattr(lib, 'awkward_ListArray32_getitem_jagged_descend_64')
    ret_pass = funcC(tooffsets, slicestarts, slicestops, sliceouterlen, fromstarts, fromstops)
    pytest_tooffsets = [0, 3, 3, 4, 5]
    assert tooffsets[:len(pytest_tooffsets)] == pytest.approx(pytest_tooffsets)
    assert not ret_pass.str

def test_unit_cpuawkward_ListArray32_getitem_jagged_descend_64_3():
    tooffsets = [123, 123, 123, 123]
    tooffsets = (ctypes.c_int64*len(tooffsets))(*tooffsets)
    fromstarts = [0, 3, 3]
    fromstarts = (ctypes.c_int32*len(fromstarts))(*fromstarts)
    fromstops = [3, 3, 5]
    fromstops = (ctypes.c_int32*len(fromstops))(*fromstops)
    sliceouterlen = 3
    slicestarts = [0, 3, 3]
    slicestarts = (ctypes.c_int64*len(slicestarts))(*slicestarts)
    slicestops = [3, 3, 5]
    slicestops = (ctypes.c_int64*len(slicestops))(*slicestops)
    funcC = getattr(lib, 'awkward_ListArray32_getitem_jagged_descend_64')
    ret_pass = funcC(tooffsets, slicestarts, slicestops, sliceouterlen, fromstarts, fromstops)
    pytest_tooffsets = [0, 3, 3, 5]
    assert tooffsets[:len(pytest_tooffsets)] == pytest.approx(pytest_tooffsets)
    assert not ret_pass.str

def test_unit_cpuawkward_ListArray32_getitem_jagged_descend_64_4():
    tooffsets = [123, 123, 123]
    tooffsets = (ctypes.c_int64*len(tooffsets))(*tooffsets)
    fromstarts = [0, 3]
    fromstarts = (ctypes.c_int32*len(fromstarts))(*fromstarts)
    fromstops = [3, 6]
    fromstops = (ctypes.c_int32*len(fromstops))(*fromstops)
    sliceouterlen = 2
    slicestarts = [0, 3]
    slicestarts = (ctypes.c_int64*len(slicestarts))(*slicestarts)
    slicestops = [3, 6]
    slicestops = (ctypes.c_int64*len(slicestops))(*slicestops)
    funcC = getattr(lib, 'awkward_ListArray32_getitem_jagged_descend_64')
    ret_pass = funcC(tooffsets, slicestarts, slicestops, sliceouterlen, fromstarts, fromstops)
    pytest_tooffsets = [0, 3, 6]
    assert tooffsets[:len(pytest_tooffsets)] == pytest.approx(pytest_tooffsets)
    assert not ret_pass.str

