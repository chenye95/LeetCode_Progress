"""
In a given grid, each cell can have one of three values:
- the value 0 representing an empty cell;
- the value 1 representing a fresh orange;
- the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return
-1 instead
"""
from typing import List


def orange_rotting(grid: List[List[int]]) -> int:
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    fresh = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1}
    rotten = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2}
    minutes_passed = 0

    while fresh:
        if not rotten:
            return -1
        rotten = {(r + d_r, c + d_c) for r, c in rotten for d_r, d_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                  if (r + d_r, c + d_c) in fresh}
        fresh -= rotten
        minutes_passed += 1

    return minutes_passed


assert orange_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
assert orange_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
assert orange_rotting([[0, 2]]) == 0
