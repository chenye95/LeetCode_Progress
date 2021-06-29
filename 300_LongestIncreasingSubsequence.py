"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
"""
from bisect import bisect_left
from typing import List


def length_of_LIS_dp_binary_search(nums: List[int]) -> int:
    """
    Dynamic Programming with Binary Search approach; this approach only tells the length of LIS, not LIS itself

    :param nums: unsorted array of integers
    :return: the length of longest increasing subsequence in an unsorted array of integers
    """
    if not nums:
        return 0

    visited, max_len = [nums[0]], 1
    # meant to store the increasing subsequence formed by including the currently encountered element
    for x in nums[1:]:
        if x > visited[-1]:
            max_len += 1
            visited.append(x)
        else:
            visited[bisect_left(visited, x)] = x

    return max_len


def length_of_LIS_dp(nums: List[int]) -> int:
    """
    Dynamic Programming approach， max LIS till the ith element

    :param nums: unsorted array of integers
    :return: the length of longest increasing subsequence in an unsorted array of integers
    """
    if not nums:
        return 0

    dp_memory = [1] * len(nums)  # max LIS till the ith element
    for i in range(1, len(nums)):
        dp_memory[i] = max([dp_j for j, dp_j in enumerate(dp_memory[:i]) if nums[j] < nums[i]] + [0]) + 1

    return max(dp_memory)


def length_of_LIS_recurse(nums: List[int]) -> int:
    """
    Recursion with memorization

    :param nums: unsorted array of integers
    :return: the length of longest increasing subsequence in an unsorted array of integers
    """
    recurse_memory = [[-1] * len(nums) for _ in range(len(nums) + 1)]

    # [prev_taken_index + 1][current_considering_index] stores the max len if the last two indexes are prev_taken_index
    # and current_considering_index

    def recurse_LIS(prev_taken_index: int, current_considering_index: int) -> int:
        if current_considering_index == len(nums):
            return 0

        if recurse_memory[prev_taken_index + 1][current_considering_index] < 0:
            take_index = 0 if prev_taken_index >= 0 and nums[current_considering_index] <= nums[prev_taken_index] \
                else 1 + recurse_LIS(current_considering_index, current_considering_index + 1)
            not_take_index = recurse_LIS(prev_taken_index, current_considering_index + 1)
            recurse_memory[prev_taken_index + 1][current_considering_index] = max(take_index, not_take_index)

        return recurse_memory[prev_taken_index + 1][current_considering_index]

    return recurse_LIS(-1, 0)


test_cases = [([10, 9, 2, 5, 3, 7, 101, 18], 4),
              ([0], 1),
              (list(range(1, 2501)), 2500), ]
for length_of_LIS in [length_of_LIS_dp, length_of_LIS_dp_binary_search]:
    for test_nums, expected_value in test_cases:
        assert length_of_LIS(test_nums) == expected_value, length_of_LIS.__name__
for length_of_LIS in [length_of_LIS_recurse]:
    for test_nums, expected_value in test_cases[:-1]:
        assert length_of_LIS(test_nums) == expected_value, length_of_LIS.__name__
