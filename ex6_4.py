#!/bin/python3

def count_ways(nCadeiras, nCores, memo):
	if nCadeiras == 1:
		return nCores
	if nCadeiras == 2:
		return nCores * nCores

	if memo[nCadeiras] != -1:
		return memo[nCadeiras]

	cnt1 = count_ways(nCadeiras - 1, nCores, memo) * (nCores - 1)
	cnt2 = count_ways(nCadeiras - 2, nCores, memo) * (nCores - 1)

	memo[nCadeiras] = cnt1 + cnt2
	return memo[nCadeiras]

def max_pinturas_cadeiras(nCadeiras, nCores):

	memo = [-1] * (nCadeiras + 1)
	return count_ways(nCadeiras, nCores, memo)

if __name__ == "__main__":
	nCadeiras = 5
	nCores = 2
	print(max_pinturas_cadeiras(nCadeiras, nCores))