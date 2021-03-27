"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    :return: whether s and t are anagram
    """
    return Counter(s) == Counter(t)


test_cases = [("anagram", "nagaram", True),
              ("rat", "car", False), ]
for test_s, test_t, expected_output in test_cases:
    assert is_anagram(test_s, test_t) is expected_output
