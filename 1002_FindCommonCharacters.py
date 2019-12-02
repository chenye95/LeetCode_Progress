from collections import Counter
from typing import List

def commonChars(A: List[str]) -> List[str]:
    if not A:
        return []
    tmp = Counter(A[0])
    for s in A[1:]:
        tmp &= Counter(s)
    return list(tmp.elements())


commonChars(["bella","label","roller"])
