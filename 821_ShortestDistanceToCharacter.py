"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
and answer[i] is the shortest distance from s[i] to the character c in s.
"""
from typing import List


def shortest_to_chr(s: str, c: chr) -> List[int]:
    distance_list = [0] * len(s)

    left_counter = len(s)
    for i, c_i in enumerate(s):
        if c_i == c:
            left_counter = 0
        else:
            left_counter += 1
        distance_list[i] = left_counter

    right_counter = right_i = len(s)
    for i in range(len(s)):
        right_i -= 1
        if s[right_i] == c:
            right_counter = 0
        else:
            right_counter += 1
        if right_counter < distance_list[right_i]:
            distance_list[right_i] = right_counter

    return distance_list


assert shortest_to_chr("loveleetcode", 'e') == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
