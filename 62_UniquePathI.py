"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
 of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


def unique_paths(m: int, n: int) -> int:
    """
    :param m: width of the grid m x n, 1 <= m <= 100
    :param n: height of the grid m x n, 1 <= n <= 100
    :return: number of path traversing from top left corner to bottom right corner
    """
    path_count = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            path_count[i][j] = path_count[i][j - 1] + path_count[i - 1][j]
    return path_count[-1][-1]


test_cases = [(3, 2, 3), (7, 3, 28), (3, 3, 6), (51, 9, 1916797311), ]
for test_m, test_n, expected_output in test_cases:
    assert unique_paths(test_m, test_n) == expected_output
