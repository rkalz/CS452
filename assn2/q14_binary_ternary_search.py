import os

# Binary search - log2(n)
# Ternary search - log3(n) = log2(n)/log2(3) ~ 0.637log2(n) -> log2(n)


def binary_search(arr, val, a, b):
    if a > b or (a == b and arr[a] != val):
        return False

    mid = int((a + b) / 2)
    mid_val = arr[mid]

    if mid_val == val:
        return True

    if mid_val > val:
        return binary_search(arr, val, a, mid - 1)

    return binary_search(arr, val, mid + 1, b)

    pass


def ternary_search(arr, val, a, b):

    if a > b or (a == b and arr[a] != val):
        return False

    gap = int((b - a + 1) / 3)
    first_mid = a + gap
    first_mid_val = arr[first_mid]
    second_mid = first_mid + gap
    second_mid_val = arr[second_mid]

    if first_mid_val == val or second_mid_val == val:
        return True

    if val < first_mid_val:
        return ternary_search(arr, val, a, first_mid - 1)

    if val > first_mid_val and val < second_mid_val:
        return ternary_search(arr, val, first_mid + 1, second_mid - 1)

    return ternary_search(arr, val, second_mid + 1, b)

    pass


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    print(ternary_search(arr, 16, 0, len(arr)-1))