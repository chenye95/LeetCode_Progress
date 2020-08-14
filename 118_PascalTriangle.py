"""
Given a non-negative integer num_rows, generate the first num_rows of Pascal's triangle.
"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    """
    :return: first num_rows of Pascal's triangles
    """
    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]
    elif num_rows == 2:
        return [[1], [1, 1]]

    return_value = [[1], [1, 1]]
    last_row = return_value[-1]
    for i in range(3, num_rows + 1):
        current_row = [1] * ((i + 1) // 2)
        for j in range(1, (i + 1) // 2):
            current_row[j] = last_row[j - 1] + last_row[j]
        if i % 2:
            current_row += current_row[:-1][::-1]
        else:
            current_row += current_row[::-1]
        return_value.append(current_row)
        last_row = current_row

    return return_value


expected_triangles = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]
for i in range(1, len(expected_triangles) + 1):
    assert generate(i) == expected_triangles[:i]
