"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list
 of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
"""
from typing import List


def find_all_concatenated_words(words: List[str]) -> List[str]:
    def dfs_recurse(current_word: str) -> bool:
        nonlocal word_set
        for i in range(1, len(current_word)):
            if current_word[:i] in word_set and (current_word[i:] in word_set or dfs_recurse(current_word[i:])):
                return True

        return False

    word_set = frozenset(words)
    return list(filter(dfs_recurse, words))


assert find_all_concatenated_words(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat",
                                    "ratcatdogcat"]) == ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
