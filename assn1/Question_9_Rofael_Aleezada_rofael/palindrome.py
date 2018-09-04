import os


def is_palindrome(string):
    # Remove all extraneous characters
    formatted_string = ''.join([c for c in string if c.isalpha()]).lower()

    # Select starting characters for palindrome checking
    a = int(len(formatted_string) / 2)
    b = a
    if len(formatted_string) % 2 == 0:
        b -= 1

    # loop over each character in string
    while a != -1 and b != len(formatted_string):
        if formatted_string[a] != formatted_string[b]:
            # If mismatched characters, then it isn't a palindrome
            return False

        a -= 1
        b += 1

    # If we made it through the loop, we have a palindrome
    return True


if __name__ == "__main__":
    test_case_file = os.path.dirname(os.path.realpath(__file__)) + "/test_cases.txt"
    test_cases = [line.rstrip('\n') for line in open(test_case_file)]

    for case in test_cases:
        print(case, end=' (')
        print(is_palindrome(case), end=')\n')