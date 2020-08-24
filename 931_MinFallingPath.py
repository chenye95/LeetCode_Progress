"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice
must be in a column that is different from the previous row's column by at most one.
"""
from copy import deepcopy
from typing import List


def min_falling_path(A: List[List[int]]) -> int:
    """
    :param A: square array of integers, such that 1 <= A.length == A[0].length <= 100 and -100 <= A[i][j] <= 100
    :return: minimum sum of a falling path through A
    """
    n = len(A[0])
    min_at_cell = deepcopy(A[0])
    for i in range(1, len(A)):
        fall_from_minus_one = float("inf")
        for j in range(n):
            fall_from_minus_one, min_at_cell[j] = min_at_cell[j], \
                                                  A[i][j] + min(fall_from_minus_one,
                                                                min_at_cell[j],
                                                                min_at_cell[j + 1] if j + 1 < n else float("inf"))
    return min(min_at_cell)


assert min_falling_path([[8, 93, 21], [18, -11, 19], [-23, 15, -42]]) == -45
assert min_falling_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 12
