#!/bin/python3

def main():
	def partition(list, low, high):
		pivot = list[high]["nota"]
		i = low - 1
		for j in range(low, high):
			if list[j]["nota"] <= pivot:
				i = i + 1
				list[i], list[j] = list[j], list[i]
		list[i + 1], list[high] = list[high], list[i + 1]
		return i + 1
	def quick_sort(list, low, high):
		if low < high:
			pivot = partition(list, low, high)
			quick_sort(list, low, pivot - 1)
			quick_sort(list, pivot + 1, high)
	
	estudantes = [
		{
			"nome": "Adam",
			"nota": 9.2
		},
		{
			"nome": "Sophie",
			"nota": 4.5
		},
		{
			"nome": "Peter",
			"nota": 10.0
		}
		,
		{
			"nome": "Matt",
			"nota": 7.0
		}
		,
		{
			"nome": "John",
			"nota": 4.3
		}
		,
		{
			"nome": "Daniel",
			"nota": 2.3
		}
	]
	
	quick_sort(estudantes, 0, len(estudantes) - 1)
	print(estudantes)

if __name__ == "__main__":
	main()