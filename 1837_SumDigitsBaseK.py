"""
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base
 k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
"""


def sum_base(n: int, k: int) -> int:
    """
    :param n: a non negative integer in base 10, 1 <= n <= 100
    :param k: 2 <= k <= 10
    :return: sum of digits of n in base 10 (each digit is interpreted as a base 10 number, and sum returned in base 10
    """
    digit_sum = 0
    while n:
        digit_sum += n % k
        n //= k
    return digit_sum


test_cases = [(34, 6, 9), (10, 10, 1), (68, 2, 2), ]
for test_n, test_k, expected_output in test_cases:
    assert sum_base(test_n, test_k) == expected_output
