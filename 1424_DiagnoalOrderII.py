"""
Given a list of lists of integers, nums, return all elements of nums in diagonal order from bottom left to top right
"""
from typing import List


def find_diagonal_order(nums: List[List[int]]) -> List[int]:
    """
    :return: diagonal order, from left bottom to top right, of int in nums
    """
    list_int_by_i_plus_j = []
    for i, row_i in enumerate(nums):
        for j, a_i_j in enumerate(row_i):
            if len(list_int_by_i_plus_j) <= i + j:
                list_int_by_i_plus_j.append([])
            list_int_by_i_plus_j[i + j].append(a_i_j)
    # List in increasing order of i + j
    # List within l_i_j reverse order of i
    return [a_i_j for l_i_j in list_int_by_i_plus_j for a_i_j in l_i_j[::-1]]


test_cases = [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 4, 2, 7, 5, 3, 8, 6, 9]),
              ([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
               [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]),
              ([[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]], [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]),
              ([[1, 2, 3, 4, 5, 6]], [1, 2, 3, 4, 5, 6]),
              ([[6], [8], [6, 1, 6, 16]], [6, 8, 6, 1, 6, 16]), ]
for test_nums, expected_output in test_cases:
    assert find_diagonal_order(test_nums) == expected_output
