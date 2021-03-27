"""
Design a data structure that supports the following two operations:
- void addWord(word)
- bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or '.'
A . means it can represent any one letter.
"""
from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.end_of_word = '$'
        TrieNode = lambda: defaultdict(TrieNode)
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """
        Adds a word into WordDictionary

        :param word: all words are consist of lowercase letters a-z
        """
        current_node = self.root
        for letter in word:
            current_node = current_node[letter]
        # '#' represents End Of Word
        current_node[self.end_of_word] = None

    def search(self, word: str) -> bool:
        """
        :param word: only contains a-z or dot character '.' to represent any letter
        :return: whether word exists in WordDictionary
        """
        current_nodes = [self.root]
        for letter in word + self.end_of_word:
            current_nodes = [kid_node for node in current_nodes
                             for kid_node in ([node[letter]] if letter in node
                                              else filter(None, node.values()) if letter == '.' else [])
                             ]
            # filter(None, node.values()) filter out end of word
        return bool(current_nodes)


test_dict = WordDictionary()
test_dict.add_word("bad")
test_dict.add_word("dad")
test_dict.add_word("mad")
assert test_dict.search("pad") is False
assert test_dict.search("bad") is True
assert test_dict.search(".ad") is True
assert test_dict.search("b..") is True

test_dict = WordDictionary()
test_dict.add_word('a')
test_dict.add_word('a')
assert test_dict.search('a') is True
assert test_dict.search('.') is True
assert test_dict.search('a') is True
assert test_dict.search('aa') is False
assert test_dict.search('.a') is False
assert test_dict.search('a.') is False
