# python3 q13_pow.py

# If n is even, n is cut in half until it reaches +/- 1, so logn recursions
# If n is odd, 1 is subtracted/added to the n, then n becomes even, so still logn recursions


def pow(x, n):
    if n == 0:
        return 1

    if n == 1:
        return x

    if n == -1:
        return 1/x

    if n % 2 == 0:
        return pow(x*x, n/2)

    if n < 0:
        return pow(x, n+1) / x

    return x * pow(x, n-1)


if __name__ == "__main__":
    print(pow(3,4))
    print(pow(3,5))

    print(pow(3, -4))
    print(pow(3, -3))

    print(pow(-3, 2))
    print(pow(-3, -3))

    print(pow(-3, 3))
    print(pow(-3, -2))
