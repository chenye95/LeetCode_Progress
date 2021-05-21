"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the
 answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the
 pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and
 no two letters map to the same letter.
"""
from typing import List


def find_and_replace_pattern_two_maps(words: List[str], pattern: str) -> List[str]:
    """
    :param words: list of words with 1 <= len(words) <= 50
    :param pattern: 1 <= len(pattern) <= 20
    :return: filtered list of words that match patterns
    """

    def match(word_i: str) -> bool:
        """
        :return: whether word_i matches pattern
        """
        if len(word_i) != len(pattern):
            return False

        pattern_mapping = {}  # c_pattern -> c_word
        word_mapping = {}  # c_word -> c_pattern
        for c_word, c_pattern in zip(word_i, pattern):
            if word_mapping.setdefault(c_word, c_pattern) != c_pattern or \
                    pattern_mapping.setdefault(c_pattern, c_word) != c_word:
                return False

        return True

    return list(filter(match, words))


def find_and_replace_pattern_one_map(words: List[str], pattern: str) -> List[str]:
    """
    :param words: list of words with 1 <= len(words) <= 50
    :param pattern: 1 <= len(pattern) <= 20
    :return: filtered list of words that match patterns
    """

    def match(word_i: str) -> bool:
        """
        :return: whether word_i matches pattern
        """
        if len(word_i) != len(pattern):
            return False

        pattern_mapping = {}  # c_pattern -> c_word
        for c_word, c_pattern in zip(word_i, pattern):
            if pattern_mapping.setdefault(c_pattern, c_word) != c_word:
                # c_pattern has assignment already
                return False

        return len(set(pattern_mapping.values())) == len(pattern_mapping.values())

    return list(filter(match, words))


test_cases = [(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),
              (["a", "b", "c"], "a", ["a", "b", "c"]),
              (["n", "a", "g", "a", "l", "w", "w", "p", "y", "x", "n", "k", "i", "e", "o", "m", "a", "a", "f", "g", "l",
                "x", "y", "h", "r", "o", "x", "h", "l", "p", "k", "k", "f", "t", "v", "q", "o", "w", "w", "a", "r", "a",
                "k", "f", "f", "l", "b", "s", "m", "w"], "s",
               ["n", "a", "g", "a", "l", "w", "w", "p", "y", "x", "n", "k", "i", "e", "o", "m", "a", "a", "f", "g", "l",
                "x", "y", "h", "r", "o", "x", "h", "l", "p", "k", "k", "f", "t", "v", "q", "o", "w", "w", "a", "r", "a",
                "k", "f", "f", "l", "b", "s", "m", "w"]),
              (["esgbvddwzs", "hqpvqqcosc", "dfgtclfpoq", "zkkcnbkwyq", "rtaxswoptc", "ropijxohad", "agoioogsmm",
                "mzvgifikfn", "vqpkaanrro", "lvwuaothgo", "unlwvssqqf", "cgzdugkokx", "ykmplzqpec", "bgehpsysqh",
                "wvtttuoghy", "elbomhahou", "acluusiypb", "hmbxknagjp", "nrenkpsijo", "vqtspqdqsb", "aswaosxjkp",
                "ramhaukosa", "dwkazvicoh", "coauoglbbg", "jkquhfmmrk", "ctbsbvfcud", "gxwjaglmrl", "jdpuiktvte",
                "izzwrckruq", "uagvcowmpy", "xadrhbhzvo", "xpckmjshce", "hpsaounlyy", "yqdlytowhq", "sspkkigqrj",
                "oifztsarjn", "ygdsnckxkw", "mwsthxzxvv", "ctzoejspeo", "btavhzxzpo", "tcuwnkktnf", "vjaqnrnqja",
                "ghnmkckhvu", "auuknqbuxw", "algvaentpg", "fhqmzenotz", "wljirchwgk", "mupkjobuup", "dgshxrwcbl",
                "ufmjumyuah"], "quepdxzarc",
               ["hmbxknagjp", "dwkazvicoh", "uagvcowmpy", "oifztsarjn", "dgshxrwcbl"]), ]
for find_and_replace_pattern in [find_and_replace_pattern_one_map, find_and_replace_pattern_two_maps, ]:
    for test_words, test_pattern, expected_output in test_cases:
        assert find_and_replace_pattern(test_words, test_pattern) == expected_output, find_and_replace_pattern.__name__
