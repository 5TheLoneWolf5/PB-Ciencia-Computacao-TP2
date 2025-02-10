#!/bin/python3

def factorial(num):
	if num <= 1:
		return 1

	return num * factorial(num-1) 

if __name__ == "__main__":
	print(factorial(5))
	print(factorial(6))
	print(factorial(10))
	print(factorial(12))