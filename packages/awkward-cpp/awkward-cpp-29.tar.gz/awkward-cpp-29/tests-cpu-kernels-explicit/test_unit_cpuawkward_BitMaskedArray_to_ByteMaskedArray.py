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

def test_unit_cpuawkward_BitMaskedArray_to_ByteMaskedArray_1():
    tobytemask = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
    tobytemask = (ctypes.c_int8*len(tobytemask))(*tobytemask)
    bitmasklength = 2
    frombitmask = [58, 59]
    frombitmask = (ctypes.c_uint8*len(frombitmask))(*frombitmask)
    lsb_order = False
    validwhen = False
    funcC = getattr(lib, 'awkward_BitMaskedArray_to_ByteMaskedArray')
    ret_pass = funcC(tobytemask, frombitmask, bitmasklength, validwhen, lsb_order)
    pytest_tobytemask = [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
    assert tobytemask[:len(pytest_tobytemask)] == pytest.approx(pytest_tobytemask)
    assert not ret_pass.str

def test_unit_cpuawkward_BitMaskedArray_to_ByteMaskedArray_2():
    tobytemask = [123, 123, 123, 123, 123, 123, 123, 123]
    tobytemask = (ctypes.c_int8*len(tobytemask))(*tobytemask)
    bitmasklength = 1
    frombitmask = [66]
    frombitmask = (ctypes.c_uint8*len(frombitmask))(*frombitmask)
    lsb_order = True
    validwhen = False
    funcC = getattr(lib, 'awkward_BitMaskedArray_to_ByteMaskedArray')
    ret_pass = funcC(tobytemask, frombitmask, bitmasklength, validwhen, lsb_order)
    pytest_tobytemask = [0, 1, 0, 0, 0, 0, 1, 0]
    assert tobytemask[:len(pytest_tobytemask)] == pytest.approx(pytest_tobytemask)
    assert not ret_pass.str

def test_unit_cpuawkward_BitMaskedArray_to_ByteMaskedArray_3():
    tobytemask = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
    tobytemask = (ctypes.c_int8*len(tobytemask))(*tobytemask)
    bitmasklength = 2
    frombitmask = [58, 59]
    frombitmask = (ctypes.c_uint8*len(frombitmask))(*frombitmask)
    lsb_order = True
    validwhen = False
    funcC = getattr(lib, 'awkward_BitMaskedArray_to_ByteMaskedArray')
    ret_pass = funcC(tobytemask, frombitmask, bitmasklength, validwhen, lsb_order)
    pytest_tobytemask = [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    assert tobytemask[:len(pytest_tobytemask)] == pytest.approx(pytest_tobytemask)
    assert not ret_pass.str

