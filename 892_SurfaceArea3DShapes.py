"""
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of
 v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular
 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.
"""
from typing import List


def surface_area(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    occupied_grid = 0
    total_surface_area = 0

    for i in range(m):
        total_surface_area += grid[i][0]
        occupied_grid += sum(map(lambda x: x > 0, grid[i]))
        for j in range(1, n):
            total_surface_area += abs(grid[i][j] - grid[i][j - 1])
        total_surface_area += grid[i][-1]

    for j in range(n):
        total_surface_area += grid[0][j]
        for i in range(1, m):
            total_surface_area += abs(grid[i][j] - grid[i - 1][j])
        total_surface_area += grid[-1][j]

    return total_surface_area + 2 * occupied_grid


test_cases = [
    ([[1, 2], [3, 4]], 34),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
    ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46),
    ([[3, 7, 18, 15, 15, 20, 16, 2, 9, 2, 8, 11, 6, 20, 7], [5, 19, 0, 15, 5, 16, 9, 12, 0, 6, 18, 6, 4, 3, 14],
      [8, 9, 6, 15, 8, 5, 19, 20, 2, 2, 14, 17, 12, 20, 2], [14, 19, 0, 1, 13, 7, 18, 20, 11, 8, 11, 12, 6, 0, 7],
      [13, 15, 14, 8, 18, 17, 3, 10, 20, 20, 12, 19, 1, 11, 2], [7, 7, 9, 14, 10, 6, 19, 7, 20, 18, 16, 5, 9, 9, 1],
      [15, 3, 13, 1, 10, 12, 0, 15, 18, 17, 0, 4, 1, 6, 19], [6, 10, 5, 10, 15, 19, 12, 7, 14, 9, 6, 14, 8, 14, 19],
      [19, 6, 13, 2, 13, 11, 10, 16, 13, 12, 4, 9, 9, 8, 8], [19, 2, 18, 18, 3, 11, 8, 0, 7, 12, 4, 2, 5, 10, 5],
      [3, 1, 19, 13, 12, 11, 4, 16, 0, 16, 8, 3, 15, 14, 18], [11, 11, 2, 19, 13, 4, 9, 0, 14, 4, 10, 2, 11, 7, 17],
      [12, 15, 9, 10, 15, 17, 0, 4, 17, 14, 7, 2, 18, 0, 1], [0, 10, 14, 2, 2, 8, 0, 6, 5, 14, 13, 3, 9, 1, 4],
      [14, 5, 17, 5, 14, 14, 1, 16, 5, 4, 7, 12, 9, 8, 12]], 3882),
]
for test_grid, expected_value in test_cases:
    assert surface_area(test_grid) == expected_value
