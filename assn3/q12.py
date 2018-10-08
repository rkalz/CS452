# python3 q12.py
# Data files should be in the same directory as the python file

import os
from math import log10
from timeit import default_timer as timer

import matplotlib.pyplot as plt


def brute_force_median(arr):
    arr_copy = arr.copy()
    arr_copy.sort()
    mid = int(len(arr_copy)/2)
    return arr_copy[mid]


def _split(arr, pivot):
    l = []
    r = []

    for num in arr:
        if num != pivot:
            if num < pivot:
                l.append(num)
            else:
                r.append(num)

    return l, r


def _chunk(arr):
    chunks = []
    for i in range(0, len(arr), 5):
        chunks.append(arr[i:i+5])
    return chunks


def _find_kth(arr, k):
    if len(arr) < 5:
        return arr[k]

    chunks = _chunk(arr)
    medians = []
    for chunk in chunks:
        medians.append(brute_force_median(chunk))

    pivot = _find_kth(medians, int(len(medians)/2))
    l, r = _split(arr, pivot)

    if k == len(l):
        return pivot
    if k <= len(l) - 1:
        return _find_kth(l, k)
    return _find_kth(r, k - len(l) - 1)


def linear_time_median(arr):
    return _find_kth(arr, int(len(arr)/2))


if __name__ == "__main__":
    files_path = os.path.dirname(os.path.realpath(__file__)) + "/"
    test_files = ["10", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500", "1000", "5000", "10000"]

    brute_force_times = []
    linear_times = []
    repeats = 1

    for size in test_files:
        print(size)
        numbers = [int(i) for i in open(files_path + size).read().split()]
        lin_time = 0
        bf_time = 0

        for _ in range(repeats):
            start = timer()
            result = brute_force_median(numbers)
            end = timer()
            print(result)
            bf_time += end - start

            start = timer()
            result = linear_time_median(numbers)
            end = timer()
            print(result)
            lin_time += end - start

            print()

        lin_time = lin_time / repeats
        bf_time = bf_time / repeats

        linear_times.append(lin_time)
        brute_force_times.append(bf_time)

    x = [log10(int(i)) for i in test_files]
    lin_graph, = plt.plot(x, brute_force_times, 'ro')
    bft_graph, = plt.plot(x, linear_times, 'bo')
    plt.xlabel("Length of Array")
    plt.ylabel("Time Taken (sec)")
    plt.legend([lin_graph, bft_graph], ["Linear Times", "Brute Force Times"])
    plt.show()

