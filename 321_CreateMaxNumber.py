"""
321. Create Maximum Number
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved. Return an array of the k digits.
"""
from typing import List

def maxNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    def prep_one_num(nums: List[int], k_digit: int) -> List[int]:
        """
        :return: the largest k_digit number selected out of nums, s.t. the relative order of the digits is preserved
        """
        assert k_digit <= len(nums)
        if k_digit == len(nums):
            return nums

        need_to_drop = len(nums) - k_digit
        output_list = []
        for num in nums:
            while need_to_drop and output_list and output_list[-1] < num:
                output_list.pop()
                need_to_drop -= 1
            output_list.append(num)
        return output_list[:k_digit]

    def merge(a: List[int], b: List[int]) -> List[int]:
        return [max(a, b).pop(0) for _ in a + b]

    return max(merge(prep_one_num(nums1, i), prep_one_num(nums2, k-i))
               for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

assert maxNumber(nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5) == [9, 8, 6, 5, 3]
assert maxNumber(nums1 = [6, 7], nums2 = [6, 0, 4], k = 5) == [6, 7, 6, 0, 4]
assert maxNumber(nums1 = [3, 9], nums2 = [8, 9], k = 3) == [9, 8, 9]
