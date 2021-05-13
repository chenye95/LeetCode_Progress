"""
Given a string s, return the longest palindromic substring in s.
"""
from typing import Tuple


def longest_palindrome_dp(s: str) -> str:
    """
    Dynamic programming approach

    :return: longest palindromic substring in s
    """
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

    for p_len in range(3, len(s) + 1):
        for i in range(0, len(s) - p_len + 1):
            j = i + p_len - 1
            memory[i][j] = memory[i + 1][j - 1] and (s[i] == s[j])
            if memory[i][j]:
                return_str = s[i: j + 1]

    return return_str


def longest_palindromic_construction(s: str) -> str:
    """
    Construction from center approach

    :return: longest palindromic substring in s
    """

    def expand_around_center(left_s: int, right_s: int) -> Tuple[int, int, int]:
        """
        :return: length the longest palindromic substring expanded around s[left_s: right_s + 1], and start and end of
            the substring
        """
        while 0 <= left_s and right_s < len(s) and s[left_s] == s[right_s]:
            left_s -= 1
            right_s += 1
        # (right_s - 1) - (left_s + 1) + 1
        return right_s - left_s - 1, left_s + 1, right_s - 1

    if not s or len(s) <= 1:
        return s

    return_str_start, return_str_end, return_str_len = 0, 0, 1
    for i in range(len(s)):
        option_odd_len = expand_around_center(i, i)  # mirror around position i
        option_even_len = expand_around_center(i, i + 1)  # mirror around position i, i + 1
        i_len, new_left, new_right = max(option_odd_len, option_even_len)
        if i_len > return_str_len:
            return_str_len, return_str_start, return_str_end = i_len, new_left, new_right

    return s[return_str_start: return_str_end + 1]


test_cases = [("ccc", {"ccc"}),
              ("babad", {"bab", "aba"}),
              ("cbbd", {"bb"}),
              ("a", {"a"}),
              ("ac", {"a", "c"}),
              ("aacabdkacaa", {"aca", }),
              ("xaabacxcabaaxcabaax", {"xaabacxcabaax", })]
for longest_palindromic in [longest_palindromic_construction, longest_palindrome_dp, ]:
    for test_input, expected_output in test_cases:
        assert longest_palindromic(s=test_input) in expected_output, longest_palindromic.__name__
