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

def test_unit_cpuawkward_ByteMaskedArray_reduce_next_nonlocal_nextshifts_64_1():
    nextshifts = [123, 123, 123, 123, 123]
    nextshifts = (ctypes.c_int64*len(nextshifts))(*nextshifts)
    length = 7
    mask = [0, 0, 0, 1, 1, 0, 0]
    mask = (ctypes.c_int8*len(mask))(*mask)
    valid_when = False
    funcC = getattr(lib, 'awkward_ByteMaskedArray_reduce_next_nonlocal_nextshifts_64')
    ret_pass = funcC(nextshifts, mask, length, valid_when)
    pytest_nextshifts = [0, 0, 0, 2, 2]
    assert nextshifts[:len(pytest_nextshifts)] == pytest.approx(pytest_nextshifts)
    assert not ret_pass.str

