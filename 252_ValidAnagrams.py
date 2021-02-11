"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
