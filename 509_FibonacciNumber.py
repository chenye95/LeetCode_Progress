"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,
- F(0) = 0,   F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n > 1.
"""


def fibonacci(n: int) -> int:
    """
    :param n: F(n) = F(n - 1) + F(n - 2)
    :return: n_th value in the Fibonacci list
    """
    if n <= 1:
        return n
    two_number = 0
    one_number = current_number = 1
    for i in range(1, n):
        current_number = two_number + one_number
        two_number = one_number
        one_number = current_number
    return current_number


test_cases = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), ]
for test_n, expected_output in test_cases:
    assert fibonacci(n=test_n) == expected_output
