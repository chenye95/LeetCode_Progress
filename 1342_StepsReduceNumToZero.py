"""
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you
have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


def number_of_steps(num: int) -> int:
    """
    :param num: 0 <= num <= 10^6; if current number is even, divide by 2, otherwise subtract by 1
    :return: number of steps to reduce it to zero
    """
    step_count = 0
    while num:
        step_count += 1
        if num % 2:
            num -= 1
        else:
            num /= 2
    return step_count


test_cases = [(14, 6), (8, 4), (123, 12), ]
for test_num, expected_output in test_cases:
    assert number_of_steps(test_num) == expected_output
