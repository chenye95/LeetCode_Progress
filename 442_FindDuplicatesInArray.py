"""
Given an array of integers, 1 ≤ nums[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.
"""
from typing import List


def find_duplicate(nums: List[int]) -> List[int]:
    """
    Use nums itself to record scan history, position num - 1 records whether we have seen num before

    :param nums: 1 <= nums[i] <= len(nums); elements appear either once or twice
    :return: all elements that appear twice in the array
    """
    duplicates = []
    for num in nums:
        if nums[abs(num) - 1] > 0:
            # change position abs(num) - 1 to negative to record we have seen the number
            nums[abs(num) - 1] *= -1
        else:
            # position abs(num) - 1 is negative, have seen num before
            duplicates.append(abs(num))
    return duplicates


test_cases = [([4, 3, 2, 7, 8, 2, 3, 1], {2, 3}),
              ([3, 11, 8, 16, 4, 15, 4, 17, 14, 14, 6, 6, 2, 8, 3, 12, 15, 20, 20, 5], {4, 14, 6, 8, 3, 15, 20})]
for test_nums, expected_output in test_cases:
    assert set(find_duplicate(nums=test_nums)) == expected_output, test_nums
