"""
Given a list of non negative integers, arrange them such that they form the largest number.
"""
from typing import List


class LargestNumberKey(str):
    def __lt__(self: str, other: str):
        return self + other > other + self


def largest_number(nums: List[int]) -> str:
    """
    :param nums: list of non-negative integers
    :return: string representation of the number
    """
    return_largest_number = ''.join(sorted(map(str, nums), key=LargestNumberKey))
    return '0' if return_largest_number[0] == '0' else return_largest_number


test_cases = [([10, 2], "210"),
              ([3, 30, 34, 5, 9], "9534330"), ]
for test_nums, expected_output in test_cases:
    assert largest_number(nums=test_nums) == expected_output
