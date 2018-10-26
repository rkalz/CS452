if __name__ == "__main__":
    coins = [5, 10, 25, 50, 100, 200, 500, 1000]
    value = 500

    dp = [[0 for i in range(value + 1)] for j in range(len(coins))]
    for i in range(len(coins)):
        coin = coins[i]
        for j in range(value + 1):
            if j == 0:
                dp[i][0] = 1
            elif j < coin:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin]

    print(dp[len(coins)-1][value])