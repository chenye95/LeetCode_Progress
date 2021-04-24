"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.
"""
from typing import List


def projection_area(grid: List[List[int]]) -> int:
    """
    :param grid: height map of towers where grid[i][j] is the height of the tower at (i, j)
    :return: projection areas onto xy, yz, and zx planes
    """
    xz_project = sum(map(max, *grid)) if len(grid) > 1 else sum(grid[0])
    yz_project = sum([max(grid_i) for grid_i in grid])
    xy_project = sum(sum(grid_i_j > 0 for grid_i_j in grid_i) for grid_i in grid)
    return xy_project + xz_project + yz_project


test_cases = [([[1, 2, 3, 4, 5, 6], [3, 2, 1, 4, 5, 6], [4, 3, 2, 1, 5, 6], [1, 1, 1, 1, 1, 1]], 68),
              ([[1, 2], [3, 4]], 17),
              ([[1, 0], [0, 2]], 8),
              ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 14),
              ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 21),
              ([[2]], 5), ]
for test_grid, expected_output in test_cases:
    assert projection_area(test_grid) == expected_output
