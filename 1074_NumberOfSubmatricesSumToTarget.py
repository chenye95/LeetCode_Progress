"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different:
 for example, if x1 != x1'
"""
from typing import List


def num_submatrix_sum_target(matrix: List[List[int]], target: int) -> int:
    n_row, n_col = len(matrix), len(matrix[0])

    # matrix sum of sub matrix
    # [r, c] -> (0, 0, r - 1, c - 1)
    # padded with zeros on the left and top
    cumulative_sum = [[0] * (n_col + 1) for _ in range(n_row + 1)]
    for r in range(n_row):
        current_row = matrix[r]
        row_sum = 0
        for c in range(n_col):
            row_sum += current_row[c]
            cumulative_sum[r + 1][c + 1] = cumulative_sum[r][c + 1] + row_sum

    return_result = 0
    for r_1 in range(n_row):
        for r_2 in range(r_1 + 1, n_row + 1):
            seen_in_current_section = {0: 1}
            for c_plus_one in range(1, n_col + 1):
                # x is the sum of submatrix (r_1, 0, r_2, c_plus_one - 1)
                x = cumulative_sum[r_2][c_plus_one] - cumulative_sum[r_1][c_plus_one]
                if x - target in seen_in_current_section:
                    return_result += seen_in_current_section[x - target]
                seen_in_current_section[x] = seen_in_current_section.get(x, 0) + 1

    return return_result


assert num_submatrix_sum_target(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0) == 4
assert num_submatrix_sum_target(matrix=[[1, -1], [-1, 1]], target=0) == 5
assert num_submatrix_sum_target(matrix=[[904]], target=0) == 0
