"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
 characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of
 "ABCDE" while "AEC" is not).
"""


def num_distinct(s: str, t: str) -> int:
    """
    :return: number of distinct subsequences of s that equals t
    """
    if not s or len(s) < len(t):
        return 0

    # Sub problem with t[:t_i] and s[:s_i] if t[t_i] is matched up with s[s_i]
    dp = [[0] * len(s) for _ in range(len(t))]

    for t_i in range(len(t)):
        for s_i in range(len(s)):
            if s[s_i] == t[t_i]:
                dp[t_i][s_i] = 1 if t_i == 0 else sum(dp[t_i - 1][:s_i])
    return sum(dp[-1])


test_cases = [("BABGBAG", "BAG", 5),
              ("rabbbit", "rabbit", 3),
              ("anacondastreetracecar", "contra", 6),
              ("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedaba" +
               "bedeacdeaaaeeaecbe", "bddabdcae", 10582116), ]
for test_s, test_t, expected_output in test_cases:
    assert num_distinct(s=test_s, t=test_t) == expected_output
