"""
The function returns the number of arithmetic slices in the array a.
"""
from typing import List


def number_of_arithmetic_slices(a: List[int]) -> int:
    current_slice = 0
    total_count = 0
    for i in range(2, len(a)):
        if a[i] + a[i - 2] == a[i - 1] << 1:
            current_slice += 1
            total_count += current_slice
        else:
            current_slice = 0
    return total_count


assert number_of_arithmetic_slices([1, 2, 3, 4]) == 3
