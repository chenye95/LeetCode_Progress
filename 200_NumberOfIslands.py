"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.
"""
from typing import List


def num_of_islands(grid: List[List[str]]) -> int:
    def dfs_explore_island(ref_grid: List[List[str]], i: int, j: int) -> None:
        if 0 <= i < len(ref_grid) and 0 <= j < len(ref_grid[0]) and ref_grid[i][j] == '1':
            ref_grid[i][j] = '#'
            dfs_explore_island(ref_grid, i - 1, j)
            dfs_explore_island(ref_grid, i + 1, j)
            dfs_explore_island(ref_grid, i, j - 1)
            dfs_explore_island(ref_grid, i, j + 1)

    if not grid:
        return 0

    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs_explore_island(grid, i, j)
                island_count += 1
    return island_count


assert 1 == num_of_islands(grid=[["1", "1", "1", "1", "0"],
                                 ["1", "1", "0", "1", "0"],
                                 ["1", "1", "0", "0", "0"],
                                 ['0', "0", "0", "0", "0"]]
                           )
assert 3 == num_of_islands(grid=[["1", "1", "0", "0", "0"],
                                 ["1", "1", "0", "0", "0"],
                                 ["0", "0", "1", "0", "0"],
                                 ["0", "0", "0", "1", "1"]]
                           )
