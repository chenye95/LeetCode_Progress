"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of
[1,2,3,4,5] while [1,5,3] is not).
"""
from typing import List


def max_dot_product(nums1: List[int], nums2: List[int]) -> int:
    """
    Dynamic Programming approach, loop through nums[:i] and find dot product against sub sequence of nums2

    :return: maximum dot product between non-empty subsequences of nums1 and nums2 of the same length
    """
    m, n = len(nums1), len(nums2)
    previous_iterations = [0] * n
    for i in range(m):
        current_iterations = [0] * n
        for j in range(n):
            current_iterations[j] = nums1[i] * nums2[j]  # Avoid empty subsequences
            if i and j:
                current_iterations[j] += max(previous_iterations[j - 1], 0)
            if i:
                current_iterations[j] = max(current_iterations[j], previous_iterations[j])
            if j:
                current_iterations[j] = max(current_iterations[j], current_iterations[j - 1])
        previous_iterations = current_iterations
    return previous_iterations[-1]


test_cases = [([2, 1, -2, 5], [3, 0, -6], 18),
              ([3, -2], [2, -6, 7], 21),
              ([-1, -1], [1, 1], -1),
              ([2, 1, -2, 5], [3, 0, -6], 18), ]
for test_nums_1, test_nums_2, expected_output in test_cases:
    assert max_dot_product(test_nums_1, test_nums_2) == expected_output
