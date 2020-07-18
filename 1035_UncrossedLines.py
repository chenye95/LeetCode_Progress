"""
We write the integers of list_a and list_b (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers list_a[i] and list_b[j] such that:
- list_a[i] == list_b[j];
- The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.
"""
from typing import List


def max_uncrossed_lines(list_a: List[int], list_b: List[int]) -> int:
    """
    Dynamic Programming method
    :return: maximum number of connecting lines between list_a[i] == list_b[j]
    """
    m, n = len(list_a), len(list_b)
    previous_row = [0] * (n + 1)
    for i in range(m):
        current_row = [0] * (n + 1)
        for j in range(n):
            current_row[j + 1] = max(previous_row[j] + (list_a[i] == list_b[j]), current_row[j], previous_row[j + 1])
        previous_row = current_row
    return previous_row[-1]


assert max_uncrossed_lines(list_a=[1, 4, 2], list_b=[1, 2, 4]) == 2
assert max_uncrossed_lines(list_a=[2, 5, 1, 2, 5], list_b=[10, 5, 2, 1, 5, 2]) == 3
assert max_uncrossed_lines(list_a=[1, 3, 7, 1, 7, 5], list_b=[1, 9, 2, 5, 1]) == 2
assert max_uncrossed_lines(list_a=[3, 2], list_b=[2, 2, 2, 3]) == 1
