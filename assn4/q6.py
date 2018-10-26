if __name__ == "__main__":
    amt = 15
    dice = 4
    dp = [[0 for i in range(amt+1)] for j in range(dice + 1)]

    for i in range(1, dice + 1):
        for j in range(1, amt + 1):
            if j < 7:
                # if value can be rolled with single die, add one
                dp[i][j] = 1
            for k in range(1, 7):
                if k == j:
                    break
                # up to 6 other rolls can be made
                dp[i][j] += dp[i-1][j-k]

    print(dp[dice][amt])