"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or
right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given
that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
"""
from collections import deque
from typing import List


def shortest_path(grid: List[List[int]], k: int) -> int:
    """
    :param grid: m x n grid where each cell is either 0 (empty) or 1 (obstacle)
    :param k: remove at most k obstacles
    :return: minimum number of steps from upper left to bottom right, -1 else
    """
    if not grid or not grid[0]:
        return -1
    if k >= len(grid) + len(grid[0]) - 2:
        return len(grid) + len(grid[0]) - 2

    visited_states = {(0, 0, k), }  # x, y, # of obstacles removal left
    state_queue = deque([(0, 0, k, 0), ])  # x, y, # of obstacles removal left, steps
    m, n = len(grid), len(grid[0])
    while state_queue:
        x, y, left_obstacles, step = state_queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < m and 0 <= next_y < n) and \
                    ((grid[next_x][next_y] == 0 and (next_x, next_y, left_obstacles) not in visited_states) or
                     (grid[next_x][next_y] == 1 and left_obstacles > 0
                      and (next_x, next_y, left_obstacles - 1) not in visited_states)):
                if next_x == m - 1 and next_y == n - 1:
                    return step + 1
                else:
                    state_queue.append((next_x, next_y, left_obstacles - grid[next_x][next_y], step + 1))
                    visited_states.add((next_x, next_y, left_obstacles - grid[next_x][next_y]))
    return -1


assert shortest_path(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1) == 6
assert shortest_path(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1) == -1
