#!/bin/python3

import timeit
import sys

sys.setrecursionlimit(15000)

if __name__ == "__main__":

	setup="import copy\nimport numpy as np\nlst = np.random.randint(1, 10000, 10000)\nlst_parallel, lst_seq = copy.deepcopy(lst), copy.deepcopy(lst)\n"

	timeTakenParallel = timeit.timeit(
"quicksort(lst_parallel)\n\
", setup=f"from ex5_3 import quicksort\n{setup}", number=10)

	print()

	timeTakenSequencial = timeit.timeit(
"quicksort(lst_seq, 0, len(lst_seq) - 1)\n\
", setup=f"\n\
def partition(list, low, high):\n\
	pivot = list[high]\n\
	i = low - 1\n\
	for j in range(low, high):\n\
		if list[j] <= pivot:\n\
			i = i + 1\n\
			list[i], list[j] = list[j], list[i]\n\
	list[i + 1], list[high] = list[high], list[i + 1]\n\
	return i + 1\n\
def quicksort(list, low, high):\n\
	if low < high:\n\
		pivot = partition(list, low, high)\n\
		quicksort(list, low, pivot - 1)\n\
		quicksort(list, pivot + 1, high)\n{setup}", number=10)

	print(f"Paralelo: {timeTakenParallel}")
	print(f"Sequencial: {timeTakenSequencial}")