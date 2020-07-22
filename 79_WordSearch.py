"""
Given a 2D current_board_state and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List


def dfs_solution(current_board_state: List[List[str]], i: int, j: int, remaining_word: str):
    """
    :param current_board_state: reference to the board
    :param i: row i
    :param j:  column j
    :param remaining_word: remaining_word to be found on the board
    :return: whether remaining_word can be found in current_board_state
    """
    if not remaining_word:
        return True
    if i < 0 or i >= len(current_board_state) or j < 0 or j >= len(current_board_state[0]) or remaining_word[0] != \
            current_board_state[i][j]:
        return False
    current_board_state[i][j] = ''
    rest_of_word = remaining_word[1:]
    return_result = dfs_solution(current_board_state, i - 1, j, rest_of_word) or dfs_solution(current_board_state,
                                                                                              i + 1, j, rest_of_word) or \
                    dfs_solution(current_board_state, i, j - 1, rest_of_word) or dfs_solution(current_board_state, i,
                                                                                              j + 1, rest_of_word)
    current_board_state[i][j] = remaining_word[0]
    return return_result


def exist(board: List[List[str]], word: str) -> bool:
    """
    :param board: 2D current_board_state of lowercase and uppercase English letters
    :param word: 1 <= word.length <= 1000
    :return: whether word can be found on the current_board_state
    """
    if not board or not board[0]:
        return False
    if not word:
        return True
    return any(dfs_solution(board, i, j, word) for i in range(len(board)) for j in range(len(board[0])))


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
assert exist(board, "ABCB") is False
assert exist(board, "ABCCED") is True
assert exist(board, "SEE") is True
