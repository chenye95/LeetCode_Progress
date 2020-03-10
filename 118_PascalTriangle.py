"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]

    return_value = [[1], [1, 1]]
    last_row = return_value[-1]
    for i in range(3, numRows + 1):
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


assert generate(5) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
