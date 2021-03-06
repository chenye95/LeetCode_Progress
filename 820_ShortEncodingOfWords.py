"""
A valid encoding of an array of words_set is any reference string s and array of indices indices such that:
- words_set.length == indices.length
- The reference string s ends with the '#' character.
- For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#'
character is equal to words_set[i].

Given an array of words_set, return the length of the shortest reference string s possible of any valid encoding of
words_set.
"""
from collections import defaultdict
from functools import reduce
from typing import List


def minimum_length_encoding_suffix(words: List[str]) -> int:
    """
    if y is a suffix of x, then y does not show up in the encoding as a separate word
    """
    encoding_candidate = set(words)
    for word in words:
        for k in range(1, len(word)):
            # find all suffix of word and discard from candidate set
            encoding_candidate.discard(word[k:])

    return sum(len(word) + 1 for word in encoding_candidate)


def minimum_length_encoding_trie(words: List[str]) -> int:
    """
    Insert word backwards into trie to build a suffix trie
    """
    trie_struct = lambda: defaultdict(trie_struct)
    trie = trie_struct()
    # first remove duplicates from word list
    # then build tree_struct: insert word backwards for suffix instead of prefix tree
    # dict.__getitem__ will return a nonempty Trie node if word is suffix of another word, or empty one if otherwise
    word_in_trie = [(word, reduce(dict.__getitem__, word[::-1], trie)) for word in set(words)]

    # only sum up length of words that returns an empty Trie Node
    return sum(len(word) + 1
               for word, word_i_trie in word_in_trie
               if not word_i_trie)


test_cases = [(["time", "time", "me", "bell"], 10),
              (["time", "me", "bell"], 10),
              (["t"], 2), ]
for minimum_length_encoding in [minimum_length_encoding_trie, minimum_length_encoding_suffix]:
    for test_input, expected_output in test_cases:
        assert minimum_length_encoding(test_input) == expected_output
