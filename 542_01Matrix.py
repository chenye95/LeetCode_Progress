"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
from collections import deque
from typing import List


def update_matrix_bfs(matrix: List[List[int]]) -> List[List[int]]:
    """
    BFS Solution

    :param matrix: matrix of 0 and 1. Matrix will be preserved after the computation
    :return: 2D matrix of same size, with each cell equals to distance to the nearest 0
    """
    if not matrix:
        return matrix
    m, n = len(matrix), len(matrix[0])
    dist_matrix = [[m + n] * n for _ in range(m)]

    traverse_queue = deque()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dist_matrix[i][j] = 0
                traverse_queue.append((i, j))  # append all 0s to the queue

    while traverse_queue:
        r, c = traverse_queue.popleft()
        for d_r, d_c in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + d_r, c + d_c
            if 0 <= new_r < m and 0 <= new_c < n and dist_matrix[new_r][new_c] > dist_matrix[r][c] + 1:
                dist_matrix[new_r][new_c] = dist_matrix[r][c] + 1
                traverse_queue.append((new_r, new_c))

    return dist_matrix


def update_matrix_dp(matrix: List[List[int]]) -> List[List[int]]:
    """
    DP Solution: shortest path doesn't go in loops: only direct paths with right-bottom moves or left-up moves

    :param matrix: matrix of 0 and 1. Matrix will be preserved after the computation
    :return: 2D matrix of same size, with each cell equals to distance to the nearest 0
    """
    if not matrix:
        return matrix
    m, n = len(matrix), len(matrix[0])
    dist_matrix = [[m + n] * n for _ in range(m)]

    # First Pass: from upper left
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                dist_matrix[r][c] = 0
            else:
                if r > 0:
                    dist_matrix[r][c] = min(dist_matrix[r][c], dist_matrix[r - 1][c] + 1)
                if c > 0:
                    dist_matrix[r][c] = min(dist_matrix[r][c], dist_matrix[r][c - 1] + 1)

    # Second Pass: from bottom right
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if r < m - 1:
                dist_matrix[r][c] = min(dist_matrix[r][c], dist_matrix[r + 1][c] + 1)
            if c < n - 1:
                dist_matrix[r][c] = min(dist_matrix[r][c], dist_matrix[r][c + 1] + 1)

    return dist_matrix


test_cases = [([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
              ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]), ]
for update_matrix in [update_matrix_bfs, update_matrix_dp]:
    for test_matrix, expected_output in test_cases:
        assert update_matrix(test_matrix) == expected_output
