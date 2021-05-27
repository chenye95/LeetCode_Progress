"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list
 of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
"""
from typing import List


def find_all_concatenated_words(words: List[str]) -> List[str]:
    """
    :param words: list of words without duplicates
    :return: all concatenated words in the list
    """

    def dfs_recurse(current_word: str) -> bool:
        """
        :param current_word: a word in words
        :return: whether current_word is a concatenated word or a word in word_list
        """
        for i in range(1, len(current_word)):
            if current_word[:i] in word_set and (current_word[i:] in word_set or dfs_recurse(current_word[i:])):
                return True

        return False

    word_set = frozenset(words)
    return list(filter(dfs_recurse, words))


test_cases = [(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
               {"catsdogcats", "dogcatsdog", "ratcatdogcat"}),
              (["cat", "dog", "catdog"], {"catdog", }), ]
for test_words, expected_output in test_cases:
    assert set(find_all_concatenated_words(test_words)) == expected_output
