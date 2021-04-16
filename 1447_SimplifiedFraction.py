"""
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is
less-than-or-equal-to n. The fractions can be in any order.
"""
from math import gcd
from time import time
from typing import List


def greatest_common_divider(x: int, y: int) -> int:
    """
    :param x: a non-negative integer such that x <= y
    :param y: a non-negative integer such that x <= y
    :return: greatest common divider of x and y
    """
    return y if x == 0 else greatest_common_divider(y % x, x)


def simplified_fractions_my(n: int) -> List[str]:
    """
    :param n: denominator <= n
    :return: a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is
    less-than-or-equal-to n
    """
    return [str(i) + '/' + str(j) for j in range(2, n + 1) for i in range(1, j) if greatest_common_divider(i, j) == 1]


def simplified_fractions_math(n: int) -> List[str]:
    """
    :param n: denominator <= n
    :return: a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is
    less-than-or-equal-to n
    """
    return [str(i) + '/' + str(j) for j in range(2, n + 1) for i in range(1, j) if gcd(i, j) == 1]


n_max = 50

for i in range(n_max):
    assert simplified_fractions_math(i) == simplified_fractions_my(i)

start_time = time()
for i in range(n_max):
    simplified_fractions_my(i)
end_time = time()
print("My gcd", end_time - start_time)

start_time = time()
for i in range(n_max):
    simplified_fractions_math(i)
end_time = time()
print("Math gcd", end_time - start_time)
