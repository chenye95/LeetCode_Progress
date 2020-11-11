"""
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is
not). A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    DP implementation Top Down Approach
    """
    short_text, long_text = (text1, text2) if len(text1) <= len(text2) else (text2, text1)
    prev_iteration = [0] * (len(short_text) + 1)
    for bi in long_text:
        curr_iteration = [0] * (len(short_text) + 1)
        for i, ai in enumerate(short_text):
            if ai == bi:
                curr_iteration[i + 1] = prev_iteration[i] + 1
            else:
                curr_iteration[i + 1] = max(curr_iteration[i], prev_iteration[i + 1])
        prev_iteration = curr_iteration
    return prev_iteration[-1]


assert 3 == longest_common_subsequence(text1="abcde", text2="ace")
assert 3 == longest_common_subsequence(text1="abc", text2="abc")
assert 0 == longest_common_subsequence(text1="abc", text2="def")
