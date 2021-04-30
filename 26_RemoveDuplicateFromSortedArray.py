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
              ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
              ([-50, -50, -49, -48, -47, -47, -47, -46, -45, -43, -42, -41, -40, -40, -40, -40, -40, -40, -39, -38, -38,
                -38, -38, -37, -36, -35, -34, -34, -34, -33, -32, -31, -30, -28, -27, -26, -26, -26, -25, -25, -24, -24,
                -24, -22, -22, -21, -21, -21, -21, -21, -20, -19, -18, -18, -18, -17, -17, -17, -17, -17, -16, -16, -15,
                -14, -14, -14, -13, -13, -12, -12, -10, -10, -9, -8, -8, -7, -7, -6, -5, -4, -4, -4, -3, -1, 1, 2, 2, 3,
                4, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 13, 13, 14, 14, 14, 15, 16, 17, 17, 18, 20,
                21, 22, 22, 22, 23, 23, 25, 26, 28, 29, 29, 29, 30, 31, 31, 32, 33, 34, 34, 34, 36, 36, 37, 37, 38, 38,
                38, 39, 40, 40, 40, 41, 42, 42, 43, 43, 44, 44, 45, 45, 45, 46, 47, 47, 47, 47, 48, 49, 49, 49, 50],
               [-50, -49, -48, -47, -46, -45, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -28,
                -27, -26, -25, -24, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -10, -9, -8, -7, -6, -5, -4,
                -3, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 25, 26, 28, 29,
                30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), ]
for test_input, expected_output in test_cases:
    assert remove_duplicates(nums=test_input) == len(expected_output)
    assert sorted(test_input[:len(expected_output)]) == expected_output
