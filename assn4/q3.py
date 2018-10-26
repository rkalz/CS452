import os

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + "/triangles.txt") as f:
        lines = f.readlines()

    lines = [line.strip().split(' ') for line in lines]
    dp = lines.copy()
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            if j == 0:
                # Left edge, only one parent
                dp[i][j] = int(lines[i][j]) + int(lines[i-1][0])
            elif j == len(lines[i]) - 1:
                # Right edge, only one parent
                dp[i][j] = int(lines[i][j]) + int(lines[i-1][j-1])
            else:
                # Pick the parent that gives the largest solution
                dp[i][j] = max(int(lines[i][j]) + int(lines[i-1][j-1]),
                               int(lines[i][j]) + int(lines[i-1][j]))


    max_val = 0
    for num in dp[-1]:
        max_val = max(max_val, num)

    print(max_val)