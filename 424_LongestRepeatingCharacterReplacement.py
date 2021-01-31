"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
In one operation, you can choose any character of the string and change it to any other uppercase English character.
Find the length of the longest sub-string containing all repeating letters you can get after performing the above
operations.
Note: Both the string's length and k will not exceed 104.
"""
from collections import Counter


def character_replacement(s: str, k: int) -> int:
    if not s:
        return 0

    if k > 0:
        window_count = Counter(s[:k])
        most_chr_in_window = max(window_count.values())
        window_start = 0
    else:
        window_count = Counter()
        most_chr_in_window = window_start = 0

    for window_end in range(k, len(s)):
        window_count[s[window_end]] += 1
        if window_count[s[window_end]] > most_chr_in_window:
            most_chr_in_window = window_count[s[window_end]]
        if window_end - window_start + 1 - most_chr_in_window > k:
            window_count[s[window_start]] -= 1
            window_start += 1
            # since we are removing one character at a time, length of the window can only expand
            # max_len is carried over to following runs

    return len(s) - window_start


assert character_replacement(s="ABAB", k=2) == 4
assert character_replacement(s="AABABBA", k=1) == 4
assert character_replacement(s="AABABBACC", k=1) == 4
assert character_replacement(s="AAAA", k=0) == 4
assert character_replacement(s="", k=10) == 0
