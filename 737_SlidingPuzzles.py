"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is
impossible for the state of the board to be solved, return -1.
"""
from collections import deque
from typing import List


def slidingPuzzle(board: List[List[int]]) -> int:
    m, n = 2, 3
    target = 123450
    start_position, zero_position = 0, 0
    for r in range(m):
        for c in range(n):
            start_position = start_position * 10 + board[r][c]
            if board[r][c] == 0:
                zero_position = m * n - 1 - r * n - c
    if start_position == target:
        return 0
    stack = deque([(start_position, zero_position, 0), ])
    visited = {(start_position, zero_position)}
    while stack:
        current_board, zero_position, step_count = stack.popleft()
        possible_next_steps = []
        if zero_position + n < m * n:
            possible_next_steps.append(zero_position + n)
        if zero_position - n >= 0:
            possible_next_steps.append(zero_position - n)
        if zero_position % n > 0:
            possible_next_steps.append(zero_position - 1)
        if zero_position % n < n - 1:
            possible_next_steps.append(zero_position + 1)
        for next_zero in possible_next_steps:
            d = current_board // 10 ** next_zero % 10
            next_board = current_board - d * 10 ** next_zero + d * 10 ** zero_position
            if next_board == target:
                return step_count + 1
            if (next_board, next_zero) not in visited:
                visited.add((next_board, next_zero))
                stack.append((next_board, next_zero, step_count + 1))
    return -1


test_cases = [([[1, 2, 3], [4, 0, 5]], 1),
              ([[1, 2, 3], [5, 4, 0]], -1),
              ([[4, 1, 2], [5, 0, 3]], 5),
              ([[3, 2, 4], [1, 5, 0]], 14)]
for input, output in test_cases:
    assert slidingPuzzle(board=input) == output
