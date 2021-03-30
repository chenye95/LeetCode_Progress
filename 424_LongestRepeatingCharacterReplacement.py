"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
In one operation, you can choose any character of the string and change it to any other uppercase English character.
Find the length of the longest sub-string containing all repeating letters you can get after performing the above
operations.
Note: Both the string's length and k will not exceed 104.
"""
from collections import Counter


def character_replacement(s: str, k: int) -> int:
    """
    :param s: string of uppercase English letters, with length not exceeding 104
    :param k: at most k operations, in which we replace any character with any other uppercase English letter. k will
    not exceed 104
    :return: length of longest substring containing all repeating letters after performing at most k operations
    """
    if not s:
        return 0

    if k > 0:
        window_count = Counter(s[:k])
        most_chr_in_window = max(window_count.values())
    else:
        window_count = Counter()
        most_chr_in_window = 0

    window_start = 0
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


test_cases = [("ABAB", 2, 4),
              ("AABABBA", 1, 4),
              ("AABABBACC", 1, 4),
              ("AAAA", 0, 4),
              ("", 10, 0), ]
for test_s, test_k, expected_count in test_cases:
    assert character_replacement(s=test_s, k=test_k) == expected_count
