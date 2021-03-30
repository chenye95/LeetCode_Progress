"""
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and
 negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two
 elements is trivially a wiggle sequence.
    * For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately
    positive and negative.
    * In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two
    differences are positive and the second because its last difference is zero.

A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the
remaining elements in their original order.
"""
from typing import List


def wiggle_max_length_dp(nums: List[int]) -> int:
    """
    Dynamic Programming approach

    :return: max length of wiggle subsequences in nums
    """
    if len(nums) < 2:
        return len(nums)

    up_len = 1  # length of wiggle if the subsequence ends wiggling up
    down_len = 1  # length of wiggle if the subsequence ends wiggling down
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up_len = down_len + 1
            # down_len = down_len
        elif nums[i] < nums[i - 1]:
            down_len = up_len + 1
            # up_len = up_len
        # else:
            # up_len = up_len
            # down_len = down_len

    return max(up_len, down_len)


def wiggle_max_length_greedy(nums: List[int]) -> int:
    """
    equivalent to finding number of local max and local min in the array
    - if we choose any other intermediate number to be a part of the current wiggle subsequence, the maximum length of
    that wiggle subsequence will always be less than or equal to the one obtained by choosing only the consecutive max
    and min elements.

    :return: number of local max and local min in the array + 1
    """
    if len(nums) < 2:
        return len(nums)

    prev_trend = nums[1] - nums[0]
    peak_count = 2 if prev_trend != 0 else 1

    for i in range(2, len(nums)):
        current_trend = nums[i] - nums[i - 1]
        if prev_trend <= 0 < current_trend or current_trend < 0 <= prev_trend:
            peak_count += 1
            prev_trend = current_trend

    return peak_count


test_cases = [([1, 7, 4, 9, 2, 5], 6),
              ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
              ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
              ]
for wiggle_max_length in [wiggle_max_length_dp, wiggle_max_length_greedy]:
    for test_input, expected_output in test_cases:
        assert wiggle_max_length(test_input) == expected_output
