# python3 q15_bruteforce_and_d_and_c.py
# Data files should be in the same directory as the python file

import os
from math import log10
from timeit import default_timer as timer

import matplotlib.pyplot as plt


def brute_force_find_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # i is always less than j
            if arr[i] > arr[j]:
                count += 1

    return count


def _merge(arr, a, m, b):
    left_half_pos = a
    right_half_pos = m+1
    copy = (b - a + 1) * [0]
    cur_pos = 0
    inversions = 0

    while left_half_pos <= m and right_half_pos <= b:
        if arr[left_half_pos] <= arr[right_half_pos]:
            copy[cur_pos] = arr[left_half_pos]
            left_half_pos += 1
        else:
            copy[cur_pos] = arr[right_half_pos]
            right_half_pos += 1

            # The number of inversions is equal to the amount of values from
            # arr[left_hand_pos] to arr[m]
            inversions += m - left_half_pos + 1
        cur_pos += 1

    while left_half_pos <= m:
        copy[cur_pos] = arr[left_half_pos]
        left_half_pos += 1
        cur_pos += 1

    while right_half_pos <= b:
        copy[cur_pos] = arr[right_half_pos]
        right_half_pos += 1
        cur_pos += 1

    for i in range(a, b + 1):
        arr[i] = copy[i - a]

    return inversions


def _merge_sort(arr, a, b):
    inversions = 0
    if a < b:
        mid = int((a + b) / 2)
        inversions += _merge_sort(arr, a, mid)
        inversions += _merge_sort(arr, mid + 1, b)
        inversions += _merge(arr, a, mid, b)

    return inversions


def divide_conquer_find_inversions(arr):
    return _merge_sort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    files_path = os.path.dirname(os.path.realpath(__file__)) + "/"
    test_files = ["10", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500", "1000", "5000"]

    brute_force_times = []
    divide_and_conquer_times = []
    repeats = 1

    for size in test_files:
        print(size)
        numbers = [int(i) for i in open(files_path + size).read().split()]
        bft = 0
        dct = 0

        for _ in range(repeats):
            start = timer()
            brute_force_find_inversions(numbers)
            end = timer()
            bft += end - start

            start = timer()
            divide_conquer_find_inversions(numbers)
            end = timer()
            dct += end - start

        bft = bft / repeats
        dct = dct / repeats

        brute_force_times.append(bft)
        divide_and_conquer_times.append(dct)

    x = [log10(int(i)) for i in test_files]
    bft_graph, = plt.plot(x, brute_force_times, 'ro')
    dct_graph, = plt.plot(x, divide_and_conquer_times, 'bo')
    plt.xlabel("Length of Array")
    plt.ylabel("Time Taken (sec)")
    plt.legend([bft_graph, dct_graph], ["Brute Force Times", "Divide and Conquer Times"])
    plt.show()



