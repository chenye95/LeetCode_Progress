"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
 characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of
 "ABCDE" while "AEC" is not).
"""
def numDistinct(s: str, t: str) -> int:
    if not s or len(s) < len(t):
        return 0

    # Matching if t[t_i] is matched up with s[s_i]
    dp = [[0] * (len(s)) for _ in range(len(t))]

    for t_i in range(len(t)):
        for s_i in range(len(s)):
            if s[s_i] == t[t_i]:
                dp[t_i][s_i] = 1 if t_i == 0 else sum(dp[t_i - 1][:s_i])
    return sum(dp[-1])


assert numDistinct(s="BABGBAG", t="BAG") == 5
assert numDistinct(s="rabbbit", t="rabbit") == 3
