"""
Given an integer, write a function to determine if it is a power of two.
"""


def is_power_of_two(n: int) -> bool:
    """
    :return: if n is a power of two
    """
    return n > 0 and not (n & (n - 1))


two_powers = {2 ** i for i in range(15)}
for i in range(32_000):
    assert is_power_of_two(i) is (i in two_powers), i
