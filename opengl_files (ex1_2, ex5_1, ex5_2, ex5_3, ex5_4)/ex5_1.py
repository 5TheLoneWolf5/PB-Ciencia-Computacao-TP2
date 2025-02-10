#!/bin/python3

# from multiprocessing import Pool

# def sum_parallel(lst):
# 	with Pool() as pool:
# 		chunk_size = len(lst) // 4
# 		chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
# 		results = pool.map(sum, chunks)
# 	return sum(results)

# if __name__ == "__main__":
# 	print(f"Soma: {sum_parallel(list(range(1, 10001)))}")

import timeit

if __name__ == "__main__":

	setup="import numpy as np\nvector = np.array(range(1, 10001))"

	timeTakenParallel = timeit.timeit(
"result_parallel = sum_of_vector(vector)\n\
print(result_parallel)\n\
", setup=f"from ex5_1 import sum_of_vector\n{setup}", number=10)

	print()

	timeTakenSequencial = timeit.timeit(
"result_sequencial = sum_of_vector_seq(vector)\n\
print(result_sequencial)\n\
", setup=f"def sum_of_vector_seq(vector):\n\
	total = 0\n\
	for i in vector:\n\
		total += i\n\
	return total\n{setup}", number=10)

	print(f"Paralelo: {timeTakenParallel}")
	print(f"Sequencial: {timeTakenSequencial}")