import pytest
import kernels

def test_awkward_IndexedArray_overlay_mask_1():
	toindex = [123, 123, 123, 123, 123, 123]
	fromindex = [5, 4, 3, 2, 1, 0]
	length = 6
	mask = [0, 0, 0, 0, 0, 0]
	funcPy = getattr(kernels, 'awkward_IndexedArray_overlay_mask')
	funcPy(toindex = toindex,fromindex = fromindex,length = length,mask = mask)
	pytest_toindex = [5, 4, 3, 2, 1, 0]
	assert toindex == pytest_toindex


