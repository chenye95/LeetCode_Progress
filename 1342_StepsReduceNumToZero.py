"""
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you
have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


def number_of_steps(num: int) -> int:
    """
    :param num: 0 <= num <= 10^6
    """
    step_count = 0
    while num:
        step_count += 1
        if num % 2:
            num -= 1
        else:
            num /= 2
    return step_count


assert number_of_steps(num=14) == 6
assert number_of_steps(num=8) == 4
assert number_of_steps(num=123) == 12
