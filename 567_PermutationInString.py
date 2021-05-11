"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.
"""
from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    """
    :param s1: short string
    :param s2: long string
    :return: whether some permutation of s1 is a substring of s2
    """
    # Sliding Window
    s1_counter = Counter(s1)
    s2_sliding_window = Counter(s2[:len(s1)])

    # keep track # of characters in s1 that has not been satisfied
    no_chr_unsatisfied = sum([1 if s1_counter[c] != s2_sliding_window.get(c, 0) else 0 for c in s1_counter])
    if no_chr_unsatisfied == 0:
        return True

    window_count = len(s2) - len(s1)
    for drop_c, add_c in zip(s2[:window_count], s2[len(s1):]):
        if drop_c != add_c:
            # Drop drop_c and add add_c
            if drop_c in s1_counter:
                if s2_sliding_window[drop_c] == s1_counter[drop_c]:
                    # Drop drop_c will create a new mismatch
                    no_chr_unsatisfied += 1
                elif s2_sliding_window[drop_c] == s1_counter[drop_c] + 1:
                    # Drop drop_c will remove an existing mismatch
                    no_chr_unsatisfied -= 1
            s2_sliding_window[drop_c] -= 1

            if add_c in s1_counter:
                if s2_sliding_window[add_c] == s1_counter[add_c]:
                    # Add add_c will create a new mismatch
                    no_chr_unsatisfied += 1
                elif s2_sliding_window[add_c] == s1_counter[add_c] - 1:
                    # Add add_c will remove an existing mismatch
                    no_chr_unsatisfied -= 1
            s2_sliding_window[add_c] += 1

            if no_chr_unsatisfied == 0:
                return True

    return False


test_cases = [("adc", "dcda", True), ("ab", "eidbaooo", True), ("ab", "eidboaoo", False),
              ("osmzg", "diyhaywtgpzosgmuxvidndouo", True),
              ("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine", True),
              ("hello", "ooolleoooleh", False),
              ("dinitrophenylhydrazine", "acetylphenylhydrazine", False), ]
for test_s1, test_s2, expected_output in test_cases:
    assert check_inclusion(s1=test_s1, s2=test_s2) is expected_output
