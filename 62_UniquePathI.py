"""
A robot is located in the top-left corner of a m x n grid (marked 'Start' in the diagram below).

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
    previous_row = [1] * n
    for _ in range(1, m):
        current_row = [1] * n
        for j in range(1, n):
            current_row[j] = current_row[j - 1] + previous_row[j]
        previous_row = current_row
    return previous_row[-1]


test_cases = [(3, 2, 3), (7, 3, 28), (3, 3, 6), (51, 9, 1916797311), ]
for test_m, test_n, expected_output in test_cases:
    assert unique_paths(test_m, test_n) == expected_output
