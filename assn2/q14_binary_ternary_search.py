import os
from timeit import default_timer as timer

import matplotlib.pyplot as plt

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

    if first_mid_val < val < second_mid_val:
        return ternary_search(arr, val, first_mid + 1, second_mid - 1)

    return ternary_search(arr, val, second_mid + 1, b)

    pass


if __name__ == "__main__":
    number_file_path = os.path.dirname(os.path.realpath(__file__)) + "/100000"
    numbers = [int(i) for i in open(number_file_path).read().split()]
    test_cases = [1, 56, 100, 769, 950, 952, 1200, 1505, 4349, 52028, 2712892, 9999616, 4369620, 4369621, 2421119,
                  2421120, 7336918, 7788346, 7336919, 9235296, 9235299, 10000000]
    test_cases.sort()
    numbers_length = len(numbers)

    binary_search_times = []
    ternary_search_times = []
    repeats = 10000

    for case in test_cases:
        bst = 0
        tst = 0
        print(str(case))

        for _ in range(repeats):
            start = timer()
            binary_search(numbers, case, 0, numbers_length-1)
            end = timer()
            bst += end-start

            start = timer()
            ternary_search(numbers, case, 0, numbers_length-1)
            end = timer()
            tst += end-start

        bst = bst / repeats
        tst = tst / repeats
        binary_search_times.append(bst)
        ternary_search_times.append(tst)
        print("Binary Search: " + str(bst))
        print("Ternary Search: " + str(tst))
        print()

    x = range(len(test_cases))
    bst_graph, = plt.plot(x, binary_search_times, 'ro')
    tst_graph, = plt.plot(x, ternary_search_times, 'bo')
    plt.xlabel("Test Case in Sorted Order")
    plt.ylabel("Time Taken (sec)")
    plt.legend([bst_graph, tst_graph], ["Binary Search Times", "Ternary Search Times"])
    plt.show()

