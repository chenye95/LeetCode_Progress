"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
"""


def reverse(x: int) -> int:
    """
    :param x: a signed 32 bits integer
    :return: x with its digits reversed. If return result go outside bound of a signed 32 bit int, return 0
    """
    if x == 0:
        return 0
    return_result = 0
    sign, x = (1, x) if x > 0 else (-1, -x)
    while x:
        return_result = return_result * 10 + (x % 10)
        x //= 10
    return_result *= sign
    if return_result < -(1 << 31) or return_result >= (1 << 31):
        return 0
    else:
        return return_result


test_cases = [(123, 321),
              (-123, -321),
              (120, 21),
              (0, 0),
              (1534236469, 0), ]
for test_x, expected_output in test_cases:
    assert reverse(x=test_x) == expected_output
