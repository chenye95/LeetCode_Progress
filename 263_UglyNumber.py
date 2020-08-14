"""
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""


def is_ugly(num: int) -> bool:
    """
    :param num: positive numbers
    :return: whether the positive numbers have prime factors only include 2, 3, 5
    """
    factors = [2, 3, 5]
    if num <= 0:
        return False
    for factor_i in factors:
        while num % factor_i == 0:
            num = num // factor_i
    return num == 1


assert is_ugly(6)
assert is_ugly(8)
assert not is_ugly(14)
