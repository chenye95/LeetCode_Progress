"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.
"""
from typing import List, Dict


def find_words(board: List[List[chr]], words: List[str]) -> List[str]:
    """
    :param board: a 2D board of characters
    :param words: list of strings
    :return: all word in words that can be found on the board
    """
    _end_of_word = '$'
    word_trie = {}
    for word in words:
        current_node = word_trie
        for letter in word:
            current_node = current_node.setdefault(letter, {})
        current_node[_end_of_word] = word

    total_rows, total_cols = len(board), len(board[0])
    return_list = []

    def explore_board(row: int, col: int, parent_node: Dict[chr, Dict]) -> None:
        nonlocal board, _end_of_word, return_list, total_rows, total_cols
        curr_letter = board[row][col]
        curr_node = parent_node[curr_letter]
        # Do not find repetitive words
        trie_word = curr_node.pop(_end_of_word, None)
        if trie_word:
            return_list.append(trie_word)

        board[row][col] = '#'
        for move_r, move_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = row + move_r, col + move_c
            if 0 <= next_row < total_rows and 0 <= next_col < total_cols \
                    and board[next_row][next_col] in curr_node:
                explore_board(next_row, next_col, curr_node)
        board[row][col] = curr_letter

        # Trimming for optimization
        if len(curr_node) == 0:
            parent_node.pop(curr_letter)

    for r in range(total_rows):
        for c in range(total_cols):
            if board[r][c] in word_trie:
                explore_board(r, c, word_trie)
    return return_list


test_cases = [([["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"]],
               ["oath", "pea", "eat", "rain"], {"eat", "oath"}),
              ([['a', 'b'], ['c', 'd']], ["abcd"], set()), ]
for test_board, test_words, expected_output in test_cases:
    assert set(find_words(board=test_board, words=test_words)) == expected_output
