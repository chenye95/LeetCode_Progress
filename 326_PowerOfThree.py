"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.
"""


def is_power_of_three(n: int) -> bool:
    """
    :param n: -2^31 <= n <= 2^31 - 1
    :return: whether n is a power of three i.e. n == 3^x for some integer x
    """
    if n <= 0:
        return False
    while n > 1:
        if n % 3:
            return False
        n //= 3

    return True


test_cases = [(-3, False), (-1, False), (0, False), (1, True), (27, True), (9, True), (45, False), ]
for test_n, expected_output in test_cases:
    assert is_power_of_three(test_n) is expected_output
