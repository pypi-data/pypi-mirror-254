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

def test_unit_cpuawkward_ByteMaskedArray_overlay_mask8_1():
    tomask = [123, 123]
    tomask = (ctypes.c_int8*len(tomask))(*tomask)
    length = 2
    mymask = [0, 0]
    mymask = (ctypes.c_int8*len(mymask))(*mymask)
    theirmask = [0, 0]
    theirmask = (ctypes.c_int8*len(theirmask))(*theirmask)
    validwhen = False
    funcC = getattr(lib, 'awkward_ByteMaskedArray_overlay_mask8')
    ret_pass = funcC(tomask, theirmask, mymask, length, validwhen)
    pytest_tomask = [0, 0]
    assert tomask[:len(pytest_tomask)] == pytest.approx(pytest_tomask)
    assert not ret_pass.str

