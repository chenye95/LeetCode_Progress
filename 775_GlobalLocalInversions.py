"""
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.
"""
from typing import List


def is_ideal_permutations(a: List[int]) -> bool:
    """
    :param a: permutations of [0, 1, ..., n - 1] where n = len(a)
    :return: whether global inversions count equal to local inversions count
    """
    # Note all local inversions are by definition global inversions
    # if abs(a[i] - i) > 1 then the local inversion will great at least 2 global inversions
    # so for ideal_permutations for i and a[i], abs(i - a[i]) <= 1
    return all(abs(i - a_i) <= 1 for i, a_i in enumerate(a))


test_cases = [([1, 0, 2], True), ([1, 2, 0], False), ]
for test_list, expected_output in test_cases:
    assert is_ideal_permutations(test_list) is expected_output
