"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


def is_palindrome(x: int) -> bool:
    """
    palindrome cannot be negative, nor start with leading 0

    :return: if x is a palindrome
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        # negative x is not palindrome
        return False

    reversed_number = 0
    while x > reversed_number:
        reversed_number = reversed_number * 10 + x % 10
        x //= 10

    return x == reversed_number or x == reversed_number // 10


test_cases = [(121, True), (-121, False), (10, False), (-101, False), (101, True), ]
for test_input, expected_output in test_cases:
    assert is_palindrome(x=test_input) is expected_output
