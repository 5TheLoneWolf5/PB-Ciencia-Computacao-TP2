#!/bin/python3

def _min_coins(i, sum, coins, memo):

	if sum == 0:
		return 0
	if sum < 0 or i == len(coins):
		return float("inf")

	if memo[i][sum] != -1:
		return memo[i][sum]

	take = float("inf")

	if coins[i] > 0:
		take = _min_coins(i, sum - coins[i], coins, memo)
		if take != float("inf"):
			take += 1

	noTake = _min_coins(i + 1, sum, coins, memo)

	memo[i][sum] = min(take, noTake)
	return memo[i][sum]

def min_coins(coins, sum):
	memo = [[-1] * (sum + 1) for _ in range(len(coins))]
	result = _min_coins(0, sum, coins, memo)
	return result if result != float("inf") else -1

if __name__ == "__main__":
	print(min_coins([4, 2, 3, 2], 15)) # 4 4 4 3 -> 4 coins.
	print(min_coins([5, 10, 15], 20))
	print(min_coins([1, 5, 9], 19))