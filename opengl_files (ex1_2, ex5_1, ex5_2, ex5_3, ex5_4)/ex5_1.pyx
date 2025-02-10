cimport cython
import cython
from cython.parallel import parallel, prange

def sum_of_vector(long[:] vector):
	cdef int i
	cdef int total = 0
	cdef int size = vector.shape[0]

	for i in prange(size, schedule='dynamic', num_threads=4, nogil=True):
		total += vector[i]

	return total