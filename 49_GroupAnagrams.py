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


for test_input, expected_output in [(["eat", "tea", "tan", "ate", "nat", "bat"],
                                     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
                                    ([""], [[""]]),
                                    (["a"], [["a"]]), ]:
    value_out = group_anagrams(str_list=test_input)
    expected_map = {}
    for one_list in expected_output:
        expected_map[tuple(sorted(one_list[0]))] = set(one_list)
    value_map = {}
    for one_list in value_out:
        value_map[tuple(sorted(one_list[0]))] = set(one_list)
    assert value_map == expected_map
