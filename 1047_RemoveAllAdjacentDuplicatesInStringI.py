"""
Given a string s of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and
 removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
"""
from functools import reduce


def remove_duplicates_pointer(s: str):
    """
    :param s: string of lowercase letters
    :return: processed s with all duplicates removed
    """
    processed_until = 0
    list_s = list(s)
    for c in s:
        list_s[processed_until] = c
        if processed_until and list_s[processed_until] == list_s[processed_until - 1]:
            # found duplicates that need to be removed
            processed_until -= 2
        processed_until += 1

    return ''.join(list_s[:processed_until])


def remove_duplicates_stack(s: str):
    """
    :param s: string of lowercase letters
    :return: processed s with all duplicates removed
    """
    return_result = []
    for c in s:
        if return_result and return_result[-1] == c:
            return_result.pop()
        else:
            return_result.append(c)
    return ''.join(return_result)


def remove_duplicates_one_line(s: str):
    """
    Similar to Stack approach

    :param s: string of lowercase letters
    :return: processed s with all duplicates removed
    """
    return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, s)


test_cases = [("abbaca", "ca"), ('aab', 'b'), ('aa', ''),
              ("egibhabdjdjbgeciacchifhhjccdhefecjfcebjbciajbiffgfjeieieiagfihfe",
               "egibhabdjdjbgeciahifjdhefecjfcebjbciajbigfjeieieiagfihfe"), ]
for remove_duplicates in [remove_duplicates_pointer, remove_duplicates_stack, remove_duplicates_one_line, ]:
    for test_s, expected_output in test_cases:
        assert remove_duplicates(test_s) == expected_output, remove_duplicates.__name__
