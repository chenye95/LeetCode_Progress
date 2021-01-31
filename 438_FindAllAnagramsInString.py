"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than
20,100.

The order of output does not matter.
"""
from collections import Counter
from typing import List


def find_anagrams(s: str, p: str) -> List[int]:
    if len(s) < len(p):
        return []

    # Sliding Window
    p_counter = Counter(p)
    s_sliding_window = Counter(s[:len(p)])

    # keep track # of characters in s1 that has not been satisfied
    mismatch_count = sum([1 if p_counter[c] != s_sliding_window.get(c, 0) else 0 for c in p_counter])

    anagram_start = [] if mismatch_count else [0]

    window_count = len(s) - len(p)
    i = 1
    for c1, c2 in zip(s[:window_count], s[len(p):]):
        if c1 != c2:
            # Drop c1 and add c2
            if c1 in p_counter:
                if s_sliding_window[c1] == p_counter[c1]:
                    # Drop c1 will create a new mismatch
                    mismatch_count += 1
                elif s_sliding_window[c1] == p_counter[c1] + 1:
                    # Drop c1 will remove an existing mismatch
                    mismatch_count -= 1
            s_sliding_window[c1] -= 1

            if c2 in p_counter:
                if s_sliding_window[c2] == p_counter[c2]:
                    # Add c2 will create a new mismatch
                    mismatch_count += 1
                elif s_sliding_window[c2] == p_counter[c2] - 1:
                    # Add c2 will remove an existing mismatch
                    mismatch_count -= 1
            s_sliding_window[c2] += 1

        if mismatch_count == 0:
            anagram_start.append(i)
        i += 1

    return anagram_start


assert find_anagrams(s="cbaebabacd", p="abc") == [0, 6]
assert find_anagrams(s="abab", p="ab") == [0, 1, 2]
