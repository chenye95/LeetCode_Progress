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
        T = lambda: defaultdict(T)  # Template class used to construct trie
        self.trie = T()
        for w in words:
            reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.possible_list = []

    def query(self, letter: str) -> bool:
        self.possible_list = [node[letter] for node in self.possible_list + [self.trie] if letter in node]
        return any('#' in node for node in self.possible_list)


streamChecker = StreamChecker(["cd","f","kl"])# init the dictionary.
assert not streamChecker.query('a');          # return false
assert not streamChecker.query('b');          # return false
assert not streamChecker.query('c');          # return false
assert streamChecker.query('d');              # return true, because 'cd' is in the wordlist
assert not streamChecker.query('e');          # return false
assert streamChecker.query('f');              # return true, because 'f' is in the wordlist
assert not streamChecker.query('g');          # return false
assert not streamChecker.query('h');          # return false
assert not streamChecker.query('i');          # return false
assert not streamChecker.query('j');          # return false
assert not streamChecker.query('k');          # return false
assert streamChecker.query('l');              # return true, because 'kl' is in the wordlist
