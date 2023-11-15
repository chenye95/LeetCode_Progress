"""
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board,
 and alternating direction each row.

You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square
 x, consists of the following:
- You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
    - (This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations,
     regardless of the size of the board.)
- If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.

A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or
 ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of
 another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first
 move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.
 )

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.
"""
from collections import deque
from typing import List


def snakes_and_ladders(board: List[List[int]]) -> int:
    """
    :param board: 2 <= len(board) == len(board[0]) <= 20. board[i][j] is between 1 and n * n, or -1
        board square with number 1 or n * n has no snake or ladder
    :return: min step needed to reach square n * n
    """
    n = len(board)

    visited = [False] * (n * n)
    visited[0] = True
    visiting = deque([(1, 0)])

    while visiting:
        current_block, current_step = visiting.popleft()
        for next_block in range(current_block + 1, current_block + 7):
            x, y = (next_block - 1) // n, (next_block - 1) % n
            # ~i = -i - 1
            next_block_val = board[~x][y if x % 2 == 0 else ~y]
            if next_block_val > 0:
                next_block = next_block_val
            if next_block == n * n:
                return current_step + 1
            if not visited[next_block - 1]:
                visited[next_block - 1] = True
                visiting.append((next_block, current_step + 1))

    return -1


test_cases = [([[-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1]], 4),
              ([[1, 1, -1],
                [1, 1, 1],
                [-1, 1, 1]], -1),
              ([[-1, -1, -1, 104, -1, -1, -1, -1, 60, 7, -1],
                [-1, -1, 101, -1, 52, -1, -1, -1, -1, -1, -1],
                [100, -1, -1, 85, -1, -1, 10, -1, -1, -1, -1],
                [-1, -1, -1, 6, -1, -1, -1, 37, -1, -1, 20],
                [-1, -1, -1, -1, -1, 27, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, 94, 4],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, 51, 97],
                [43, -1, -1, -1, -1, 22, -1, -1, -1, -1, 86],
                [-1, -1, -1, -1, 89, 92, -1, -1, -1, -1, 75],
                [-1, -1, -1, -1, -1, -1, 41, -1, -1, -1, 3],
                [-1, -1, 112, -1, -1, -1, 120, 19, -1, -1, -1]], 2),
              ([[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, 194, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, 14, -1, -1, 107, 236, -1, -1, -1, -1, -1, -1, -1, -1, 227],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, 109, -1, -1, -1, -1, 6, 81],
                [-1, 58, -1, -1, -1, 128, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, 242, -1, -1, -1, -1, -1, 154, 127, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, 249, 144, -1, 220, -1, -1, -1, -1, -1, -1, -1],
                [-1, 102, -1, -1, -1, -1, 37, -1, -1, -1, 9, -1, -1, 195, -1, 98],
                [-1, -1, -1, 69, 203, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 108],
                [-1, -1, -1, -1, -1, -1, 125, -1, -1, -1, 135, -1, -1, -1, 140, 111],
                [-1, -1, -1, 135, -1, -1, -1, -1, 14, -1, 60, -1, -1, -1, -1, -1],
                [-1, -1, 142, -1, -1, 109, -1, -1, -1, 178, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 158, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 190, 229, -1],
                [-1, 135, -1, -1, -1, -1, 221, -1, -1, -1, -1, 254, -1, -1, -1, -1],
                [-1, 192, -1, -1, 184, 175, -1, 89, -1, 246, -1, -1, -1, -1, -1, -1]], 4),
              ([[-1, -1, -1, 46, 47, -1, -1, -1],
                [51, -1, -1, 63, -1, 31, 21, -1],
                [-1, -1, 26, -1, -1, 38, -1, -1],
                [-1, -1, 11, -1, 14, 23, 56, 57],
                [11, -1, -1, -1, 49, 36, -1, 48],
                [-1, -1, -1, 33, 56, -1, 57, 21],
                [-1, -1, -1, -1, -1, -1, 2, -1],
                [-1, -1, -1, 8, 3, -1, 6, 56]], 4),
              ]
for test_board, expected_step in test_cases:
    assert snakes_and_ladders(test_board) == expected_step
