"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


def reverse(x: int) -> int:
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


assert reverse(x=123) == 321
assert reverse(x=-123) == -321
assert reverse(x=120) == 21
assert reverse(x=0) == 0
assert reverse(x=1534236469) == 0
