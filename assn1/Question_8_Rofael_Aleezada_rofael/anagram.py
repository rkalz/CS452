import os


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        # Can't be an anagram if the strings are different lengths
        return False

    for i in range(len(s1)):
        if s1[i] != s2[len(s1) - 1 - i]:
            # Compare nth character with len-n-1th character
            # If there is a difference, return False
            return False

    return True


if __name__ == "__main__":
    test_case_file = os.path.dirname(os.path.realpath(__file__)) + "/test_cases.txt"
    test_cases = [line.rstrip('\n').split(' ') for line in open(test_case_file)]

    for case in test_cases:
        print(case[0], end=' ')
        print(case[1], end=' ')
        print(is_anagram(case[0], case[1]))
