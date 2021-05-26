"""
Given an array of strings words, return the smallest string that contains each string in words as a substring. If there
 are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.
"""
from typing import List


def shortest_super_string(words: List[str]) -> str:
    """
    :param words: 1 to 12 unique words and 1 <= len(words[i]) <= 20. words consists of lower case english letters only
    :return: shortest super string that captures all words
    """
    # Equivalent to finding the most overlaps in permutation of words
    n = len(words)

    # Populate overlap_len
    overlap_len = [[0] * n for _ in range(n)]
    for i, i_word in enumerate(words):
        overlap_word_i = overlap_len[i]
        for j, j_word in enumerate(words):
            if i != j:
                for i_j_overlap_len in range(min(len(i_word), len(j_word)), 0, -1):
                    if i_word.endswith(j_word[:i_j_overlap_len]):
                        overlap_word_i[j] = i_j_overlap_len
                        break

    # dp_memory[chosen_words][i]: most overlap among chosen words represented by chosen_words mask, ending with words[i]
    dp_memory = [[0] * n for _ in range(1 << n)]
    # used for reconstruction
    before_word_i = [[None] * n for _ in range(1 << n)]

    for chosen_words in range(1, 1 << n):
        for word_i in range(n):
            if (chosen_words >> word_i) & 1:
                # word_i is in chosen_words
                # assuming word_i is the last word added to chosen words
                remove_word_i = chosen_words ^ (1 << word_i)
                if remove_word_i == 0:
                    # only word_i is chosen
                    continue

                biggest_overlap_i, previous_insert_word = 0, None

                for word_j in range(n):
                    if (remove_word_i >> word_j) & 1:
                        # word_j also is in chosen words
                        # assuming word_j is the last one added before word_i
                        overlap_word_j_i = dp_memory[remove_word_i][word_j] + overlap_len[word_j][word_i]
                        if overlap_word_j_i > biggest_overlap_i:
                            biggest_overlap_i, previous_insert_word = overlap_word_j_i, word_j
                    elif 1 << word_j > remove_word_i:
                        break

                if biggest_overlap_i:
                    dp_memory[chosen_words][word_i] = biggest_overlap_i
                    before_word_i[chosen_words][word_i] = previous_insert_word

            elif 1 << word_i > chosen_words:
                break

    # Shorted super string will have length sum(len(word_i) for word_i in words) - max(dp_memory[-1])
    # Reconstruct shortest super string

    # Follow parents down backwards path that retains maximum overlap
    words_order = []
    need_to_insert = (1 << n) - 1
    word_i = int(max(range(n), key=dp_memory[-1].__getitem__))
    while word_i is not None:
        words_order.append(word_i)
        need_to_insert, word_i = need_to_insert ^ (1 << word_i), before_word_i[need_to_insert][word_i]

    # Reverse path to get forwards direction
    words_order = words_order[::-1]

    # Reconstruct super string from words_order
    super_string = words[words_order[0]]
    previous_word = words_order[0]
    for word_i in words_order[1:]:
        super_string += words[word_i][overlap_len[previous_word][word_i]:]
        previous_word = word_i

    # Add all remaining words, i.e. those with 0 overlap
    for word_i in range(n):
        if word_i not in words_order:
            super_string += words[word_i]

    return super_string


test_cases = [(["hello"], "hello"),
              (["alex", "loves", "leetcode"], "alexlovesleetcode"),
              (["catg", "ctaagt", "gcta", "ttca", "atgcatc"], "gctaagttcatgcatc"),
              (["cedefifgstkyxfcuajfa", "ooncedefifgstkyxfcua", "assqjfwarvjcjedqtoz", "fcuajfassqjfwarvjc",
                "fwarvjcjedqtozctcd", "zppedxfumcfsngp", "kyxfcuajfassqjfwa", "fumcfsngphjyfhhwkqa",
                "fassqjfwarvjcjedq", "ppedxfumcfsngphjyf", "dqtozctcdk"],
               "ooncedefifgstkyxfcuajfassqjfwarvjcjedqtozctcdkzppedxfumcfsngphjyfhhwkqa"),
              (["cgjufdqhfw", "bsrchpiau", "hfwbsrchpi", "sezsorql", "srchpiaues", "rqlmc"],
               "sezsorqlmcgjufdqhfwbsrchpiaues"), ]
for test_words, expected_output in test_cases:
    get_super_string = shortest_super_string(test_words)
    assert len(get_super_string) == len(expected_output)
    for word in test_words:
        assert word in get_super_string
