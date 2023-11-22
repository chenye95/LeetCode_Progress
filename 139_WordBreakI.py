"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
 of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
from functools import lru_cache
from typing import List


def word_break_no_cache(s: str, word_dict: List[str]) -> bool:
    """
    :param s: string to break down into words
    :param word_dict: acceptable words in the dict. All strings of word_dict are unique.
    :return: whether it is possible to split s into list of words, such that word concatenates to s, and all words
        appear in word_dict
    """
    beginning_letters = {w[0] for w in word_dict}
    memory = {len(s): True}

    def split_into_sentences(start_at: int) -> bool:
        """
        Depth First Search with Memorization

        :return: can split s[start_at:] into list of words
        """
        if start_at not in memory:
            if s[start_at] not in beginning_letters:
                memory[start_at] = False
            elif s[start_at:] in word_dict:
                memory[start_at] = True
            else:
                memory[start_at] = any(s[start_at:end_at] in word_dict and split_into_sentences(end_at)
                                       for end_at in range(start_at + 1, len(s)))
        return memory[start_at]

    return split_into_sentences(0)


def word_break_cache(s: str, word_dict: List[str]) -> bool:
    beginning_letters = {w[0] for w in word_dict}

    @lru_cache(maxsize=300)
    def split_into_sentences(start_at: int) -> bool:
        """
        Depth First Search with Memorization

        :return: can split s[start_at:] into list of words
        """
        if s[start_at] not in beginning_letters:
            return False
        elif s[start_at:] in word_dict:
            return True
        else:
            return any(s[start_at:end_at] in word_dict and split_into_sentences(end_at)
                       for end_at in range(start_at + 1, len(s)))

    return split_into_sentences(0)


test_cases = [("catsanddog", ["cat", "cats", "and", "sand", "dog"], True),
              ("leetcode", ["leet", "code"], True),
              ("applepenapple", ["apple", "pen"], True),
              ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"], True),
              ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
              ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
               ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], False),
              ("bccdbacdbdacddabbaaaadababadad",
               ["cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad", "dac", "ba", "aa", "bd", "abab", "bb", "dbda", "cb",
                "caccc", "d", "dd", "aadb", "cc", "b", "bcc", "bcd", "cd", "cbca", "bbd", "ddd", "dabb", "ab", "acd",
                "a", "bbcc", "cdcbd", "cada", "dbca", "ac", "abacd", "cba", "cdb", "dbac", "aada", "cdcda", "cdc",
                "dbc", "dbcb", "bdb", "ddbdd", "cadaa", "ddbc", "babb"], True),
              ]
for word_break in [word_break_no_cache, word_break_cache, ]:
    for test_s, test_dict, expected_output in test_cases:
        assert word_break(test_s, test_dict) is expected_output, word_break.__name__
