#!/bin/python3

def main():

	def findPermutation(n, current, cnt, result):
		if len(current) == n:
			result.append(current)
			return

		for i, count in cnt.items():
			if count == 0:
				continue
			cnt[i] -= 1
			findPermutation(n, current + i, cnt, result)
			cnt[i] += 1

	st = "XYZ"

	result = []

	cnt = {}

	for i in st:
		cnt[i] = cnt.get(i, 0) + 1

	findPermutation(len(st), "", cnt, result)
	print(*result)

if __name__ == "__main__":
	main()