"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following
properties:
- Integers in each row are sorted in ascending from left to right
- Integers in each column are sorted in ascending from top to bottom.
"""
from bisect import bisect_left
from typing import List


def search_matrix_binary_search(matrix: List[List[int]], target: int) -> bool:
    """
    Search from top right, leftward and downward. Utilize property 2 to eliminate whole columns

    :return: whether target exists in matrix
    """
    if not matrix or not matrix[0]:
        return False
    j = len(matrix[0]) - 1
    for row in matrix:
        j = bisect_left(row, target, hi=j)
        if row[j] == target:
            return True
        elif row[j] > target:
            j -= 1

    return False


def search_matrix_sequential(matrix: List[List[int]], target: int) -> bool:
    """
    Search from top right, leftward and downward. Utilize property 2 to eliminate whole columns

    :return: whether target exists in matrix
    """
    if not matrix or not matrix[0]:
        return False
    j = len(matrix[0]) - 1
    for row in matrix:
        while j and row[j] > target:
            # ignore column j beneath the current row
            j -= 1
        if row[j] == target:
            return True

    return False


test_cases = [
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5, True),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20, False),
]
for search_matrix in [search_matrix_binary_search, search_matrix_sequential]:
    for test_matrix, test_target, expected_output in test_cases:
        assert search_matrix(matrix=test_matrix, target=test_target) is expected_output, search_matrix.__name__
