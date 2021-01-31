"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.
"""
from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    # Sliding Window
    s1_counter = Counter(s1)
    s2_sliding_window = Counter(s2[:len(s1)])

    # keep track # of characters in s1 that has not been satisfied
    mismatch_count = sum([1 if s1_counter[c] != s2_sliding_window.get(c, 0) else 0 for c in s1_counter])
    if mismatch_count == 0:
        return True

    window_count = len(s2) - len(s1)
    for c1, c2 in zip(s2[:window_count], s2[len(s1):]):
        if c1 != c2:
            # Drop c1 and add c2
            if c1 in s1_counter:
                if s2_sliding_window[c1] == s1_counter[c1]:
                    # Drop c1 will create a new mismatch
                    mismatch_count += 1
                elif s2_sliding_window[c1] == s1_counter[c1] + 1:
                    # Drop c1 will remove an existing mismatch
                    mismatch_count -= 1
            s2_sliding_window[c1] -= 1

            if c2 in s1_counter:
                if s2_sliding_window[c2] == s1_counter[c2]:
                    # Add c2 will create a new mismatch
                    mismatch_count += 1
                elif s2_sliding_window[c2] == s1_counter[c2] - 1:
                    # Add c2 will remove an existing mismatch
                    mismatch_count -= 1
            s2_sliding_window[c2] += 1

            if mismatch_count == 0:
                return True

    return False


assert check_inclusion(s1="adc", s2="dcda")
assert check_inclusion(s1="ab", s2="eidbaooo")
assert not check_inclusion(s1="ab", s2="eidboaoo")
