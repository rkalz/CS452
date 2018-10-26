if __name__ == "__main__":
    x = 21
    y = 21
    dp = [[0 for i in range(x+1)] for j in range(y+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[x][y])