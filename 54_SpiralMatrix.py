"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    return_list = []
    if not matrix:
        return []
    upper_bound, lower_bound = 0, len(matrix) - 1
    left_bound, right_bound = 0, len(matrix[0]) - 1
    while upper_bound < lower_bound and left_bound <= right_bound:
        return_list.extend(matrix[upper_bound][upper_bound:right_bound + 1])
        return_list.extend([row[right_bound] for row in matrix[upper_bound + 1:lower_bound]])
        tmp_list = matrix[lower_bound][upper_bound:right_bound + 1]
        tmp_list.reverse()
        return_list.extend(tmp_list)
        if left_bound < right_bound:
            return_list.extend([matrix[i][left_bound] for i in range(lower_bound - 1, upper_bound, -1)])
        upper_bound += 1
        left_bound += 1
        lower_bound -= 1
        right_bound -= 1
    if upper_bound == lower_bound:
        return_list.extend(matrix[upper_bound][upper_bound:right_bound + 1])
    return return_list


test_cases = [([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]], [1,2,3,6,9,8,7,4,5]),
              ([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
              ([[7], [9], [6]], [7, 9, 6]),
              ([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]], [1,2,3,4,5,6,7,8,9,10])]

for input, output in test_cases:
    assert spiralOrder(input) == output
