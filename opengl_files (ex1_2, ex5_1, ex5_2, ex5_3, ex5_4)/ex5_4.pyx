cimport cython
import cython
from cython.parallel import parallel, prange

def biggest_list(double[:] lst):

	cdef int num_threads = 4

	cdef int i, size = lst.shape[0]
	cdef double local_max[4]
	cdef int chunk_size = (size + num_threads - 1) // num_threads

	for i in range(num_threads):
		local_max[i] = -1e300

	cdef int start
	cdef int end
	cdef int j

	for i in prange(num_threads, schedule='dynamic', nogil=True):
		start = i * chunk_size
		end = start + chunk_size
		if end > size: # Passou do final do tamanho.
			end = size
		for j in range(start, end):
			if lst[j] > local_max[i]:
				local_max[i] = lst[j]

	cdef double overall_biggest = local_max[0]

	for i in range(1, num_threads):
		if local_max[i] > overall_biggest:
			overall_biggest = local_max[i]

	return overall_biggest