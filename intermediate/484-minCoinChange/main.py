from math import inf as INF


def minCoinChange(coins: list, amount: int) -> int:
    coins_length = len(coins)
    dp = [
        [INF if i != 0 else 0 for i in range(amount + 1)]
        for _ in range(coins_length + 1)
    ]

    for i in range(1, coins_length + 1):
        coin = coins[i - 1]

        for j in range(1, amount + 1):

            if coin > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i][j - coin] + 1, dp[i - 1][j])

    return dp[coins_length][amount] if dp[coins_length][amount] != INF else -1


# print(minCoinChange([1, 3, 4, 5], 7))
