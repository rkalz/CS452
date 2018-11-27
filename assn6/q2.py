def staircase(steps):
    dp = [0 for _ in range(steps+1)]
    dp[0] = dp[1] = 1

    for i in range(2, steps+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


if __name__ == "__main__":
    print(staircase(200))