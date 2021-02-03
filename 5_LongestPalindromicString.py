"""
Given a string s, return the longest palindromic substring in s.
"""


def longest_palindrome_dp(s: str) -> str:
    if not s or len(s) <= 1:
        return s
    memory = [[False] * len(s) for _ in range(len(s))]

    return_str = ""
    # Base Case
    for i in range(len(s) - 1):
        memory[i][i] = True
        if s[i] == s[i + 1]:
            memory[i][i + 1] = True
            if not return_str:
                return_str = s[i: i + 2]
    memory[-1][-1] = True

    if not return_str:
        return_str = s[0]

    for p_len in range(3, len(s)):
        for i in range(0, len(s) - p_len + 1):
            j = i + p_len - 1
            memory[i][j] = memory[i + 1][j - 1] and (s[i] == s[j])
            if memory[i][j]:
                return_str = s[i: j + 1]

    return return_str


def longest_palindromic_construction(s: str) -> str:
    def expand_around_center(l: int, r: int) -> int:
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1  # (r - 1) - (l + 1) + 1

    if not s or len(s) <= 1:
        return s

    return_str_start, return_str_end, return_str_len = 0, 0, 1
    for i in range(len(s)):
        len_1 = expand_around_center(i, i)  # mirror around position i
        len_2 = expand_around_center(i, i + 1)  # mirror around position i, i + 1
        i_len = max(len_1, len_2)
        if i_len > return_str_len:
            return_str_len = i_len
            return_str_start = i - (i_len - 1) // 2
            return_str_end = i + i_len // 2

    return s[return_str_start: return_str_end + 1]


test_cases = [("babad", ["bab", "aba"]),
              ("cbbd", ["bb"]),
              ("a", ["a"]),
              ("ac", ["a", "c"])]
for longest_palindromic in [longest_palindromic_construction, longest_palindrome_dp]:
    for test_input, expected_output in test_cases:
        assert longest_palindromic(test_input) in expected_output
