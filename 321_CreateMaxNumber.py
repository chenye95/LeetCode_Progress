"""
321. Create Maximum Number
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved. Return an array of the k digits.
"""
from typing import List


def max_number(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    """
    :param nums1: list of length m of digits 0-9
    :param nums2: list of length n of digits 0-9
    :param k: length of return list, such that k <= m + n
    :return: maximum number of length k, combining digits from nums1 and nums2 such that relative order of the digits
    from the same list are preserved
    """

    def prep_one_num(nums: List[int], l_digit: int) -> List[int]:
        """
        :return: the largest l_digit number selected out of nums, s.t. the relative order of the digits is preserved
        """
        assert l_digit <= len(nums)
        if l_digit == len(nums):
            return nums

        need_to_drop = len(nums) - l_digit
        output_list = []
        for num in nums:
            while need_to_drop and output_list and output_list[-1] < num:
                output_list.pop()
                need_to_drop -= 1
            output_list.append(num)
        return output_list[:l_digit]

    def merge(a: List[int], b: List[int]) -> List[int]:
        """
        :return: the largest number by combining a and b while preserving relative digits order from the same list
        """
        return [max(a, b).pop(0) for _ in a + b]

    return max(merge(prep_one_num(nums1, i), prep_one_num(nums2, k - i))
               for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))


test_cases = [([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]),
              ([6, 7], [6, 0, 4], 5, [6, 7, 6, 0, 4]),
              ([3, 9], [8, 9], 3, [9, 8, 9]), ]
for test_num_1, test_num_2, test_k, expected_output in test_cases:
    assert max_number(nums1=test_num_1, nums2=test_num_2, k=test_k) == expected_output
