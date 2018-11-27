import os


def robber(houses):
    dp = [0 for _ in range(len(houses))]

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        # Which is better: This house and the house 2 away,
        # Or the previous house?
        dp[i] = max(houses[i] + dp[i-2], dp[i-1])

    return dp[-1]


def get_numbers(filename):
    with open(os.path.dirname(os.path.realpath(__file__)) + "/" + filename) as f:
        lines = f.readlines()

    numbers = []
    lines = [line.strip() for line in lines]
    for line in lines:
        nums = line.split(' ')
        for num in nums:
            numbers.append(int(num))

    return numbers


if __name__ == "__main__":
    houses = get_numbers("Money.txt")
    print(robber(houses))