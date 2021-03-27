"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same
characters.
"""
from typing import List


def count_palindromic_substrings_dp(s: str) -> int:
    """
    :return: number of palindromic substrings in string s
    """
    if not s:
        return 0
    elif len(s) == 1:
        return 1

    two_chr_before = [True] * len(s)
    one_chr_before = [s[i] == s[i + 1] for i in range(len(s) - 1)]

    total_count = len(s) + sum(one_chr_before)

    for substring_len in range(3, len(s) + 1):
        current_dp = [s[i] == s[i + substring_len - 1] and two_chr_before[i + 1]
                      for i in range(len(s) - substring_len + 1)]
        total_count += sum(current_dp)
        two_chr_before, one_chr_before = one_chr_before, current_dp

    return total_count


def count_palindromic_substrings_dp_split(s: str) -> int:
    """
    :return: number of palindromic substrings in string s
    """
    if not s:
        return 0
    elif len(s) == 1:
        return 1

    def increment_by_two(start_len: int, len_minus_2_dp: List[bool]) -> int:
        sub_total = 0
        for substring_len in range(start_len, len(s) + 1, 2):
            current_dp = [s[i] == s[i + substring_len - 1] and len_minus_2_dp[i + 1]
                          for i in range(len(s) - substring_len + 1)]
            sub_total += sum(current_dp)
            len_minus_2_dp = current_dp

        return sub_total

    single_character = [True] * len(s)
    total_count = len(s) + increment_by_two(3, single_character)

    two_characters = [s[i] == s[i + 1] for i in (range(len(s) - 1))]
    total_count += sum(two_characters) + increment_by_two(4, two_characters)

    return total_count


def count_palindromic_substrings_build(s: str) -> int:
    """
    :return: number of palindromic substrings in string s
    """

    def count_around_center(lo: int, hi: int) -> int:
        sub_total = 0
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
            sub_total += 1
        return sub_total

    if not s:
        return 0

    total_count = 1  # s[-1] as a substring
    for i in range(len(s) - 1):
        total_count += count_around_center(i, i)
        total_count += count_around_center(i, i + 1)

    return total_count


test_cases = [("abc", 3),
              ("aaa", 6),
              ("longtimenosee", 14),
              ("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg", 77)]
for count_palindromic_substrings in [count_palindromic_substrings_build,
                                     count_palindromic_substrings_dp,
                                     count_palindromic_substrings_dp_split]:
    for test_input, expected_output in test_cases:
        assert count_palindromic_substrings(test_input) == expected_output, count_palindromic_substrings.__name__
