"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write
a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
 citations each, and the other N − h papers have no more than h citations each."
"""
from bisect import bisect_left
from typing import List


def hIndex(citations: List[int]) -> int:
    if not citations:
        return 0
    # elif len(citations) == 1:
    #    return 1
    h_index = 0
    n = len(citations)
    start, end = 0, len(citations) - 1
    while start <= end:
        mid = (start + end) // 2
        if citations[mid] >= (n - mid):
            h_index = max(h_index, n - mid)
            end = mid - 1
        else:
            start = mid + 1
    return h_index


def hIndexBisect(citations: List[int]) -> int:
    n = len(citations)
    class Range():
        def __getitem__(self, key):
            return n - key <= citations[key]
    index = bisect_left(Range(), True, 0, n)
    return n - index if index < n else 0


from timeit import Timer
from functools import partial

assert(hIndex([1,1,2,3,4,5,7])) == 3
assert(hIndex([1, 2])) == 1
assert(hIndex([0,1,3,5,6])) == 3
assert(hIndex([0])) == 0
assert(hIndex([100])) == 1

test_citations = [1,1,2,3,4,5,7]
n_cyclces = 10000
t_disect = Timer(partial(hIndexBisect, test_citations))
print("Bisect", t_disect.timeit(n_cyclces)/n_cyclces)

t_my = Timer(partial(hIndex, test_citations))
print("My", t_my.timeit(n_cyclces)/n_cyclces)
