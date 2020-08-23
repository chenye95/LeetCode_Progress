"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to
newest, including this letter just queried) spell one of the words in the given list.
"""
from collections import defaultdict
from functools import reduce
from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        """
        Create reversed word trie for lookup
        :param words: list of words acceptable in StreamChecker
        """
        trie = lambda: defaultdict(trie)  # Template class used to construct trie_root
        self.trie_root = trie()
        for w in words:
            # reverse word lookup
            reduce(dict.__getitem__, w[::-1], self.trie_root)['#'] = True
        self.trailing_string = ""
        # for optimization, don't need to carry too long a trailing string
        self.max_word_len = max(map(len, words))

    def query(self, letter: chr) -> bool:
        """
        :param letter: query letter by letter
        :return: returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to
        newest, including this letter just queried) spell one of the words in the given list.
        """

        # revered word string
        self.trailing_string = (letter + self.trailing_string)[:self.max_word_len]

        current_node = self.trie_root
        for c in self.trailing_string:
            if c in current_node:
                current_node = current_node[c]
                if current_node['#']:
                    return True
            else:
                break

        return False


streamChecker = StreamChecker(["cd", "f", "kl"])  # init the dictionary.
assert not streamChecker.query('a');  # return false
assert not streamChecker.query('b');  # return false
assert not streamChecker.query('c');  # return false
assert streamChecker.query('d');  # return true, because 'cd' is in the wordlist
assert not streamChecker.query('e');  # return false
assert streamChecker.query('f');  # return true, because 'f' is in the wordlist
assert not streamChecker.query('g');  # return false
assert not streamChecker.query('h');  # return false
assert not streamChecker.query('i');  # return false
assert not streamChecker.query('j');  # return false
assert not streamChecker.query('k');  # return false
assert streamChecker.query('l');  # return true, because 'kl' is in the wordlist
