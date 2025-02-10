cimport cython
import cython
from cython.parallel import parallel, prange
# from libc.stdio import printf
# from openmp cimport omp_set_num_threads # omp_get_wtime

def sum_of_vector(double[:] vector, int threads):
	cdef int i
	cdef double total = 0
	cdef int size = vector.shape[0]

	# omp_set_num_threads(threads)

	# cdef double start_time
	# cdef double end_time

	for i in prange(size, schedule='dynamic', nogil=True, num_threads=threads):
		# start_time = omp_get_wtime()
		total += vector[i]
		# end_time = omp_get_wtime()
		# printf("%d\n", end_time - start_time)

	return total