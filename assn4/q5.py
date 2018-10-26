import os

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + "/matrix.txt") as f:
        lines = f.readlines()

    lines = [line.strip().split(",") for line in lines]
    dp = lines.copy()

    for i in range(80):
        for j in range(80):
            dp[i][j] = int(dp[i][j])
            if i == 0 and j == 0:
                break

            if i == 0:
                dp[0][j] += int(dp[0][j-1])
            elif j == 0:
                dp[i][0] += int(dp[i-1][0])
            else:
                dp[i][j] += min(int(dp[i][j-1]), int(dp[i-1][j]))

    print(dp[79][79])
