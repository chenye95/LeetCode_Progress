"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
"""
from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    :param grid: 2D array of 0 (water) and 1 (land)
    :return: maximum area of an island in the given 2D array
    """

    def search(i: int, j: int, area_so_far: int) -> int:
        if j + 1 < len(grid[i]) and grid[i][j + 1]:
            grid[i][j + 1] = 0
            area_so_far = search(i, j + 1, area_so_far + 1)
        if j - 1 >= 0 and grid[i][j - 1]:
            grid[i][j - 1] = 0
            area_so_far = search(i, j - 1, area_so_far + 1)
        if i + 1 < len(grid) and grid[i + 1][j]:
            grid[i + 1][j] = 0
            area_so_far = search(i + 1, j, area_so_far + 1)
        if i - 1 >= 0 and grid[i - 1][j]:
            grid[i - 1][j] = 0
            area_so_far = search(i - 1, j, area_so_far + 1)
        return area_so_far

    max_area: int = 0
    for i, r in enumerate(grid):
        for j, c in enumerate(grid[i]):
            if grid[i][j]:
                grid[i][j] = 0
                max_area = max(max_area, search(i, j, 1))
    return max_area


test_cases = [([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
              ([[0, 0, 0, 0, 0, 0, 0, 0]], 0), ]
for test_grid, expected_output in test_cases:
    assert max_area_of_island(test_grid) == expected_output
