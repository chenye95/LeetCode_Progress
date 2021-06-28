"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""
from functools import cache
from typing import List


def find_max_form(str_list: List[str], m: int, n: int) -> int:
    """
    :param str_list: array of binary strings
    :param m: at most m 0's in the subset
    :param n: at most n 1's in the subset
    :return: largest subset of str_list with at most m 0's and n 1's in the subset
    """
    binary_count = [(s.count('0'), s.count('1')) for s in str_list]

    @cache
    def depth_first_search(zero_remainder: int, one_remainder: int, str_k: int) -> int:
        """
        Sub-problem, find the largest subset from str_list[str_k:] with zero_remainder 0's and one_remainder 1's

        :param zero_remainder: at most zero_remainder 0's in the sub problem
        :param one_remainder: at most one_remainder 1's in the sub problem
        :param str_k: evaluating whether to take str_list[str_k] or not
        :return: largest subset in the sub problem
        """
        if zero_remainder < 0 or one_remainder < 0:
            return -len(str_list)
        if str_k == len(str_list):
            return 0
        zero_count, one_count = binary_count[str_k]
        return max(1 + depth_first_search(zero_remainder - zero_count, one_remainder - one_count, str_k + 1),
                   depth_first_search(zero_remainder, one_remainder, str_k + 1))

    return depth_first_search(m, n, 0)


test_cases = [(["10", "0001", "111001", "1", "0"], 5, 3, 4),
              (["10", "0", "1"], 1, 1, 2),
              (["0", "0", "1", "1", "1", "0", "1", "0", "0", "1", "1", "0", "1", "0", "1", "0", "1", "0", "0", "1", "0",
                "1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0",
                "1", "0", "0", "1", "0", "0", "1", "1", "1", "1", "1", "0", "0", "1", "0", "1", "0", "1", "1", "0", "0",
                "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "0", "1", "1", "0", "1",
                "0", "0", "1"], 93, 91, 87),
              (["1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1",
                "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0",
                "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1",
                "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0",
                "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1",
                "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0",
                "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1",
                "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0",
                "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1",
                "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0",
                "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0"], 30, 30, 60), ]
for test_list, test_m, test_n, expected_output in test_cases:
    assert find_max_form(str_list=test_list, m=test_m, n=test_n) == expected_output
