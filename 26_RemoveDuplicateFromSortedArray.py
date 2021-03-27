"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new
length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates in place for a sorted integer list

    :param nums: sorted integer list
    :return: new length after de-duplication
    """
    if not nums:
        return 0

    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            if i != j:
                nums[i] = nums[j]
    return i + 1


test_cases = [([1, 1, 2], [1, 2]),
              ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])]
for test_input, expected_output in test_cases:
    assert remove_duplicates(nums=test_input) == len(expected_output)
    assert sorted(test_input[:len(expected_output)]) == expected_output
