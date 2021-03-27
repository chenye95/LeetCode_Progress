"""
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
 endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""


def is_happy_number(n: int) -> bool:
    """
    :return: whether the number n is a happy number
    """
    appeared = set()
    current_number = n
    while current_number not in appeared:
        appeared.add(current_number)
        next_number = 0
        while current_number > 0:
            current_digit = current_number % 10
            current_number = current_number // 10
            next_number += current_digit ** 2
        if next_number == 1:
            return True
        current_number = next_number
    return False


test_cases = [(19, True), (2, False), ]
for test_n, expected_output in test_cases:
    assert is_happy_number(test_n) is expected_output
