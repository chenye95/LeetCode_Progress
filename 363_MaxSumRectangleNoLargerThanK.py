"""
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no
 larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.
"""
import bisect
from typing import List


def max_sub_matrix_no_greater_k_precompute(matrix: List[List[int]], k: int) -> int:
    """
    :param matrix: matrix of integers values, such that 1 <= matrix.length <= 100 and 1 <= matrix[0].length <= 100
    :param k: -10**5 <= k <= 10**5
    :return: will destruct matrix, return max sum of a sub matrix that is no larger than k
    """
    # Convert matrix into cumulative sum
    # i.e. row[i][j] = sum(old_matrix[i][:j+1]), self included
    m, n = len(matrix), len(matrix[0])
    for row in matrix:
        for i in range(1, n):
            row[i] += row[i - 1]

    sub_matrix_max = float("-inf")
    for col_1 in range(n):
        for col_2 in range(col_1, n):
            # use cumulative sum methods to count sub matrix count that bounded between col_1 and col_2
            previous_sum = [float("inf")]
            accumulator = 0
            for row_i in range(m):
                bisect.insort(previous_sum, accumulator)
                accumulator += matrix[row_i][col_2] - (matrix[row_i][col_1 - 1] if col_1 else 0)
                i = bisect.bisect_left(previous_sum, accumulator - k)
                sub_matrix_max = max(sub_matrix_max, accumulator - previous_sum[i])
                if sub_matrix_max == k:
                    return k

    return sub_matrix_max


def max_sub_matrix_no_greater_k_on_the_fly(matrix: List[List[int]], k: int) -> int:
    """
    :param matrix: matrix of integers values, such that 1 <= matrix.length <= 100 and 1 <= matrix[0].length <= 100
    :param k: -10**5 <= k <= 10**5
    :return: will not destruct matrix, return max sum of a sub matrix that is no larger than k
    """
    # Convert matrix into cumulative sum
    # i.e. row[i][j] = sum(old_matrix[i][:j+1]), self included
    m, n = len(matrix), len(matrix[0])
    if m > n:
        matrix = list(zip(*matrix))
        m, n = n, m

    sub_matrix_max = float("-inf")
    for row_1 in range(m):
        cumulative_sum = [0] * n  # cumulative sum for sub matrix with upper bound on row_1
        for row_2 in range(row_1, m):
            for col, val in enumerate(matrix[row_2]):
                cumulative_sum[col] += val

            # use cumulative sum methods to count sub matrix count that bounded between col_1 and col_2
            previous_sum = [float("inf")]
            accumulator = 0
            for col_cumulative_sum in cumulative_sum:
                bisect.insort(previous_sum, accumulator)
                accumulator += col_cumulative_sum
                i = bisect.bisect_left(previous_sum, accumulator - k)
                sub_matrix_max = max(sub_matrix_max, accumulator - previous_sum[i])
                if sub_matrix_max == k:
                    return k

    return sub_matrix_max


test_cases = [([[1, 0, 1], [0, -2, 3]], 2, 2),
              ([[2, 2, -1]], 3, 3),
              ([[2, 2, -1]], 0, -1),
              ([[27, 5, -20, -9, 1, 26, 1, 12, 7, -4, 8, 7, -1, 5, 8],
                [16, 28, 8, 3, 16, 28, -10, -7, -5, -13, 7, 9, 20, -9, 26],
                [24, -14, 20, 23, 25, -16, -15, 8, 8, -6, -14, -6, 12, -19, -13],
                [28, 13, -17, 20, -3, -18, 12, 5, 1, 25, 25, -14, 22, 17, 12],
                [7, 29, -12, 5, -5, 26, -5, 10, -5, 24, -9, -19, 20, 0, 18],
                [-7, -11, -8, 12, 19, 18, -15, 17, 7, -1, -11, -10, -1, 25, 17],
                [-3, -20, -20, -7, 14, -12, 22, 1, -9, 11, 14, -16, -5, -12, 14],
                [-20, -4, -17, 3, 3, -18, 22, -13, -1, 16, -11, 29, 17, -2, 22],
                [23, -15, 24, 26, 28, -13, 10, 18, -6, 29, 27, -19, -19, -8, 0],
                [5, 9, 23, 11, -4, -20, 18, 29, -6, -4, -11, 21, -6, 24, 12],
                [13, 16, 0, -20, 22, 21, 26, -3, 15, 14, 26, 17, 19, 20, -5],
                [15, 1, 22, -6, 1, -9, 0, 21, 12, 27, 5, 8, 8, 18, -1],
                [15, 29, 13, 6, -11, 7, -6, 27, 22, 18, 22, -3, -9, 20, 14],
                [26, -6, 12, -10, 0, 26, 10, 1, 11, -10, -16, -18, 29, 8, -8],
                [-19, 14, 15, 18, -10, 24, -9, -7, -19, -14, 23, 23, 17, -5, 6]], -100, -101),
              ([[2, 4, 2, 8, -7, -10],
                [-10, 6, -9, 0, -9, -8],
                [9, -6, -6, -2, 7, -10],
                [4, 3, -4, 7, 4, 4],
                [-4, 7, -10, 8, 8, -3]], 10, 10),
              ([[7, 7, 4, -6, -10],
                [-7, -3, -9, -1, -7],
                [9, 6, -3, -7, 7],
                [-4, 1, 4, -3, -8],
                [-7, -4, -4, 6, -10],
                [1, 3, -2, 3, -10],
                [8, -2, 1, 1, -8]], 12, 12), ]
# do not change order of functions
for max_sub_matrix_no_greater_k in [max_sub_matrix_no_greater_k_on_the_fly, max_sub_matrix_no_greater_k_precompute]:
    for test_matrix, test_k, expected_output in test_cases:
        assert max_sub_matrix_no_greater_k(test_matrix, test_k) == expected_output, max_sub_matrix_no_greater_k.__name__
