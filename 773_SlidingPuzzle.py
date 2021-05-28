"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is
 impossible for the state of the board to be solved, return -1.
"""
from typing import List, Tuple


def sliding_puzzle(board: List[List[int]]) -> int:
    """
    :param board: starting from board
    :return: minimum no of moves to get to [[1, 2, 3], [4, 5, 0]]
    """
    if board == [[1, 2, 3], [4, 5, 0]]:
        return 0

    target_board = 123450

    multiple_lookup = {(0, 0): 100000,
                       (0, 1): 10000,
                       (0, 2): 1000,
                       (1, 0): 100,
                       (1, 1): 10,
                       (1, 2): 1}
    next_steps = {(0, 0): [(0, 1), (1, 0)],
                  (0, 1): [(0, 0), (0, 2), (1, 1)],
                  (0, 2): [(0, 1), (1, 2)],
                  (1, 0): [(1, 1), (0, 0)],
                  (1, 1): [(1, 0), (1, 2), (0, 1)],
                  (1, 2): [(1, 1), (0, 2)]}

    current_board = 0
    zero_position = None
    zero_multiple = 100000
    for i in range(2):
        row_i = board[i]
        for j in range(3):
            if row_i[j] == 0:
                zero_position = (i, j)
            else:
                current_board += row_i[j] * zero_multiple
            zero_multiple //= 10

    exploring: List[Tuple[int, Tuple[int, int]]] = [(current_board, zero_position), ]
    seen = {current_board}

    current_step = 1
    while exploring:
        next_explore = []
        while exploring:
            current_board, zero_position = exploring.pop()
            zero_multiple = multiple_lookup[zero_position]

            for next_zero_position in next_steps[zero_position]:
                swap_multiple = multiple_lookup[next_zero_position]
                swap_digit = current_board // swap_multiple % 10
                next_board = current_board - swap_digit * swap_multiple + swap_digit * zero_multiple
                if next_board == target_board:
                    return current_step
                if next_board not in seen:
                    next_explore.append((next_board, next_zero_position))
                    seen.add(next_board)

        current_step += 1
        exploring = next_explore

    return -1


test_cases = [([[1, 2, 3], [4, 0, 5]], 1),
              ([[1, 2, 3], [5, 4, 0]], -1),
              ([[4, 1, 2], [5, 0, 3]], 5),
              ([[3, 2, 4], [1, 5, 0]], 14),
              ([[5, 3, 2], [0, 4, 1]], 18),
              ([[1, 2, 3], [4, 5, 0]], 0), ]
for test_board, expected_value in test_cases:
    assert sliding_puzzle(test_board) == expected_value
