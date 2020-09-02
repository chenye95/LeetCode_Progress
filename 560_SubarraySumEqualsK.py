"""
Given an array of integers and an integer k, you need to find the total number of continuous sub arrays whose sum equals
to k.
"""
from typing import List


def sub_array_sum(nums: List[int], k: int) -> int:
    """
    :return: number of pairs (i, j) such that sum(nums[i:j]) == k
    """
    # compute sum(nums[:i]) and count number of times sum_i appears
    sum_count = {0: 1}
    sum_plus_c = 0
    return_count = 0
    for c in nums:
        sum_plus_c += c
        # note when sum(nums[i+1:j]) == k
        # sum(nums[:j]) - sum(nums[:i]) == k
        # i.e. sum(nums[:i]) == sum(nums[:j]) - k
        return_count += sum_count.get(sum_plus_c - k, 0)
        sum_count[sum_plus_c] = sum_count.get(sum_plus_c, 0) + 1
    return return_count


assert sub_array_sum(nums=[1, 1, 1], k=2) == 2
