#!/bin/python3

import math

def main():

	# Quicksort usando o último elemento como pivô:

	def partition(list, low, high):
		pivot = list[high]
		i = low - 1
		for j in range(low, high):
			if list[j] <= pivot: # Elementos menores.
				i = i + 1
				list[i], list[j] = list[j], list[i]
		list[i + 1], list[high] = list[high], list[i + 1]
		return i + 1
	def quick_sort(list, low, high):
		if low < high:
			pivot = partition(list, low, high)
			quick_sort(list, low, pivot - 1)
			quick_sort(list, pivot + 1, high)

	# Quicksort usando o primeiro elemento como pivô:

	def partition_first(list, low, high):
		pivot = list[low]
		start = low + 1
		end = high

		while True:
			while start <= end and list[end] >= pivot:
				end = end - 1
			while start <= end and list[start] <= pivot:
				start = start + 1
			if start <= end:
				list[start], list[end] = list[end], list[start]
			else:
				break

		list[low], list[end] = list[end], list[low]

		return end

	def quick_sort_first(list, low, high):
		if low < high:
			pivot = partition_first(list, low, high)
			quick_sort_first(list, low, pivot - 1)
			quick_sort_first(list, pivot + 1, high)

	# Quicksort usando o elemento mediano como pivô:

	def bigger(list, a, b):
		if list[a] > list[b]:
			return a
		return b # returning one of the indexes.

	def median_pivot(list, start, end):

		mid = math.floor((start + end) / 2)
		idx_biggest = bigger(list, start, bigger(list, mid, end))

		if (idx_biggest == start):
			return bigger(list, mid, end)
		if (idx_biggest == end):
			return bigger(list, start, mid)

		return bigger(list, start, end)

	def partition_median(list, low, high):
		pivot_idx = median_pivot(list, low, high)
		list[pivot_idx], list[high] = list[high], list[pivot_idx]
		pivot = list[high]
		i = low - 1
		for j in range(low, high):
			if list[j] <= pivot: # Elementos menores.
				i = i + 1
				list[i], list[j] = list[j], list[i]
		list[i + 1], list[high] = list[high], list[i + 1]
		return i + 1

	def quick_sort_median(list, low, high):
		if low < high:
			pivot = partition_median(list, low, high)
			quick_sort_median(list, low, pivot - 1)
			quick_sort_median(list, pivot + 1, high)
	
	while True:
		user_input = input("-----------------------------------\nDigite o número do pivô da lista:\n\n1 - primeiro elemento.\n2 - último elemento.\n3 - elemento mediano.\n\n")
		pivot = None
		example = [100, -3, 2, 43, 10, 20, 95, 43, 19]

		match(user_input):
			case "1":
				quick_sort_first(example, 0, len(example) - 1)
			case "2":
				quick_sort(example, 0, len(example) - 1)
			case "3":
				quick_sort_median(example, 0, len(example) - 1)
			case _:
				print("\nNúmero não identificado. A lista não foi ordenada.")

		print(f"\nResultado: {example}", end="\n\n")

if __name__ == "__main__":
	main()