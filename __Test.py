def uniquePaths(m: int, n: int) -> int:
    assert m > 0 and n > 0
    grid = [[1] * n]
    grid.extend([[0] * n for _ in range(m-1)])
    for i in range(1, m):
        grid_i = grid[i]
        grid_prev = grid[i-1]
        grid_i[0] = 1
        for j in range(1, n):
            grid_i[j] = grid_i[j - 1] + grid_prev[j]
    return grid[m - 1][n - 1]

assert 3 == uniquePaths(3, 2)
assert 28 == uniquePaths(7, 3)
