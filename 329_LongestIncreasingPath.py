"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move
outside of the boundary (i.e. wrap-around is not allowed)
"""
from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    """
    DFS with memorization
    """

    def dfs_recurse(ref_memory: List[List[int]], ref_matrix: List[List[int]], i: int, j: int) -> int:
        nonlocal m, n
        if not ref_memory[i][j]:
            current_val = ref_matrix[i][j]
            dp_memory[i][j] = 1 + max(
                dfs_recurse(ref_memory, ref_matrix, i - 1, j) if i and ref_matrix[i - 1][j] > current_val else 0,
                dfs_recurse(ref_memory, ref_matrix, i + 1, j) if i < m - 1
                                                                 and ref_matrix[i + 1][j] > current_val else 0,
                dfs_recurse(ref_memory, ref_matrix, i, j - 1) if j and ref_matrix[i][j - 1] > current_val else 0,
                dfs_recurse(ref_memory, ref_matrix, i, j + 1) if j < n - 1
                                                                 and ref_matrix[i][j + 1] > current_val else 0,
            )
        return ref_memory[i][j]

    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp_memory = [[0] * n for _ in range(m)]
    return max([dfs_recurse(dp_memory, matrix, i, j) for i in range(m) for j in range(n)])


assert 4 == longest_increasing_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
assert 4 == longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]])
assert 140 == longest_increasing_path([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                       [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
                                       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                                       [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
                                       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
                                       [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
                                       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
                                       [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
                                       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
                                       [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
                                       [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
                                       [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
                                       [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
                                       [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
