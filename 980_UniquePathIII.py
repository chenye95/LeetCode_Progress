"""
On a 2-dimensional grid, there are 4 types of squares:
* 1 represents the starting square.  There is exactly one starting square.
* 2 represents the ending square.  There is exactly one ending square.
* 0 represents empty squares we can walk over.
* -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every
 non-obstacle square exactly once
"""
from typing import List


def unique_path_count(grid: List[List[int]]) -> int:
    """
    :param grid: m x n grid with 1 starting square and one ending square, empty_count are either empty or blocked with
        obstacle
    :return: number of ways from starting to ending square
    """
    _exploring_cell = -2

    def dfs_explore(x: int, y: int, empty_count: int) -> int:
        """
        :param x: currently on cell (x, y)
        :param y: currently on cell (x, y)
        :param empty_count: # of non-obstacle squares remain to explore
        :return: unique path count from current state
        """
        if grid[x][y] == 2:
            return empty_count == 0

        save_val, grid[x][y] = grid[x][y], _exploring_cell
        path_count = 0

        for d_x, d_y in neighbors:
            next_x, next_y = x + d_x, y + d_y
            if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] >= 0:
                path_count += dfs_explore(next_x, next_y, empty_count - 1)

        grid[x][y] = save_val
        return path_count

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    empty_cell_count = 0

    m, n = len(grid), len(grid[0])
    # Starting position
    s_x, s_y = -1, -1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                s_x, s_y = i, j
                grid[i][j] = _exploring_cell
            elif grid[i][j] != -1:
                empty_cell_count += 1

    return dfs_explore(s_x, s_y, empty_cell_count)


test_cases = [([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
              ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
              ([[0, 1], [2, 0]], 0),
              ([[0, 0, 0, 0, 0, 1, 0, 2, 0, -1, 0, -1, 0, -1, 0]], 0),
              ([[0, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, 0], [1, 0, 2, 0], [0, 0, -1, 0]], 0), ]
for test_grid, expected_count in test_cases:
    assert unique_path_count(test_grid) == expected_count
