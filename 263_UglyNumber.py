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


test_cases = [(6, True), (8, True), (14, False), ]
for test_n, expected_output in test_cases:
    assert is_ugly(test_n) is expected_output
