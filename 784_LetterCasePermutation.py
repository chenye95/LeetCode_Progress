"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
"""
from typing import List


def letter_case_permutations_backtrack(s: str) -> List[str]:
    def permutation_helper(current_str: str, start_from: int) -> None:
        next_c = start_from
        while next_c < len(current_str) and not current_str[next_c].isalpha():
            next_c += 1

        if next_c == len(current_str):
            nonlocal return_list
            return_list.append(current_str)
            return

        permutation_helper(current_str, next_c + 1)
        if current_str[next_c].isupper():
            current_str = current_str[:next_c] + current_str[next_c].lower() + current_str[next_c + 1:]
        else:
            current_str = current_str[:next_c] + current_str[next_c].upper() + current_str[next_c + 1:]
        permutation_helper(current_str, next_c + 1)

    return_list = []
    if s:
        permutation_helper(s, 0)
    return return_list


def letter_case_permutations_list(s: str) -> List[str]:
    if not s:
        return []

    current_level = ['']
    i_start = 0
    while i_start < len(s):
        i_end = i_start
        while i_end < len(s) and not s[i_end].isalpha():
            i_end += 1

        if i_end < len(s):
            next_level = [s_current + s[i_start: i_end] + s[i_end].lower() for s_current in current_level]
            next_level += [s_current + s[i_start: i_end] + s[i_end].upper() for s_current in current_level]
        else:
            next_level = [s_current + s[i_start: i_end] for s_current in current_level]

        i_start = i_end + 1
        current_level = next_level

    return current_level


test_cases = [("a", {"a", "A"}),
              ("a1b2", {"a1b2", "a1B2", "A1b2", "A1B2"}),
              ("3z4", {"3z4", "3Z4"}),
              ("12345", {"12345"}),
              ("0", {"0"}),
              ("ab", {"ab", "aB", "Ab", "AB"}),
              ("", set()), ]
for letter_case_permutation in [letter_case_permutations_list, letter_case_permutations_backtrack]:
    for test_input, expected_output in test_cases:
        assert set(letter_case_permutation(test_input)) == expected_output, letter_case_permutation.__name__
