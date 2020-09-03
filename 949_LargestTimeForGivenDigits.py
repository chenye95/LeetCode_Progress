"""
Given an array of 4 four_digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has
elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
"""
from itertools import permutations
from typing import List


def largest_time_from_digits(four_digits: List[int]) -> str:
    """
    :param four_digits: list of 4 four_digits
    :return: largest time that can be composed from the 4 four_digits
    """
    for time in permutations(sorted(four_digits, reverse=True)):
        if time[:2] < (2, 4) and time[2] < 6:
            return "%d%d:%d%d" % time
    return ""


def my_largest_time_from_digits(four_digits: List[int]) -> str:
    """
    Custom implementation of permutation
    """

    def build_time(proposal_time: List[int]) -> int:
        """
        :return: number of minutes if proposal_time is a valid timestamp, or else -1
        """
        if proposal_time[:2] < [2, 4] and proposal_time[2] < 6:
            return 60 * (10 * proposal_time[0] + proposal_time[1]) + (10 * proposal_time[2] + proposal_time[3])
        else:
            return -1

    def permute(ref_digits: List[int], start_index: int):
        nonlocal max_time

        if start_index == len(ref_digits):
            max_time = max(max_time, build_time(ref_digits))
            return

        for swap_index in range(start_index, len(ref_digits)):
            if swap_index > start_index:
                ref_digits[start_index], ref_digits[swap_index] = ref_digits[swap_index], ref_digits[start_index]
            permute(ref_digits, start_index + 1)
            if swap_index > start_index:
                ref_digits[start_index], ref_digits[swap_index] = ref_digits[swap_index], ref_digits[start_index]

    max_time = -1
    permute(four_digits, 0)
    if max_time == -1:
        return ""
    else:
        return "{:2d}:{:2d}".format(max_time // 60, max_time % 60)


test_cases = [([1, 2, 3, 4], "23:41"),
              ([5, 5, 5, 5], ""),
              ([2, 3, 5, 9], "23:59"),
              ([1, 2, 5, 8], "21:58"),
              ([2, 4, 6, 0], "20:46"),
              ([2, 4, 6, 5], "")]
for test_function in [largest_time_from_digits, my_largest_time_from_digits]:
    for test_input, expected_output in test_cases:
        assert test_function(test_input) == expected_output
