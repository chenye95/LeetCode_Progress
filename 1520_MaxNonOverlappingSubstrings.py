"""
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the
following conditions:
- The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
- A substring that contains a certain character c must also contain all occurrences of c.

Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same
number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of
minimum total length.
"""
from typing import List, Dict


def max_num_of_substrings(s: str) -> List[str]:
    """
    Greedy Algorithm
    :param s: string to find non-overlapping substrings among
    :return: maximum number of substrings that meet conditions
    """

    def check_substring(substring_start: int, character_lookup: Dict[chr, List[int]]) -> int:
        """
        :param substring_start: substring starting from s[substring_start:]
        :param character_lookup: passed in lookup dictionary record first and last occurrence for each character
        :return: substring_end for the shortest substring s[substring_start:substring_end] that satisfies condition
                -1 no such substring exists
        """
        substring_end = character_lookup[s[substring_start]][1]
        substring_probe = substring_start
        while substring_probe <= substring_end:
            if character_lookup[s[substring_probe]][0] < substring_start:
                return -1
            substring_end = max(substring_end, character_lookup[s[substring_probe]][1])
            substring_probe += 1
        return substring_end

    # Calculate the first and last appearance for each character
    first_last_occurrence = dict()
    for i, c in enumerate(s):
        if c not in first_last_occurrence:
            first_last_occurrence[c] = [i, i]
        else:
            first_last_occurrence[c][1] = i

    return_list = []
    starting_position = sorted(list(first_last_occurrence_c[0]
                                    for first_last_occurrence_c in first_last_occurrence.values()))

    last_substring_end = -1
    # Greedy approach, take the shorter substring among overlapping substrings
    for i in starting_position:
        current_substring_end = check_substring(i, first_last_occurrence)
        if current_substring_end != -1:
            if i > last_substring_end:
                # Next substring not overlapping with previous ones
                return_list.append('')
            # Greedy algorithm replace with shorter one
            return_list[-1] = s[i:current_substring_end + 1]
            last_substring_end = current_substring_end

    return return_list


assert {"e", "f", "ccc"} == set(max_num_of_substrings(s="adefaddaccc"))
assert {"d", "bb", "cc"} == set(max_num_of_substrings(s="abbaccd"))
