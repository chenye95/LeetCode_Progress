"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order
 of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
 given words are sorted lexicographical-y in this alien language.
"""
from typing import List


def is_alien_word_list_sorted(words: List[str], order: str) -> bool:
    """
    :param words: list of words consists of lowercase english letter
    :param order: a permutation of lowercase letters
    :return: whether the word list is sorted according to order
    """
    order_map = {c: i for i, c in enumerate(order)}

    # sequentially compare lexicographical order of word[i] and word[i + 1]
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                # "apple" and "app"
                return False
            if words[i][j] != words[i + 1][j]:
                if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                    return False
                # else order_map[words[i][j]] < order_map[words[i + 1][j]]
                # and words[i] is lexicographically smaller than words[i + 1]
                break

    return True


test_cases = [(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
              (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
              (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False), ]
for test_word_list, test_order, expected_output in test_cases:
    assert is_alien_word_list_sorted(test_word_list, test_order) is expected_output
