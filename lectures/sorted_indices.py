def binary_search(arr, num, a, b):
    if a > b or (a == b and arr[a] != num):
        return -1

    mid = int((a + b) / 2)
    if arr[mid] == num:
        return mid

    if arr[mid] > num:
        return binary_search(arr, num, a, mid - 1)

    return binary_search(arr, num, mid + 1, b)


def sorted_indices(arr, num):
    index = binary_search(arr, num, 0, len(arr) - 1)

    left, right = index, index
    temp_left, temp_right = index, index

    while temp_left != -1:
        # Look for earliest occurance of value in [0, index - 1]
        left = temp_left
        temp_left = binary_search(arr, num, 0, temp_left - 1)

    while temp_right != -1:
        # Look for latest occurance of value in [index + 1, len - 1]
        right = temp_right
        temp_right = binary_search(arr, num, temp_right + 1, len(arr) - 1)

    return [left, right]


print(sorted_indices([0,0,1,5,5,5,5,5,5,5,5,8,100,1001], 5))