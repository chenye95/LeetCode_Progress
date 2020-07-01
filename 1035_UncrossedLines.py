"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
- A[i] == B[j];
- The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.
"""
from typing import List


def maxUncrossedLines(A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    previous_row = [0] * (n + 1)
    for i in range(m):
        current_row = [0] * (n + 1)
        for j in range(n):
            current_row[j + 1] = max(previous_row[j] + (A[i] == B[j]), previous_row[j + 1], current_row[j])
        previous_row = current_row
    return previous_row[-1]


assert maxUncrossedLines(A=[1, 4, 2], B=[1, 2, 4]) == 2
assert maxUncrossedLines(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]) == 3
assert maxUncrossedLines(A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]) == 2
assert maxUncrossedLines(A=[3, 2], B=[2, 2, 2, 3]) == 1
