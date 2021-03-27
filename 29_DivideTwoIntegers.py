"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example,
truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""


def divide(dividend: int, divisor: int) -> int:
    """
    Implementation of division without *, / or mod.
    Subtract 2^n * abs(divisor) from abs(dividend) until abs(dividend) < abs(divisor)

    :return: return quotient from dividend / divisor. Round to zero
    """
    is_negative = (dividend > 0) is not (divisor > 0)
    remainder, divisor = abs(dividend), abs(divisor)
    return_result = 0

    while remainder >= divisor:
        tmp, i = divisor, 1
        while remainder >= tmp:
            i <<= 1
            tmp <<= 1
        return_result += (i >> 1)
        remainder -= (tmp >> 1)

    if is_negative:
        return_result = -return_result

    return min(max(-2 ** 31, return_result), 2 ** 31 - 1)


test_cases = [(5891, 2, 2945),
              (10, 3, 3),
              (7, -3, -2),
              (0, 1, 0),
              (1, 1, 1), ]
for test_dividend, test_divisor, expected_output in test_cases:
    assert divide(dividend=test_dividend, divisor=test_divisor) == expected_output
