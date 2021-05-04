"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].
"""
from typing import List


def product_except_self_product(nums: List[int]) -> List[int]:
    """
    :param nums: array of n integers
    :return: output[i] is equal to the product of all the elements of nums except nums[i]
    """
    n = len(nums)
    left_product, right_product = [1] * n, [1] * n

    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]
        right_product[n - 1 - i] = right_product[n - i] * nums[n - i]

    return [left_product[i] * right_product[i] for i in range(n)]


def product_except_self_division(nums: List[int]) -> List[int]:
    """
    :param nums: array of n integers
    :return: output[i] is equal to the product of all the elements of nums except nums[i]
    """

    def get_product_non_zero():
        all_product = 1
        for num_i in nums:
            if num_i != 0:
                all_product *= num_i
        return all_product

    zero_count = sum(num_i == 0 for num_i in nums)
    if zero_count >= 2:
        return [0] * len(nums)
    if zero_count == 1:
        return_val = [0] * len(nums)
        return_val[nums.index(0)] = get_product_non_zero()
        return return_val
    else:
        product_all = get_product_non_zero()
        return [product_all // num_i for num_i in nums]


test_cases = [([1, 2, 3, 4], [24, 12, 8, 6]),
              ([3, 8, 4, 5, 9], [1440, 540, 1080, 864, 480]),
              ([2, 4, -2, 1, 2, -1, 4, 1, 3, -3, -1, 2, 1, 2, 1, -3, 1, -1, 1, 3, 3, -2, -2, 3, -3, -1, 1, -2, -4, -2],
               [-35831808, -17915904, 35831808, -71663616, -35831808, 71663616, -17915904, -71663616, -23887872,
                23887872, 71663616, -35831808, -71663616, -35831808, -71663616, 23887872, -71663616, 71663616,
                -71663616, -23887872, -23887872, 35831808, 35831808, -23887872, 23887872, 71663616, -71663616, 35831808,
                17915904, 35831808]), ]
for product_except_self in [product_except_self_product, product_except_self_division, ]:
    for test_nums, expected_output in test_cases:
        assert product_except_self(nums=test_nums) == expected_output, product_except_self.__name__
