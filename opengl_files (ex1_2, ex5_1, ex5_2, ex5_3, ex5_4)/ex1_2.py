#!/bin/python3

# from multiprocessing import Pool
# import random

# def main():
# 	def sum_chunk(chunk):
# 		return sum(chunk)

# 	data = [random.randint(1, 100000) for _ in range(10000)]
# 	chunks = [data[i:i + 1000] for i in range(0, len(data), 1000)]

# 	with Pool() as pool:
# 		result = sum(pool.map(sum_chunk, chunks))

# 	print(result)

# if __name__ == "__main__":
# 	main()

import timeit

if __name__ == "__main__":

	setup="import numpy as np\nvector = np.random.uniform(1, 100001, 10000)"

	limitThreads = 16 # Ou 1, se quiser usar apenas uma thread (de forma padrão, sequencialmente). Ou deixar o OpenMP resolver sozinho.
	i = 1

	while i <= limitThreads:
		timeTakenParallel = timeit.timeit(
f"\n\
result_parallel = sum_of_vector(vector, {i})\n\
print(result_parallel)\n\
", setup=f"from ex1_2 import sum_of_vector\n{setup}", number=10)
		print(f"Tempo: {timeTakenParallel}. Número de Threads: {i}")
		i *= 2

	timeTakenSequencial = timeit.timeit(
"result_sequencial = sum_of_vector_seq(vector)\n\
print(result_sequencial)\n\
", setup=f"def sum_of_vector_seq(vector):\n\
	total = 0\n\
	for i in vector:\n\
		total += i\n\
	return total\n{setup}", number=10)

	# print(f"Paralelo: {timeTakenParallel}")
	print(f"Sequencial: {timeTakenSequencial}")