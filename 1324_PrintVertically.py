"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
"""
from itertools import zip_longest
from typing import List


def printVertically(s: str) -> List[str]:
    words = s.split()
    return [''.join(w).rstrip() for w in zip_longest(*words, fillvalue=' ')]


assert ["HAY", "ORO", "WEU"] == printVertically(s="HOW ARE YOU")
assert ["TBONTB", "OEROOE", "   T"] == printVertically(s="TO BE OR NOT TO BE")
assert ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"] == printVertically(s="CONTEST IS COMING")
