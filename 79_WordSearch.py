"""
Given a 2D current_board_state and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List


def _dfs_helper(current_board_state: List[List[str]], i: int, j: int, remaining_word: str):
    """
    Depth first search helper function

    :param current_board_state: reference to the board
    :param i: row i
    :param j: column j
    :param remaining_word: remaining_word to be found on the board
    :return: whether remaining_word can be found in current_board_state
    """
    if not remaining_word:
        return True
    if i < 0 or i >= len(current_board_state) or j < 0 or j >= len(current_board_state[0]) or \
            remaining_word[0] != current_board_state[i][j]:
        return False
    current_board_state[i][j] = ''
    rest_of_word = remaining_word[1:]
    return_result = _dfs_helper(current_board_state, i - 1, j, rest_of_word) or \
                    _dfs_helper(current_board_state, i + 1, j, rest_of_word) or \
                    _dfs_helper(current_board_state, i, j - 1, rest_of_word) or \
                    _dfs_helper(current_board_state, i, j + 1, rest_of_word)
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
    return any(_dfs_helper(board, i, j, word) for i in range(len(board)) for j in range(len(board[0])))


test_cases = [([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB", False),
              ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED", True),
              ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE", True), ]
for test_board, test_word, expected_output in test_cases:
    assert exist(board=test_board, word=test_word) is expected_output
