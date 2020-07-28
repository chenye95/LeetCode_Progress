"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all
strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4
times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""
from collections import Counter
from typing import List


def commonChars(A: List[str]) -> List[str]:
    if not A:
        return []
    tmp = Counter(A[0])
    for s in A[1:]:
        tmp &= Counter(s)
    return list(tmp.elements())


assert commonChars(["bella", "label", "roller"]) == ['e', 'l', 'l']