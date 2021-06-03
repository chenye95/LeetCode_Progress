"""
208 Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
 dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
    otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix,
    and false otherwise.
"""
from collections import defaultdict


class Trie:
    def __init__(self, chr_match_all_letters: chr = '.'):
        """
        Initialize data structure here.
        """
        _Trie_Node = lambda: defaultdict(_Trie_Node)
        self.end_of_word = '$' if chr_match_all_letters != '$' else '.'
        self.chr_match_all_letters = chr_match_all_letters
        self.root = _Trie_Node()

    def insert(self, word: str) -> None:
        """
        :param word: inserts a word into the trie. 1 <= len(word) <= 2000 and consists of lowercase english letters only
        """
        current_node = self.root
        for letter in word:
            current_node = current_node[letter]
        # self.end_of_word represents End Of Word
        current_node[self.end_of_word] = None

    def search(self, word: str) -> bool:
        """
        :param: May contain self.chr_match_all_letters to represent any letter
        :return: if the word is in the trie
        """
        current_nodes = [self.root]
        for letter in word + self.end_of_word:
            current_nodes = [kid_node for node in current_nodes
                             for kid_node in ([node[letter]] if letter in node else
                                              filter(None, node.values()) if letter == self.chr_match_all_letters
                                              else [])
                             ]
            # filter(None, node.values()) filter out self.end_of_word
            if not current_nodes:
                return False

        return True

    def starts_with(self, prefix: str) -> bool:
        """
        :param: may contain self.chr_match_all_letters to represent any letter
        :return: if there is any word in the trie that starts with the given prefix
        """
        current_nodes = [self.root]
        for letter in prefix:
            current_nodes = [kid_node for node in current_nodes
                             for kid_node in ([node[letter]] if letter in node else
                                              filter(None, node.values()) if letter == self.chr_match_all_letters
                                              else [])
                             ]
            # filter(None, node.values()) filter out self.end_of_word
            if not current_nodes:
                return False

        return True

    def get_words_start_with(self, prefix: str, max_recommendation: int):
        """
        :param prefix: string starts with, case sensitive, prefix. Does not support self.chr_match_all_letters
        :param max_recommendation: max length of the returned list
        :return: list of words, in alphabetical order, that starts with prefix
        """

        def dfs_explore_words(exploring_node: defaultdict, word_so_far: str) -> None:
            for c in sorted(exploring_node.keys()):
                if c != self.end_of_word:
                    if len(words_list) < max_recommendation:
                        dfs_explore_words(exploring_node[c], word_so_far + c)
                else:
                    words_list.append(word_so_far)

                if len(words_list) >= max_recommendation:
                    return

        current_node = self.root
        for c in prefix:
            if c not in current_node:
                return []
            else:
                current_node = current_node[c]

        words_list = []
        dfs_explore_words(current_node, prefix)
        return words_list
