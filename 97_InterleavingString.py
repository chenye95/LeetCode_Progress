"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
"""
from functools import cache


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    """
    :param s1: 0 <= len(s1) <= 100, consists of lowercase english letter
    :param s2: 0 <= len(s2) <= 100, consists of lowercase english letter
    :param s3: 0 <= len(s3) <= 200, consists of lowercase english letter
    :return: whether s3 is interleaving of s1 and s2
    """

    @cache
    def solve_substring(i: int, j: int) -> bool:
        """
        :return: whether s3[i + j:] is interleaving of s1[i:] and s2[j:]
        """
        if i == len(s1):
            return s2[j:] == s3[i + j:]
        if j == len(s2):
            return s1[i:] == s3[i + j:]
        return (s1[i] == s3[i + j] and solve_substring(i + 1, j)) or (s2[j] == s3[i + j] and solve_substring(i, j + 1))

    if len(s3) != len(s1) + len(s2):
        return False
    return solve_substring(0, 0)


test_cases = [("", "", "", True),
              ("", "", "a", False),
              ("aabcc", "dbbca", "aadbbbaccc", False),
              ("aabcc", "dbbca", "aadbbcbcac", True),
              ("cabbcaaacacbac", "acabaabacabcca", "cacabaabacaabccbabcaaacacbac", True),
              ("abaaacbacaab", "bcccababccc", "bcccabaaaaabccaccbacabb", False), ]
for test_s1, test_s2, test_s3, expected_value in test_cases:
    assert is_interleave(test_s1, test_s2, test_s3) is expected_value
