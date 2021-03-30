"""
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two
consecutive elements is the same.

The function returns the number of arithmetic slices in the array a.
"""
from typing import List


def number_of_arithmetic_slices(a: List[int]) -> int:
    """
    :param a: array of integers
    :return: number of arithmetic slices in array a
    """
    current_slice = 0
    total_count = 0
    for i in range(2, len(a)):
        if a[i] + a[i - 2] == a[i - 1] << 1:
            current_slice += 1
            total_count += current_slice
        else:
            current_slice = 0
    return total_count


test_cases = [([1, 2, 3, 4], 3), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 55), ([7, 8, 9, 10], 3), ]
for test_a, expected_output in test_cases:
    assert number_of_arithmetic_slices(test_a) == expected_output
