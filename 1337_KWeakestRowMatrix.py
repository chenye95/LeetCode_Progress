"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the
k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they
have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is,
always ones may appear first and then zeros.
"""
from typing import List


def k_weakest_rows(matrix: List[List[int]], k: int) -> List[int]:
    return [i for _, i in sorted([(sum(row_i), i) for i, row_i in enumerate(matrix)])[:k]]


assert k_weakest_rows(matrix=[[1, 1, 0, 0, 0],
                              [1, 1, 1, 1, 0],
                              [1, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0],
                              [1, 1, 1, 1, 1]],
                      k=3) == [2, 0, 3]
assert k_weakest_rows(matrix=[[1, 0, 0, 0],
                              [1, 1, 1, 1],
                              [1, 0, 0, 0],
                              [1, 0, 0, 0]],
                      k=2) == [0, 2]
