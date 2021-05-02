"""
Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:
- WordFilter(string[] words) Initializes the object with the words in the dictionary.
- search(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the
 suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the
 dictionary, return -1.
"""
from collections import defaultdict
from itertools import zip_longest
from typing import List

Trie = lambda: defaultdict(Trie)
_HOLDS_WORD_I = "#_#"


class WordFilter:
    def __init__(self, words: List[str]):
        """
        :param words: dictionary of words to be searched from
        """
        self.words = words

    def search(self, prefix: str, suffix: str) -> int:
        """
        :param prefix: searching for word that has prefix equals to prefix
        :param suffix: searching for word that has suffix equals to suffix
        :return: largest index in self.words that has prefix and suffix, or -1 if no such word exists
        """
        pass


class WordFilterPaired(WordFilter):
    def __init__(self, words: List[str]):
        """
        Store (prefix_c, suffix_c) pair in Trie to search for prefix and suffix in the same trie structure.
        Also store (prefix_c, None) and (None, suffix_c) pair to support len(prefix) != len(suffix)

        :param words: dictionary of words to be searched from
        """
        super().__init__(words)
        self.trie = Trie()

        for word_i, word in enumerate(words):
            current_node = self.trie

            for position_j, word_c in enumerate(word):
                # add (prefix_c, None)
                tmp_node = current_node
                for word_letter in word[position_j:]:
                    tmp_node = tmp_node[word_letter, None]
                    tmp_node[_HOLDS_WORD_I] = word_i

                # add (None, suffix_c)
                tmp_node = current_node
                for word_letter in word[:-position_j][::-1]:
                    tmp_node = tmp_node[None, word_letter]
                    tmp_node[_HOLDS_WORD_I] = word_i

                # add (prefix_c, suffix_c)
                current_node = current_node[word_c, word[-position_j - 1]]
                current_node[_HOLDS_WORD_I] = word_i

        self.trie[_HOLDS_WORD_I] = len(words) - 1

    def search(self, prefix: str, suffix: str) -> int:
        """
        :param prefix: searching for word that has prefix equals to prefix
        :param suffix: searching for word that has suffix equals to suffix
        :return: largest index in self.words that has prefix and suffix, or -1 if no such word exists
        """
        current_node = self.trie
        for prefix_c, suffix_c in zip_longest(prefix, suffix[::-1], fillvalue=None):
            if (prefix_c, suffix_c) not in current_node:
                return -1
            current_node = current_node[prefix_c, suffix_c]
        return current_node[_HOLDS_WORD_I]


class WordFilterWrapped(WordFilter):
    concat_chr = '#'

    def __init__(self, words: List[str]):
        """
        Store suffix + '#' + prefix in trie.

        :param words: dictionary of words to be searched from
        """
        super().__init__(words)
        self.trie = Trie()

        for word_i, word in enumerate(words):
            word += self.concat_chr

            for position_j in range(len(word)):
                # "apple" => ["apple#apple", "pple#apple", "ple#apple", "le#apple", "e#apple", "#apple"]
                current_node = self.trie
                current_node[_HOLDS_WORD_I] = word_i
                # print(word)
                # print([word[position_k % len(word)] for position_k in range(position_j, 2 * len(word) - 1)])
                for position_k in range(position_j, 2 * len(word) - 1):
                    current_node = current_node[word[position_k % len(word)]]
                    current_node[_HOLDS_WORD_I] = word_i

    def search(self, prefix: str, suffix: str) -> int:
        """
        :param prefix: searching for word that has prefix equals to prefix
        :param suffix: searching for word that has suffix equals to suffix
        :return: largest index in self.words that has prefix and suffix, or -1 if no such word exists
        """
        current_node = self.trie
        for letter in suffix + self.concat_chr + prefix:
            if letter not in current_node:
                return -1
            current_node = current_node[letter]
        return current_node[_HOLDS_WORD_I]


class WordFilterSetIntersection(WordFilter):
    def __init__(self, words: List[str]):
        """
        Store suffix + '#' + prefix in trie.

        :param words: dictionary of words to be searched from
        """
        super().__init__(words)

        self.prefix_set = defaultdict(set)
        self.suffix_set = defaultdict(set)

        seen_in_dictionary = set()
        for word_i in range(len(words) - 1, -1, -1):
            word = words[word_i]
            if word in seen_in_dictionary:
                continue
            seen_in_dictionary.add(word)

            for position_j in range(len(word) + 1):
                self.prefix_set[word[:position_j]].add(word_i)
                self.suffix_set[word[position_j:]].add(word_i)

    def search(self, prefix: str, suffix: str) -> int:
        """
        :param prefix: searching for word that has prefix equals to prefix
        :param suffix: searching for word that has suffix equals to suffix
        :return: largest index in self.words that has prefix and suffix, or -1 if no such word exists
        """
        prefix_match = self.prefix_set[prefix]
        suffix_match = self.suffix_set[suffix]
        both_match = prefix_match & suffix_match
        return max(both_match) if both_match else -1


test_cases = [(["apple", "pear"], [('a', 'e', 0), ('ap', 'e', 0), ('aq', 'e', -1), ('e', 'e', -1), ('', '', 1),
                                   ('p', 'r', 1), ('p', '', 1), ("pear", "r", 1), ]),
              (["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca",
                "ababccabcb", "caccbbcbab", "bccbacbcba"],
               [("bccbacbcba", "a", 9), ("ab", "abcaccbcaa", 4), ("a", "aa", 5), ("cabaaba", "abaaaa", 0),
                ("cacc", "accbbcbab", 8), ("ccbcab", "bac", 1), ("bac", "cba", 2), ("ac", "accabaccaa", 5),
                ("bcbb", "aa", 3), ("ccbca", "cbcababac", 1), ("c", "b", 8), ("b", "a", 9), ]), ]
for word_filter_type in [WordFilterSetIntersection, WordFilterPaired, WordFilterWrapped, ]:
    for test_dictionary, test_query in test_cases:
        test_search = word_filter_type(words=test_dictionary)
        for test_prefix, test_suffix, expected_output in test_query:
            assert test_search.search(prefix=test_prefix, suffix=test_suffix) == expected_output
