import os


def is_monotonic(nums):
    # An array of length 1 is always monotonic
    if len(nums) == 1:
        return True

    a = 1
    # Can't know if the array increases or decreases until we find two different numbers in an array
    while nums[a-1] == nums[a]:
        # The array is just multiples of a single number
        if a == len(nums) - 1:
            return True
        a += 1

    if nums[a-1] < nums[a]:
        # All numbers must be less than or equal to the previous
        while a != len(nums):
            if nums[a-1] > nums[a]:
                # If a pair of number breaks this rule, it's not monotonic
                return False
            a += 1
    else:
        # All numbers must be greater than or equal to the previous
        while a != len(nums):
            if nums[a-1] < nums[a]:
                # If a pair of number breaks this rule, it's not monotonic
                return False
            a += 1

    return True


if __name__ == "__main__":
    test_case_file = os.path.dirname(os.path.realpath(__file__)) + "/test_cases.txt"
    test_cases = [line.rstrip('\n').split(' ') for line in open(test_case_file)]

    for case in test_cases:
        case = [int(i) for i in case]
        print(case, end=' ')
        print(is_monotonic(case))
