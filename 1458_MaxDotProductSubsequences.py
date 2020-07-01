"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of
[1,2,3,4,5] while [1,5,3] is not).
"""
from typing import List


def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
    m, n = len(nums1), len(nums2)
    previous_iterations = [0] * n
    for i in range(m):
        current_iterations = [0] * n
        for j in range(n):
            current_iterations[j] = nums1[i] * nums2[j]  # Avoid empty subsequences
            if i and j: current_iterations[j] += max(previous_iterations[j - 1], 0)
            if i: current_iterations[j] = max(current_iterations[j], previous_iterations[j])
            if j: current_iterations[j] = max(current_iterations[j], current_iterations[j - 1])
        previous_iterations = current_iterations
    return previous_iterations[-1]


assert maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]) == 18
assert maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]) == 21
assert maxDotProduct(nums1=[-1, -1], nums2=[1, 1]) == -1
assert maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]) == 18
