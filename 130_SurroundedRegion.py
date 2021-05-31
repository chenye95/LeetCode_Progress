"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
from typing import List


def capture_surrounded_regions(board: List[List[str]]) -> None:
    """
    start from border and connect inwards

    :param board: 2D grid of X and O
    """
    if not board:
        return

    m, n = len(board), len(board[0])
    save_queue = [(0, j) for j in range(n) if board[0][j] == 'O']
    save_queue.extend([(m - 1, j) for j in range(n) if board[m - 1][j] == 'O'])
    save_queue.extend([(i, 0) for i in range(1, m - 1) if board[i][0] == 'O'])
    save_queue.extend([(i, n - 1) for i in range(1, m - 1) if board[i][n - 1] == 'O'])

    while save_queue:
        i, j = save_queue.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save_queue += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)

    board[:] = [['XO'[c == 'S'] for c in row] for row in board]


test_cases = [([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']],
               [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]),
              ([["X", "O", "O", "X", "X", "X", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["X", "O", "O", "X", "X", "O", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "O", "O", "X", "O"],
                ["O", "O", "O", "X", "X", "X", "X", "O", "X", "O", "X", "X", "O", "O", "O", "O", "X", "O", "X", "O"],
                ["O", "O", "O", "X", "X", "O", "O", "X", "O", "O", "O", "X", "X", "X", "O", "O", "X", "O", "O", "X"],
                ["O", "O", "O", "O", "O", "O", "O", "X", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["X", "O", "O", "O", "O", "X", "O", "X", "O", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "X"],
                ["O", "O", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X"],
                ["O", "O", "O", "X", "O", "X", "O", "O", "X", "X", "O", "X", "O", "X", "X", "O", "X", "X", "X", "O"],
                ["O", "O", "O", "O", "X", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "X"],
                ["O", "O", "X", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "X", "O"],
                ["X", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "X", "O", "X", "O"],
                ["O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "X", "O", "X", "X", "X", "O", "X", "X", "O", "O"],
                ["X", "X", "O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X"],
                ["O", "X", "O", "O", "X", "X", "X", "O", "O", "O", "X", "X", "X", "X", "X", "O", "X", "O", "O", "O"],
                ["O", "O", "X", "X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "X", "O", "X", "O", "O", "O", "O"],
                ["X", "O", "O", "X", "O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "X"],
                ["X", "O", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "X", "O", "X", "O", "O", "O", "O"],
                ["O", "X", "X", "O", "O", "O", "X", "X", "X", "O", "X", "O", "X", "O", "X", "X", "X", "X", "O", "O"],
                ["O", "X", "O", "O", "O", "O", "X", "X", "O", "O", "X", "O", "X", "O", "O", "X", "O", "O", "X", "X"],
                ["O", "O", "O", "O", "O", "O", "X", "X", "X", "X", "O", "X", "O", "O", "O", "X", "X", "O", "O", "O"]],
               [['X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                ['X', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'],
                ['O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'O'],
                ['O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X'],
                ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                ['X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X'],
                ['O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
                ['O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
                ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'O'],
                ['X', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'O'],
                ['O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O'],
                ['X', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X'],
                ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O'],
                ['O', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O'],
                ['X', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X'],
                ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O'],
                ['O', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O'],
                ['O', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'X'],
                ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'O']]),
              ]
for test_board, expected_output in test_cases:
    capture_surrounded_regions(test_board)
    assert test_board == expected_output
