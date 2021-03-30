"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific
ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
"""
from collections import deque
from typing import List, Tuple, Deque, Set


def pacific_atlantic_bfs(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Traverse from ocean to hill (from lower height to taller height path)

    :param matrix: len and width 0 <= m, n < 150
    :return: order of returned grid coordinates does not matter
    """
    if not matrix or not matrix[0]:
        return []

    n_rows, n_cols = len(matrix), len(matrix[0])
    pacific_queue = deque([(i, 0) for i in range(n_rows)] + [(0, i) for i in range(1, n_cols)])
    atlantic_queue = deque([(i, n_cols - 1) for i in range(n_rows)] + [(n_rows - 1, i) for i in range(n_cols - 1)])

    def bfs_ocean(ocean_queue: Deque[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        """
        Traverse from ocean to hill (from lower height to taller height path)
        """
        reachable = set()
        while ocean_queue:
            row, col = ocean_queue.popleft()
            if (row, col) not in reachable:
                reachable.add((row, col))
                current_height = matrix[row][col]
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < n_rows and 0 <= new_col < n_cols and (new_row, new_col) not in reachable and \
                            matrix[new_row][new_col] >= current_height:
                        ocean_queue.append((new_row, new_col))

        return reachable

    # Perform BFS for both oceans and find intersections
    pacific_reachable = bfs_ocean(pacific_queue)
    atlantic_reachable = bfs_ocean(atlantic_queue)
    return list(pacific_reachable.intersection(atlantic_reachable))


def pacific_atlantic_dfs(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Traverse from ocean to hill (from lower height to taller height path)

    :param matrix: len and width 0 <= m, n < 150
    :return: order of returned grid coordinates does not matter
    """
    if not matrix or not matrix[0]:
        return []

    n_rows, n_cols = len(matrix), len(matrix[0])
    pacific_reachable, atlantic_reachable = set(), set()

    def dfs_ocean(row: int, col: int, ocean_reachable: Set[Tuple[int, int]]) -> None:
        """
        Traverse from ocean to hill (from lower height to taller height path)
        """
        if (row, col) not in ocean_reachable:
            ocean_reachable.add((row, col))
            current_height = matrix[row][col]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n_rows and 0 <= new_col < n_cols and (new_row, new_col) not in ocean_reachable and \
                        matrix[new_row][new_col] >= current_height:
                    dfs_ocean(new_row, new_col, ocean_reachable)

    for i in range(n_rows):
        dfs_ocean(i, 0, pacific_reachable)
        dfs_ocean(i, n_cols - 1, atlantic_reachable)
    for i in range(n_cols):
        dfs_ocean(0, i, pacific_reachable)
        dfs_ocean(n_rows - 1, i, atlantic_reachable)

    # Perform BFS for both oceans and find intersection
    return list(pacific_reachable.intersection(atlantic_reachable))


test_matrices = [([[1, 2, 2, 3, 5],
                   [3, 2, 3, 4, 4],
                   [2, 4, 5, 3, 1],
                   [6, 7, 1, 4, 5],
                   [5, 1, 1, 2, 4], ],
                  {(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)}),
                 ([[1, 1],
                   [1, 1],
                   [1, 1], ],
                  {(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)}), ]
for test_matrix, expected_output in test_matrices:
    for pacific_atlantic in [pacific_atlantic_dfs, pacific_atlantic_bfs]:
        assert set(pacific_atlantic(test_matrix)) == expected_output, pacific_atlantic.__name__
