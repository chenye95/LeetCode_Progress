"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are
asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
"""
from typing import List


def burst_balloons(nums: List[int]) -> int:
    """
    When you burst balloon i, you get nums[left] * nums[i] * nums[right] coins, where left and right are balloons
    adjacent to i at i's bursting

    :param nums: coins in balloon i
    :return: maximum number of coins you can collect by bursting the balloons sequentially
    """
    # Drop all 0s in nums as this will not change final results
    # Extend both ends by 1
    nums = [1] + list(filter(lambda x: x > 0, nums)) + [1]
    n = len(nums)
    # Record the biggest number from nums[i], ..., nums[j] when all balloons inside the range are dropped off,
    # and nums[i] and nums[j] stay
    # dp_memory[0][-1] stores the final result, as nums[0] and nums[-1] are filler 1 and don't need to be dropped
    dp_memory = [[0] * n for _ in range(n)]

    # Scan (i, j) pair by window size j - i
    for window_size in range(2, n):
        for window_start in range(n - window_size):
            window_end = window_start + window_size
            window_multiplier = nums[window_start] * nums[window_end]
            # burst in way such that the last three remaining items in the group are nums[window_start],
            # nums[window_end] and nums[window_mid], and then burst nums[window_mid]
            dp_memory[window_start][window_end] = max(dp_memory[window_start][window_mid] +
                                                      dp_memory[window_mid][window_end] +
                                                      window_multiplier * nums[window_mid]
                                                      for window_mid in range(window_start + 1, window_end))
    return dp_memory[0][-1]


test_cases = [([3, 1, 5, 8], 167),
              ([1, 5], 10),
              ([7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3], 1654),
              ([54, 88, 26, 48, 9, 32, 0, 66, 4, 82, 66, 7, 28, 23, 73, 99, 44, 27, 16, 29, 52, 66, 30, 97, 41, 33, 60,
                62, 45, 40, 19, 35, 97, 69, 19, 60, 2, 48, 81, 66, 45, 86, 51, 51, 47, 97, 5, 59, 54, 98, 79, 90, 70,
                70, 62, 16, 96, 95, 97, 77, 21, 35, 10, 90, 14, 31, 21, 29, 40, 81, 33, 64, 91, 44, 81, 85, 77, 9, 67,
                58, 77, 88, 69, 76, 89, 33, 36, 87, 85, 77, 94, 96, 37, 61, 23, 75, 15, 29, 21, 88, 91], 39731870),
              ([9, 76], 760),
              ]
for test_nums, expected_coins in test_cases:
    assert burst_balloons(nums=test_nums) == expected_coins
