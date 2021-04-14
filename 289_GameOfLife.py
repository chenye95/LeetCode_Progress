"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the
 British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead
 (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following
  four rules (taken from the above Wikipedia article):
    - Any live cell with fewer than two live neighbors dies as if caused by under-population.
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies, as if by over-population.
    - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births
 and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""
from collections import Counter
from copy import deepcopy
from typing import List


def game_of_life_copy(board: List[List[int]]) -> None:
    """
    This method makes a deep copy of the board to evaluate next iteration in game of life

    :param board: board of 0 and 1, indicating whether the cell is alive or dead; assuming board is valid
    :return: None; in place modification of board to display next state in the evolution of game of life
    """
    neighbor_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    n_rows, n_cols = len(board), len(board[0])

    copy_board = deepcopy(board)
    for row in range(n_rows):
        for col in range(n_cols):
            # For each cell count the number of live neighbors.
            living_neighbors = 0
            for d_row, d_col in neighbor_cells:
                r = row + d_row
                c = col + d_col
                if 0 <= r < n_rows and 0 <= c < n_cols and copy_board[r][c]:
                    living_neighbors += 1

            if copy_board[row][col] and (living_neighbors < 2 or living_neighbors > 3):
                board[row][col] = 0
            elif not copy_board[row][col] and living_neighbors == 3:
                board[row][col] = 1


def game_of_life_in_place(board: List[List[int]]) -> None:
    """
    This method updates board in place without making a copy

    :param board: board of 0 and 1, indicating whether the cell is alive or dead; assuming board is valid
    :return: None; in place modification of board to display next state in the evolution of game of life
    """
    neighbor_cells = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    n_rows, n_cols = len(board), len(board[0])

    # Iterate through board cell by cell.
    for row in range(n_rows):
        for col in range(n_cols):
            # For each cell count the number of live neighbors.
            living_neighbors = 0
            for d_row, d_col in neighbor_cells:
                # row and column of the neighboring cell
                r = row + d_row
                c = col + d_col

                # Check the validity of the neighboring cell and if it was originally a live cell.
                if 0 <= r < n_rows and 0 <= c < n_cols and abs(board[r][c]) == 1:
                    living_neighbors += 1

            if board[row][col] == 1 and (living_neighbors < 2 or living_neighbors > 3):
                # -1 signifies the cell is now dead but originally was live.
                board[row][col] = -1
            elif board[row][col] == 0 and living_neighbors == 3:
                # 2 signifies the cell is now live but was originally dead.
                board[row][col] = 2

    # Get the final representation for the newly updated board.
    for row in range(n_rows):
        for col in range(n_cols):
            board[row][col] = 1 if board[row][col] > 0 else 0


def game_of_life_counter(board: List[List[int]]) -> None:
    """
    This method uses counter to deal with large size board with sparse living cells

    :param board: board of 0 and 1, indicating whether the cell is alive or dead; assuming board is valid
    :return: None; in place modification of board to display next state in the evolution of game of life
    """
    living_cells = {(i, j) for i, row in enumerate(board) for j, is_alive in enumerate(row) if is_alive}
    n_rows, n_cols = len(board), len(board[0])
    neighbor_cells = Counter((i + d_i, j + d_j)
                             for d_i, d_j in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
                             for i, j in living_cells
                             if 0 <= i + d_i < n_rows and 0 <= j + d_j < n_cols)
    living_cells = {i_j for i_j in neighbor_cells
                    if neighbor_cells[i_j] == 3 or neighbor_cells[i_j] == 2 and i_j in living_cells}
    for i, row in enumerate(board):
        for j in range(n_cols):
            row[j] = int((i, j) in living_cells)


test_cases = [([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
              ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
              ([[1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
                [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
                [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
                [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]],
               [[1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]), ]
for game_of_life_next_state in [game_of_life_counter, game_of_life_copy, game_of_life_in_place]:
    for test_input, expected_output in test_cases:
        input_board = deepcopy(test_input)
        game_of_life_next_state(input_board)
        assert input_board == expected_output, game_of_life_next_state.__name__
