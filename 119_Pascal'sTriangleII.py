"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""
from typing import List


def get_row(row_index: int) -> List[int]:
    """
    :param row_index: k ≤ 33
    :return: the kth index row of the Pascal's triangle
    """
    if row_index == 0:
        return [1]
    elif row_index == 1:
        return [1, 1]
    next_row = [1] * 3
    current_row = [1, 1]
    for k in range(1, row_index):
        for j in range(1, k + 1):
            next_row[j] = current_row[j] + current_row[j - 1]
        current_row = next_row
        next_row = [1] * (k + 3)
    return current_row


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
for i in range(10):
    assert get_row(i) == expected_triangles[i]
