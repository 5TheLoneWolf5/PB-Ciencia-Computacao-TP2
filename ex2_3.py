#!/bin/python3

import random

def quick_select(array, low, high, k):
    if low == high:
        return array[low]

    pivot_index = partition(array, low, high)

    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quick_select(array, low, pivot_index - 1, k)
    else:
        return quick_select(array, pivot_index + 1, high, k)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

def main():
    array1 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array2 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array3 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array4 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array5 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array6 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array7 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array8 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array9 = [random.randint(1, 1000) for _ in range(1, 10001)]
    array10 = [random.randint(1, 1000) for _ in range(1, 10001)]

    setArrays = [array1, array2, array3, array4, array5, array6, array7, array8, array9, array10]

    k1 = 5 # 5th smallest element
    k2 = 50 # 50th smallest
    k3 = 100 # And so on...
    k4 = 250
    k5 = 500

    ks = [k1, k2, k3, k4, k5]

    for idx, i in enumerate(setArrays):
        print(f"Array {idx + 1}:")
        for j in ks:
            print(quick_select(i[:], 0, len(i) - 1, j - 1))
        print()

if __name__ == "__main__":
    main()