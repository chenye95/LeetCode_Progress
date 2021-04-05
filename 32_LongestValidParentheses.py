"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substrings
"""


def longest_valid_parentheses_dp(s: str) -> int:
    """
    Dynamic Programming approach

    :param s: string of parentheses ( and )
    :return: length of the longest substring of parentheses
    """
    max_len = 0
    dp_list = [0] * len(s)  # max length of longest valid parentheses substring among substrings of s[:i]
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                # s[i - 1: i + 1] == "()"
                dp_list[i] = dp_list[i - 2] + 2 if i >= 2 else 2
            elif i - dp_list[i - 1] > 0 and s[i - dp_list[i - 1] - 1] == '(':
                # s[i - 1: i + 1] == "))"
                # s[i - dp_list[i - 1]: i] is a valid parentheses substring of length dp_list[i - 1]
                # if s[i - dp_list[i - 1] - 1] == '(' match up with s[i]
                # we can extend to include previous substrings and add dp_list[i - dp_list[i - 1] - 2]
                dp_list[i] = dp_list[i - 1] + dp_list[i - dp_list[i - 1] - 2] + 2 if i - dp_list[i - 1] >= 2 \
                    else dp_list[i - 1] + 2
            max_len = max(max_len, dp_list[i])
    return max_len


def longest_valid_parentheses_stack(s: str) -> int:
    """
    Stack approach

    :param s: string of parentheses ( and )
    :return: length of the longest substring of parentheses
    """
    max_len = 0
    valid_substring_start_from = [-1]
    for i, s_i in enumerate(s):
        if s_i == '(':
            valid_substring_start_from.append(i)
        else:
            valid_substring_start_from.pop()
            if not valid_substring_start_from:
                valid_substring_start_from = [i]
            else:
                max_len = max(max_len, i - valid_substring_start_from[-1])

    return max_len


def longest_valid_parentheses_two_scan(s: str) -> int:
    """
    Scan from left to right, and from right to left approach

    :param s: string of parentheses ( and )
    :return: length of the longest substring of parentheses
    """
    max_len = 0

    for scan_order, reset_condition in [(s, lambda left_c, right_c: right_c > left_c),
                                        (s[::-1], lambda left_c, right_c: left_c > right_c)]:
        left_count = right_count = 0
        for s_i in scan_order:
            if s_i == '(':
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                max_len = max(max_len, 2 * right_count)
            elif reset_condition(left_count, right_count):
                # invalid substring, reset counters to restart
                left_count = right_count = 0

    return max_len


test_cases = [("())((())", 4), ("(()", 2), (")()())", 4), ("", 0), ]
for longest_valid_parentheses in [longest_valid_parentheses_two_scan,
                                  longest_valid_parentheses_stack,
                                  longest_valid_parentheses_dp, ]:
    for test_s, expected_output in test_cases:
        assert longest_valid_parentheses(test_s) == expected_output
