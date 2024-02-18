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

def test_unit_cpuawkward_ListArray32_getitem_next_range_counts_64_1():
    total = [123]
    total = (ctypes.c_int64*len(total))(*total)
    fromoffsets = [0, 2, 2, 4, 4, 5, 6, 7, 9, 9]
    fromoffsets = (ctypes.c_int32*len(fromoffsets))(*fromoffsets)
    lenstarts = 9
    funcC = getattr(lib, 'awkward_ListArray32_getitem_next_range_counts_64')
    ret_pass = funcC(total, fromoffsets, lenstarts)
    pytest_total = [9]
    assert total[:len(pytest_total)] == pytest.approx(pytest_total)
    assert not ret_pass.str

def test_unit_cpuawkward_ListArray32_getitem_next_range_counts_64_2():
    total = [123]
    total = (ctypes.c_int64*len(total))(*total)
    fromoffsets = [0, 2, 4, 5, 6, 7, 9]
    fromoffsets = (ctypes.c_int32*len(fromoffsets))(*fromoffsets)
    lenstarts = 6
    funcC = getattr(lib, 'awkward_ListArray32_getitem_next_range_counts_64')
    ret_pass = funcC(total, fromoffsets, lenstarts)
    pytest_total = [9]
    assert total[:len(pytest_total)] == pytest.approx(pytest_total)
    assert not ret_pass.str

