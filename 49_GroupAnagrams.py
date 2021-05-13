"""
Given an array of strings str_list, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.
"""
from collections import defaultdict
from typing import List


def group_anagrams(str_list: List[str]) -> List[List[str]]:
    """
    :param str_list: list of strings
    :return: list of list such that anagrams are grouped together
    """
    anagram_map = defaultdict(list)
    for s in str_list:
        anagram_map[tuple(sorted(s))].append(s)
    return [anagram_map[key] for key in anagram_map]


test_cases = [(["eat", "tea", "tan", "ate", "nat", "bat"],
               [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
              ([""], [[""]]),
              (["a"], [["a"]]),
              (["ray", "cod", "abe", "ned", "arc", "jar", "owl", "pop", "paw", "sky", "yup", "fed", "jul", "woo", "ado",
                "why", "ben", "mys", "den", "dem", "fat", "you", "eon", "sui", "oct", "asp", "ago", "lea", "sow", "hus",
                "fee", "yup", "eve", "red", "flo", "ids", "tic", "pup", "hag", "ito", "zoo"],
               [["zoo"], ["hag"], ["pup"], ["ids"], ["tic"], ["flo"], ["red"], ["fee"], ["hus"], ["fed"], ["sky"],
                ["yup", "yup"], ["ben"], ["pop"], ["you"], ["abe"], ["den", "ned"], ["cod"], ["jul"], ["jar"], ["ray"],
                ["paw"], ["owl"], ["oct"], ["woo"], ["ado"], ["dem"], ["eve"], ["why"], ["sui"], ["ito"], ["ago"],
                ["arc"], ["mys"], ["fat"], ["eon"], ["asp"], ["lea"], ["sow"]]),
              (["eat", "tea", "tan", "ate", "nat", "bat", "ac", "bd", "aac", "bbd", "aacc", "bbdd", "acc", "bdd"],
               [["bdd"], ["bat"], ["nat", "tan"], ["ac"], ["ate", "eat", "tea"], ["bd"], ["aac"], ["bbd"], ["aacc"],
                ["bbdd"], ["acc"]]),
              (["abets", "bead", "remain", "betas", "abed", "baste", "airline", "leading", "beast", "dealing", "beats",
                "airmen", "marine", "single", "bade", "aligned"],
               [["single"], ["abets", "baste", "beast", "beats", "betas"], ["abed", "bade", "bead"],
                ["airmen", "marine", "remain"], ["airline"], ["aligned", "dealing", "leading"]]),
              ]
for test_input, expected_output in test_cases:
    expected_map = {tuple(sorted(one_list[0])): set(one_list) for one_list in expected_output}
    value_map = {tuple(sorted(one_list[0])): set(one_list) for one_list in group_anagrams(str_list=test_input)}
    assert value_map == expected_map
