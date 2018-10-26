if __name__ == "__main__":
    c = 20
    dp = [1]

    for i in range(1, c+1):
        num = 0
        for j in range(i):
            num += dp[j] * dp[i-j-1]
        dp.append(num)

    print(dp[c])