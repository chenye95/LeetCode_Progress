"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
- '?' Matches any single character.
= '*' Matches any sequence of characters (including the empty sequence).
"""
def isMatch(s: str, p: str) -> bool:
    dp_memory = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp_memory[0][0] = True
    # Leading * can match to no characters
    for p_i in range(len(p)):
        if p[p_i] == '*':
            dp_memory[p_i + 1][0] = True
        else:
            break
    for p_i in range(len(p)):
        for s_i in range(len(s)):
            if p[p_i] == s[s_i] or p[p_i] == '?':
                dp_memory[p_i + 1][s_i + 1] = dp_memory[p_i][s_i]
            elif p[p_i] == '*':
                # * stands for zero -> dp_memory[p_i][s_i + 1]
                # * stands for one -> dp_memory[p_i][s_i]
                # * stands for more -> dp_memory[p_i + 1][s_i]
                dp_memory[p_i + 1][s_i + 1] = dp_memory[p_i][s_i + 1] or dp_memory[p_i + 1][s_i] or dp_memory[p_i][s_i]
    return dp_memory[-1][-1]


assert isMatch(s="acdcb", p="a*c?")
assert isMatch(s="adceb", p="*a*b")
assert isMatch(s="adceb", p="**")
