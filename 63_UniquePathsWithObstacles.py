"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""
from typing import List


def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    """
    :param obstacle_grid: grids with some obstacles added
    :return: unique path from top-left to bottom right, if robot can only move down or right at any point in time
    """
    if not obstacle_grid or not obstacle_grid[0]:
        return 1
    elif obstacle_grid[0][0]:
        return 0
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    path_count = [[0] * n for _ in range(m)]
    path_count[0][0] = 1
    for i in range(m):
        for j in range(n):
            if not obstacle_grid[i][j] and (i + j > 0):
                up_path = 0 if i == 0 else path_count[i - 1][j]
                left_path = 0 if j == 0 else path_count[i][j - 1]
                path_count[i][j] = up_path + left_path
    return path_count[-1][-1]


assert unique_paths_with_obstacles([[0]]) == 1
assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
assert unique_paths_with_obstacles([[1]]) == 0
