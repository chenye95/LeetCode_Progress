"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such
that:
- Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
- C_1 is at location (0, 0) (ie. has value grid[0][0])
- C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
- If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return
-1.
"""
from collections import deque
from typing import List


def shortest_path_binary_matrix_bfs(grid: List[List[int]]) -> int:
    """
    BFS search approach;
    Grid values will be destructed
    """
    if not grid or grid[0][0] or grid[-1][-1]:
        return -1

    m, n = len(grid), len(grid[0])
    grid[0][0] = 1
    frontier = deque([(1, 0, 0)])
    while frontier:
        steps, current_x, current_y = frontier.popleft()
        if (current_x, current_y) == (m - 1, n - 1):
            return steps
        for d_x, d_y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if 0 <= current_x + d_x < m and 0 <= current_y + d_y < n and grid[current_x + d_x][current_y + d_y] == 0:
                frontier.append((steps + 1, current_x + d_x, current_y + d_y))
                # Shortest path will have no loop, or repetitive visit of the same block
                grid[current_x + d_x][current_y + d_y] = 1

    return -1


for shortest_path_binary_matrix in [shortest_path_binary_matrix_bfs]:
    assert 2 == shortest_path_binary_matrix(grid=[[0, 1], [1, 0]])
    assert 4 == shortest_path_binary_matrix(grid=[[0, 0, 0],
                                                  [1, 1, 0],
                                                  [1, 1, 0]])
    assert 7 == shortest_path_binary_matrix(grid=[[0, 1, 0, 0, 0, 0],
                                                  [0, 1, 1, 1, 1, 1],
                                                  [0, 0, 0, 0, 1, 1],
                                                  [0, 1, 0, 0, 0, 1],
                                                  [1, 0, 0, 1, 0, 1],
                                                  [0, 0, 1, 0, 1, 0]])
    assert 11 == shortest_path_binary_matrix(grid=[[0, 0, 0, 0, 1, 1, 1, 1, 0],
                                                   [0, 1, 1, 0, 0, 0, 0, 1, 0],
                                                   [0, 0, 1, 0, 0, 0, 0, 0, 0],
                                                   [1, 1, 0, 0, 1, 0, 0, 1, 1],
                                                   [0, 0, 1, 1, 1, 0, 1, 0, 1],
                                                   [0, 1, 0, 1, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 1, 0, 1, 0, 0, 0],
                                                   [0, 1, 0, 1, 1, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 1, 0, 1, 0]])
    assert 9 == shortest_path_binary_matrix(grid=[[0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 1, 0, 0, 0, 0, 1],
                                                  [1, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 1, 1, 0],
                                                  [0, 0, 1, 0, 1, 0, 1, 1],
                                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 1, 1, 1, 0, 0],
                                                  [1, 0, 1, 1, 1, 0, 0, 0]])
