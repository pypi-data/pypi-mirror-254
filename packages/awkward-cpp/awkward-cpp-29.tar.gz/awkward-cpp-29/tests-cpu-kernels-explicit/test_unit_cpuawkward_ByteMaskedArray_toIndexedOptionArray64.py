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

def test_unit_cpuawkward_ByteMaskedArray_toIndexedOptionArray64_1():
    toindex = [123, 123]
    toindex = (ctypes.c_int64*len(toindex))(*toindex)
    length = 2
    mask = [0, 0]
    mask = (ctypes.c_int8*len(mask))(*mask)
    validwhen = False
    funcC = getattr(lib, 'awkward_ByteMaskedArray_toIndexedOptionArray64')
    ret_pass = funcC(toindex, mask, length, validwhen)
    pytest_toindex = [0, 1]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    assert not ret_pass.str

def test_unit_cpuawkward_ByteMaskedArray_toIndexedOptionArray64_2():
    toindex = [123, 123, 123, 123]
    toindex = (ctypes.c_int64*len(toindex))(*toindex)
    length = 4
    mask = [0, 0, 0, 0]
    mask = (ctypes.c_int8*len(mask))(*mask)
    validwhen = False
    funcC = getattr(lib, 'awkward_ByteMaskedArray_toIndexedOptionArray64')
    ret_pass = funcC(toindex, mask, length, validwhen)
    pytest_toindex = [0, 1, 2, 3]
    assert toindex[:len(pytest_toindex)] == pytest.approx(pytest_toindex)
    assert not ret_pass.str

