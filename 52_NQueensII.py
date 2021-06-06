"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""
from typing import List


def total_n_queens_solutions(n: int) -> int:
    """
    :param n: placing n queens on an nxn chessboard, such that no two queens will attack each other, 1 <= n <= 9
    :return: total number of solutions to the n queens puzzle
    """

    def place_one_queen_on_row(current_row: int,
                               column_attack: List[bool],
                               diagonal_attack: List[bool], anti_diagonal_attack: List[bool]) -> int:
        """
        :param current_row: trying to place a queen on current_row
        :param column_attack: True if a queen already exists on the ith column
        :param diagonal_attack: True if a queen already exists on a diagonal
        :param anti_diagonal_attack: True if a queen already exists on a diagonal
        :return: number of solutions given existing placement
        """
        if current_row == n:
            return 1

        solution_count = 0
        for choose_col in range(n):
            current_diagonal = current_row - choose_col
            current_anti_diagonal = current_row + choose_col
            if column_attack[choose_col] or \
                    diagonal_attack[current_diagonal] or \
                    anti_diagonal_attack[current_anti_diagonal]:
                continue

            column_attack[choose_col] = diagonal_attack[current_diagonal] = \
                anti_diagonal_attack[current_anti_diagonal] = True

            solution_count += place_one_queen_on_row(current_row + 1,
                                                     column_attack, diagonal_attack, anti_diagonal_attack)

            column_attack[choose_col] = diagonal_attack[current_diagonal] = \
                anti_diagonal_attack[current_anti_diagonal] = False

        return solution_count

    return place_one_queen_on_row(0, [False] * n, [False] * (2 * n), [False] * (2 * n))


test_cases = [(1, 1),
              (2, 0),
              (3, 0),
              (4, 2),
              (5, 10),
              (6, 4),
              (7, 40),
              (8, 92),
              (9, 352), ]
for test_n, expected_count in test_cases:
    assert total_n_queens_solutions(test_n) == expected_count
