"""
Given an array of integers and an integer k, you need to find the total number of continuous sub arrays whose sum equals
to k.
"""
from typing import List


def sub_array_sum(nums: List[int], k: int) -> int:
    """
    :param nums: array of  integers
    :param k: target to sum up to
    :return: number of pairs (i, j) such that sum(nums[i:j]) == k
    """
    # compute sum(nums[:i]) and count number of times sum_i appears
    sum_count = {0: 1}
    accumulator = 0
    return_count = 0
    for c in nums:
        accumulator += c
        # note when sum(nums[i+1:j]) == k
        # sum(nums[:j]) - sum(nums[:i]) == k
        # i.e. sum(nums[:i]) == sum(nums[:j]) - k
        return_count += sum_count.get(accumulator - k, 0)
        sum_count[accumulator] = sum_count.get(accumulator, 0) + 1
    return return_count


test_cases = [([1, 1, 1], 2, 2),
              ([1, 2, 3], 3, 2),
              ([100, 1, 2, 3, 100, 1, 2, 3, 4], 3, 4),
              ([-27, 125, 209, -84, -222, -137, 112, -76, 200, -139, 200, 61, -215, 121, 318, -128, 121, 216, -132, 165,
                -19, 89, 193, -59, 203, 8, 140, -128, -201, 199, -5, 36, -167, -140, -194, -166, 182, -50, 729, -167,
                -114, -71, 108, -40, -189, 188, -109, 69, -134, 682, 173, -89, -114, -177, 194, -1, 168, -42, -55, -32,
                198, 171, 45, 25, -18, 154, -22, -192, 213, 86, -16], 223, 10),
              ([100, 1, 2, 100, 2, 100, 1, 1, 1, 100, 2], 3, 2), ]
for test_nums, test_k, expected_output in test_cases:
    assert sub_array_sum(nums=test_nums, k=test_k) == expected_output
