"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.
"""
from typing import List


def num_of_islands(grid: List[List[str]]) -> int:
    """
    Depth First Search

    :param grid: 2D grid of 1 (land) and 0 (water)
    :return: number of islands in the grid
    """

    def dfs_explore_island(ref_grid: List[List[str]], i: int, j: int) -> None:

        ref_grid[i][j] = '#'
        if i > 0 and ref_grid[i - 1][j] == '1':
            dfs_explore_island(ref_grid, i - 1, j)
        if i + 1 < len(ref_grid) and ref_grid[i + 1][j] == '1':
            dfs_explore_island(ref_grid, i + 1, j)
        if j > 0 and ref_grid[i][j - 1] == '1':
            dfs_explore_island(ref_grid, i, j - 1)
        if j + 1 < len(ref_grid[0]) and ref_grid[i][j + 1] == '1':
            dfs_explore_island(ref_grid, i, j + 1)

    if not grid:
        return 0

    island_count = 0
    for row_i in range(len(grid)):
        for col_j in range(len(grid[0])):
            if grid[row_i][col_j] == '1':
                dfs_explore_island(grid, row_i, col_j)
                island_count += 1
    return island_count


test_cases = [([["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ['0', "0", "0", "0", "0"]], 1),
              ([["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]], 3), ]
for test_grid, expected_output in test_cases:
    assert num_of_islands(test_grid) == expected_output
