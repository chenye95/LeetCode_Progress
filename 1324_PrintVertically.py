"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
"""
from itertools import zip_longest
from typing import List


def print_vertically(s: str) -> List[str]:
    """
    :return: list represent words printed vertically in the same order in which they appear in s. No Trialing spaces
    """
    words = s.split()
    return [''.join(w).rstrip() for w in zip_longest(*words, fillvalue=' ')]


test_cases = [("HOW ARE YOU", ["HAY", "ORO", "WEU"]),
              ("TO BE OR NOT TO BE", ["TBONTB", "OEROOE", "   T"]),
              ("CONTEST IS COMING", ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]), ]
for test_s, expected_output in test_cases:
    assert print_vertically(s=test_s) == expected_output
