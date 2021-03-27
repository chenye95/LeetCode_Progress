"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


def longest_common_prefix(str_list: List[str]) -> str:
    """
    :param str_list: list of random strings
    :return: longest common prefix of all strings in str_list
    """
    if not str_list:
        return ""
    if len(str_list) == 1:
        return str_list[0]

    longest_prefix_list = []
    s_0 = str_list[0]
    for i in range(min(len(s_i) for s_i in str_list)):
        if all(s_i[i] == s_0[i] for s_i in str_list[1:]):
            longest_prefix_list.append(s_0[i])
        else:
            break

    return ''.join(longest_prefix_list)


test_cases = [(["", "b"], ""),
              (["flower", "flow", "flight"], "fl"),
              (["dog", "racecar", "car"], ""),
              (["you"], "you"), ]
for test_str_list, expected_output in test_cases:
    assert longest_common_prefix(str_list=test_str_list) == expected_output
