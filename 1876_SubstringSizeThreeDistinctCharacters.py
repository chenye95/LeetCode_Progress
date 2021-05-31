"""
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
"""


def count_good_substrings(s: str, substring_len: int = 3) -> int:
    """
    :param s: consists of lower case english letters only and 1 <= len(s) <= 100
    :param substring_len: length of the substring, requires substring has distinct characters
    :return: number of good substrings of s that is of length 3
    """
    substring_len = 3

    if len(s) < substring_len:
        return 0

    seen_so_far = {}
    distinct_chr = 0
    for add_c in s[:substring_len]:
        if seen_so_far.get(add_c, 0) == 0:
            distinct_chr += 1
        seen_so_far[add_c] = seen_so_far.get(add_c, 0) + 1

    substring_count = 1 if distinct_chr == substring_len else 0

    for remove_c, add_c in zip(s[:-substring_len], s[substring_len:]):
        if remove_c != add_c:
            if seen_so_far[remove_c] == 1:
                distinct_chr -= 1
            seen_so_far[remove_c] -= 1
            if seen_so_far.get(add_c, 0) == 0:
                distinct_chr += 1
            seen_so_far[add_c] = seen_so_far.get(add_c, 0) + 1

        if distinct_chr == substring_len:
            substring_count += 1

    return substring_count


test_cases = [("aab", 0),
              ("abc", 1),
              ("ab", 0),
              ("aabc", 1),
              ("aababcabc", 4),
              ("xyzzaz", 1),
              ("ogwwmbdsrelstcbgpbmxovfmnenrxdvjqjtpplfdsrxrxpifagd", 41), ]
for test_s, expected_value in test_cases:
    assert count_good_substrings(test_s) == expected_value
