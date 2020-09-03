"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the
 substring together. You may assume the given string consists of lowercase English letters only and its length will not
 exceed 10000.
"""


def repeated_substring_pattern(s: str) -> bool:
    """
    Note that
        - First char of input string is first char of repeated substring
        - Last char of input string is last char of repeated substring
    :return: if s exhibits repeated pattern
    """
    if not s:
        return False
    return s in (s + s)[1: -1]


assert repeated_substring_pattern("abc") is False
assert repeated_substring_pattern("abab") is True
assert repeated_substring_pattern("abcabcabcabc") is True
