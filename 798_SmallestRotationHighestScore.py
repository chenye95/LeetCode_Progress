"""
Given an array nums, we may rotate it by a non-negative integer K so that the array becomes nums[K], nums[K+1],
nums{K+2], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[K-1].  Afterward, any entries that are less than or
equal to their index are worth 1 point.

For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points
because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If
there are multiple answers, return the smallest such index K.
"""
from typing import List


def bestRotation(nums: List[int]) -> int:
    """
    Interval Stabbing Approach
    :param nums: array of integers
    :return: index k that yields that highest score post rotation
    """
    n = len(nums)
    interval_overlap = [0] * n
    for i, a in enumerate(nums):
        # Calculate the interval of rotation steps for which nums[i] = a will not score point
        # left inclusive, right exclusive
        interval_left, interval_right = (i - a + 1) % n, (i + 1) % n
        interval_overlap[interval_left] -= 1
        interval_overlap[interval_right] += 1

        if interval_left > interval_right:
            # loop around then break into two intervals
            interval_overlap[0] -= 1
            # doesn't have to keep track of interval_overlap[n]

    smallest_overlap = -n
    rotation_steps = current_overlap = 0
    for i, score in enumerate(interval_overlap):
        current_overlap += score
        if current_overlap > smallest_overlap:
            smallest_overlap = current_overlap
            rotation_steps = i

    return rotation_steps


test_cases = [([2, 3, 1, 4, 0], 3)]
for input, expected_value in test_cases:
    assert bestRotation(input) == expected_value, "Expected %d Got %d" % (expected_value, bestRotation(input))
