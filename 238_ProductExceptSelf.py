"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    left_product, right_product = [0] * n, [0] * n

    left_product[0] = 1
    right_product[-1] = 1
    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]
        right_product[n - 1 - i] = right_product[n - i] * nums[n - i]

    result = [0] * n
    for i in range(n):
        result[i] = left_product[i] * right_product[i]
    return result


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
