"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def length_of_longest_substring(s: str) -> int:
    """
    :return: the length of the longest substring of s without repeating characters
    """
    substring_start = max_len = 0
    last_seen = {}

    for i, c in enumerate(s):
        if c in last_seen and substring_start <= last_seen[c]:
            # seen character c before, reset the start of substring
            # i - substring_start + 1 with new substring_start guaranteed to be less than max_len
            substring_start = last_seen[c] + 1
        elif i - substring_start + 1 > max_len:
            max_len = i - substring_start + 1

        last_seen[c] = i

    return max_len


test_cases = [("abcabcbb", 3),
              ("bbbbb", 1),
              ("pwwkew", 3),
              ("", 0), ]
for test_s, expected_output in test_cases:
    assert length_of_longest_substring(s=test_s) == expected_output
