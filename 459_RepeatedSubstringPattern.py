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

    :param s: a non empty string
    :return: if s exhibits repeated pattern
    """
    assert s
    return s in (s + s)[1: -1]


test_cases = [("abc", False), ("abab", True), ("abcabcabcabc", True), ]
for test_s, expected_output in test_cases:
    assert repeated_substring_pattern(s=test_s) is expected_output
