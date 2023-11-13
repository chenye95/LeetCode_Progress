"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
 another 2D matrix and do the rotation.
"""
from copy import deepcopy
from typing import List


def rotate_set_of_four(matrix: List[List[int]]) -> None:
    """
    :param matrix: None empty square matrix, n x n, to be rotated clockwise, in place
    """
    n = len(matrix)
    # divide the matrix into 4 sections
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]  # bottom_left corner
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]  # bottom_left takes bottom_right
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]  # bottom_right takes top_right
            matrix[j][n - 1 - i] = matrix[i][j]  # top_right takes top_left
            matrix[i][j] = tmp  # top_left takes bottom_left


def rotate_transpose_reflect(matrix: List[List[int]]) -> None:
    """
    :param matrix: None empty square matrix, n x n, to be rotated clockwise, in place
    """
    n = len(matrix)

    # Transpose around main diagonal
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Flip around the vertical midpoint
    for i in range(n):
        matrix[i].reverse()


test_cases = [([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
               [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]),
              ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
              ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
               [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
              ([[1]], [[1]]),
              ([[1, 2], [3, 4]], [[3, 1], [4, 2]]), ]
for rotate in [rotate_transpose_reflect, rotate_set_of_four, ]:
    for test_matrix, expected_output in test_cases:
        copy_matrix = deepcopy(test_matrix)
        rotate(copy_matrix)
        assert copy_matrix == expected_output, rotate.__name__
