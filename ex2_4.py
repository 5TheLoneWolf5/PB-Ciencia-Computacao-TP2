#!/bin/python3

import random

# Tarefas 1 e 2:

def medianUtil(array, l, r, k, a, b):
    if l <= r:
    	idxPartition = randomPartition(array, l, r)
    	if idxPartition == k:
    		b[0] = array[idxPartition]
    		if a[0] != -1:
    			return
    	elif idxPartition == k - 1:
    		a[0] = array[idxPartition]
    		if b[0] != -1:
    			return
    	if idxPartition >= k:
    		medianUtil(array, l, idxPartition - 1, k, a, b)
    	else:
    		medianUtil(array, idxPartition + 1, r, k, a, b)


def randomPartition(array, l, r):
	n = r - l + 1
	pivot = random.randint(0, n - 1)
	array[l + pivot], array[r] = array[r], array[l + pivot]
	return partition(array, l, r)

def partition(array, l, r):
    pivot = array[r]
    i = l
    j = l

    while j < r:
    	if array[j] < pivot:
    		array[i], array[j] = array[j], array[i]
    		i += 1
    	j += 1
    array[i], array[r] = array[r], array[i]
    return i

def findMedian(array):
	a = [-1]
	b = [-1]
	n = len(array)
	if n % 2 == 1:
		medianUtil(array, 0, n - 1, n // 2, a, b)
		return b[0]
	else:
		medianUtil(array, 0, n - 1, n // 2, a, b)
		return (a[0] + b[0]) / 2.0

def main():
    array = [random.randint(1, 1000) for _ in range(1, 10001)]
    print(findMedian(array))

if __name__ == "__main__":
	main()