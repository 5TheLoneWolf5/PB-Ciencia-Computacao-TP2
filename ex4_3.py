#!/bin/python3

import timeit

if __name__ == "__main__":

	results = []

	for i in [1, 5, 10, 15, 20, 25, 30]:
		timeTaken = timeit.timeit(
f"Tower_Of_Hanoi({i}, 'A', 'C', 'B')", setup=f"\n\
def Tower_Of_Hanoi(n, from_rod, to_rod, aux_rod):\n\
	if n == 0:\n\
		return\n\
	Tower_Of_Hanoi(n-1, from_rod, aux_rod, to_rod)\n\
	print('Disco', n, 'movido da haste', from_rod, 'para a haste', to_rod)\n\
	Tower_Of_Hanoi(n-1, aux_rod, to_rod, from_rod)\n", number=1)

		results.append((i, timeTaken))
	
	for i, timeTaken in results:
		print(f"{i} disco(s): — Tempo: {timeTaken}")