"""
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly
 K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.
"""
from collections import deque


def k_similarity(word_a: str, word_b: str) -> int:
    def swap_first_non_matching_character(s_to_morph: str) -> str:
        """
        to morph s_to_morph into word_b with fewest steps, each swap needs to match at least one character
        assume that we do it sequentially - i.e. each step matches the first unmatched character
        :param s_to_morph: s_to_morph != word_b, s_to_morph is an anagram of word_b
        :return:
        """
        i = 0
        while s_to_morph[i] == word_b[i]:
            # find the first i such that s_to_morph[i] <> word_b[i]
            i += 1

        for j in range(i + 1, len(s_to_morph)):
            # target word is word_b
            if s_to_morph[j] == word_b[i]:
                # swap i and j such that s_to_morph[i] will become B[i]
                yield s_to_morph[:i] + word_b[i] + s_to_morph[i + 1: j] + s_to_morph[i] + s_to_morph[j + 1:]

    # breadth first search
    queue = deque([word_a])
    steps_to_become = {word_a: 0}
    while queue:
        word_s = queue.popleft()
        if word_s == word_b:
            return steps_to_become[word_s]
        for word_t in swap_first_non_matching_character(word_s):
            if word_t not in steps_to_become:
                steps_to_become[word_t] = steps_to_become[word_s] + 1
                queue.append(word_t)


assert k_similarity(word_a="abac", word_b="baca") == 2
assert k_similarity(word_a="ab", word_b="ba") == 1
assert k_similarity(word_a="abc", word_b="bca") == 2
assert k_similarity(word_a="aabc", word_b="abca") == 2
