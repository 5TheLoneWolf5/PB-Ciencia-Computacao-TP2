#!/bin/python3

def fibonacci(num):
	if num <= 1:
		return num

	return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_memo(num):
	def fibonacci_util(n, memo):
		if n <= 1:
			return n
		if memo[n] != -1:
			return memo[n]

		memo[n] = fibonacci_util(n-1, memo) + fibonacci_util(n-2, memo)
		return memo[n]

	memo = [-1] * (num + 1)
	return fibonacci_util(num, memo)

if __name__ == "__main__":
	print("Fibonacci sem memoização")
	print(fibonacci(5))
	print(fibonacci(6))
	print(fibonacci(10))
	print(fibonacci(12))
	print(fibonacci(30))
	print("Fibonacci com memoização")
	print(fibonacci_memo(5))
	print(fibonacci_memo(12))
	print(fibonacci(30))