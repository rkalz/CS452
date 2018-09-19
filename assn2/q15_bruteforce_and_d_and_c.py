import os


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


def _binary_search(arr, val, a, b):
    if a > b:
        return -1

    if a == b and arr[a] == val:
        return a

    mid = int((a + b) / 2)
    mid_val = arr[mid]

    if mid_val == val:
        return mid

    if mid_val > val:
        return _binary_search(arr, val, a, mid - 1)

    return _binary_search(arr, val, mid + 1, b)


def divide_conquer_find_inversions(arr):
    return _merge_sort(arr, 0, len(arr)-1)



if __name__ == "__main__":
    arr = [9,5,2,4,3,6,0]
    print(brute_force_find_inversions(arr))
    print(divide_conquer_find_inversions(arr))
