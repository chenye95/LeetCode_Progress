"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


def longest_common_prefix(str_list: List[str]) -> str:
    if not str_list:
        return ""
    if len(str_list) == 1:
        return str_list[0]

    longest_prefix = ""
    s_0 = str_list[0]
    for i in range(min(len(s_i) for s_i in str_list)):
        if all(s_i[i] == s_0[i] for s_i in str_list[1:]):
            longest_prefix += s_0[i]
        else:
            break

    return longest_prefix


assert longest_common_prefix(["", "b"]) == ""
assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix(["you"]) == "you"
