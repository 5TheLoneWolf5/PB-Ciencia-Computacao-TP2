#!/bin/python3

import timeit

if __name__ == "__main__":

	setup="import numpy as np\nlst = np.random.uniform(1, 100001, 10000)"

	timeTakenParallel = timeit.timeit(
"result_parallel = biggest_list(lst)\n\
print(result_parallel)\n\
", setup=f"from ex5_4 import biggest_list\n{setup}", number=10)

	print()

	timeTakenSequencial = timeit.timeit(
"result_sequencial = biggest_list_seq(lst)\n\
print(result_sequencial)\n\
", setup=f"def biggest_list_seq(lst):\n\
	biggest = 0\n\
	for i in lst:\n\
		if i > biggest:\n\
			biggest = i\n\
	return biggest\n{setup}", number=10)

	print(f"Paralelo: {timeTakenParallel}")
	print(f"Sequencial: {timeTakenSequencial}")