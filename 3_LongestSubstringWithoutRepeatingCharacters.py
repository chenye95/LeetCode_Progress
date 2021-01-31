"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def length_of_longest_substring(s: str) -> int:
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


assert length_of_longest_substring(s="abcabcbb") == 3
assert length_of_longest_substring(s="bbbbb") == 1
assert length_of_longest_substring(s="pwwkew") == 3
assert length_of_longest_substring(s="") == 0
