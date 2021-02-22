"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
characters of the given string. If there are more than one possible results, return the longest word with the smallest
lexicographical order. If there is no possible result, return the empty string.
"""
from typing import List


def find_longest_word(s: str, d: List[str]) -> str:
    d.sort(key=lambda x: (-len(x), x))
    for dict_str in d:
        last_chr_position = 0

        for c in dict_str:
            last_chr_position = s.find(c, last_chr_position) + 1
            if last_chr_position == 0:
                break

        if last_chr_position > 0:
            return dict_str

    return ""


test_cases = [("abpcplea", ["ale", "apple", "monkey", "plea"], "apple"),
              ("abpcplea", ["a", "b", "c"], "a")]
for test_s, test_dict, expected_output in test_cases:
    assert find_longest_word(test_s, test_dict) == expected_output
