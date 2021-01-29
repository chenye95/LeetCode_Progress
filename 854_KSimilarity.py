"""
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly
 K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.
"""
from collections import deque


def k_similarity(a: str, b: str) -> int:
    def swap_first_non_matching_character(s_to_morph: str) -> str:
        """
        to morph a into b with fewest steps, each swap needs to match at least one character
        assume that we do it sequentially - i.e. each step matches the first unmatched character
        :param s_to_morph: s_to_morph != b, s_to_morph is an anagram of b
        :return:
        """
        i = 0
        while s_to_morph[i] == b[i]:
            # find the first i such that s_to_morph[i] <> b[i]
            i += 1

        for j in range(i + 1, len(s_to_morph)):
            if s_to_morph[j] == b[i]:
                # swap i and j such that s_to_morph[i] will become B[i]
                yield s_to_morph[:i] + b[i] + s_to_morph[i + 1: j] + s_to_morph[i] + s_to_morph[j + 1:]

    # breadth first search
    queue = deque([a])
    seen_before = {a: 0}
    while queue:
        s = queue.popleft()
        if s == b:
            return seen_before[s]
        for t in swap_first_non_matching_character(s):
            if t not in seen_before:
                seen_before[t] = seen_before[s] + 1
                queue.append(t)


assert k_similarity(a="abac", b="baca") == 2
assert k_similarity(a="ab", b="ba") == 1
assert k_similarity(a="abc", b="bca") == 2
assert k_similarity(a="aabc", b="abca") == 2
