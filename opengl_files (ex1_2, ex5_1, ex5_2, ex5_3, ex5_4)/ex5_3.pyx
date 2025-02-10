cimport cython
import cython
from cython.parallel import parallel, prange

cdef int partition(long[:] list, int low, int high) nogil:
		cdef long pivot = list[high]
		cdef int i = low - 1
		cdef int j
		cdef long temp
		for j in range(low, high):
			if list[j] <= pivot: # Elementos menores.
				i = i + 1
				temp = list[i]
				list[i] = list[j]
				list[j] = temp
		temp = list[i + 1]
		list[i + 1] = list[high]
		list[high] = temp
		return i + 1

cdef void _quicksort(long[:] list, int low, int high, int depth) nogil:
	cdef int pivot
	if low < high:
		pivot = partition(list, low, high)
		if depth > 0:
			# with nogil:
			with parallel():
				_quicksort(list, low, pivot - 1, depth - 1)
				_quicksort(list, pivot + 1, high, depth - 1)
		else:
			_quicksort(list, low, pivot - 1, depth)
			_quicksort(list, pivot + 1, high, depth)

def quicksort(long[:] list):
	levels = 4
	_quicksort(list, 0, list.shape[0] -1, levels)