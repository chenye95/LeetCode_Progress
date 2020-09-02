"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) sub arrays where the product of all the elements in the sub array is less
than k.
"""
from typing import List


def num_sub_array_product_less_than_k(nums: List[int], k: int) -> int:
    """
    :param nums: 0 < nums[i] < 1000
    :param k: 0 <= k < 10^6
    :return: number of pairs (i,j) such that product(nums[i:j]) < k
    """
    if k <= 1:
        # nums[i] > 0
        return 0
    cumulative_prod = 1
    return_ans = left_pointer = 0
    for right_pointer, num_right_pointer in enumerate(nums):
        cumulative_prod *= num_right_pointer
        while cumulative_prod >= k:
            cumulative_prod /= nums[left_pointer]
            left_pointer += 1
        return_ans += (right_pointer - left_pointer + 1)
    return return_ans


assert num_sub_array_product_less_than_k(nums=[10, 5, 2, 6], k=100) == 8
