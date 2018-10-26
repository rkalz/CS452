if __name__ == "__main__":
    dp = [5, 6]
    while dp[-1] < 50000000000:
        dp.append(dp[-1] + dp[-2])
    dp.pop(-1)  # Last value is greater than 50b

    odd_sum = 0
    for num in dp:
        if num % 2 == 1:
            odd_sum += num

    print(odd_sum)