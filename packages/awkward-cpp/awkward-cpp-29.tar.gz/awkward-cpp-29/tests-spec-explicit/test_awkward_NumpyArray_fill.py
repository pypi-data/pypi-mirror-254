import pytest
import kernels

def test_awkward_NumpyArray_fill_1():
	toptr = [123, 123, 123]
	tooffset = 0
	fromptr = [0, 1, 3]
	length = 3
	funcPy = getattr(kernels, 'awkward_NumpyArray_fill')
	funcPy(toptr = toptr,tooffset = tooffset,fromptr = fromptr,length = length)
	pytest_toptr = [0, 1, 3]
	assert toptr == pytest_toptr


def test_awkward_NumpyArray_fill_2():
	toptr = [123, 123, 123, 123]
	tooffset = 0
	fromptr = [1, 3, 3, 5]
	length = 4
	funcPy = getattr(kernels, 'awkward_NumpyArray_fill')
	funcPy(toptr = toptr,tooffset = tooffset,fromptr = fromptr,length = length)
	pytest_toptr = [1, 3, 3, 5]
	assert toptr == pytest_toptr


def test_awkward_NumpyArray_fill_3():
	toptr = [123, 123]
	tooffset = 0
	fromptr = [3, 5]
	length = 2
	funcPy = getattr(kernels, 'awkward_NumpyArray_fill')
	funcPy(toptr = toptr,tooffset = tooffset,fromptr = fromptr,length = length)
	pytest_toptr = [3, 5]
	assert toptr == pytest_toptr


def test_awkward_NumpyArray_fill_4():
	toptr = [123, 123, 123, 123, 123]
	tooffset = 0
	fromptr = [0, 3, 3, 5, 6]
	length = 5
	funcPy = getattr(kernels, 'awkward_NumpyArray_fill')
	funcPy(toptr = toptr,tooffset = tooffset,fromptr = fromptr,length = length)
	pytest_toptr = [0, 3, 3, 5, 6]
	assert toptr == pytest_toptr


