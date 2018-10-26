if __name__ == "__main__":
    n = 40
    k = 5

    dp = [0 for i in range(n+1)]
    dp[5] = 1

    for i in range(6, n+1):
        dp[i] = int(dp[i-1]*i/(i-k))

    print(dp[40])
