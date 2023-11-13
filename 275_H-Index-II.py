"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write
a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
 citations each, and the other N − h papers have no more than h citations each."
"""
from bisect import bisect_left
from typing import List


def h_index_my_bisect(citations: List[int]) -> int:
    """
    :param citations: array of non-negative integers in ascending order
    :return: h-index of the researcher
    """
    if not citations:
        return 0
    # elif len(citations) == 1:
    #    return 1
    result_h_index = 0
    n = len(citations)
    start, end = 0, len(citations) - 1
    while start <= end:
        mid = (start + end) // 2
        if citations[mid] >= (n - mid):
            result_h_index = max(result_h_index, n - mid)
            end = mid - 1
        else:
            start = mid + 1
    return result_h_index


def h_index_bisect(citations: List[int]) -> int:
    """
    :param citations: array of non-negative integers in ascending order
    :return: h-index of the researcher
    """
    n = len(citations)

    class Range():
        def __getitem__(self, key):
            return n - key <= citations[key]

    index = bisect_left(Range(), True, 0, n)
    return n - index if index < n else 0


test_cases = [([1, 1, 2, 3, 4, 5, 7], 3),
              ([1, 2], 1),
              ([0, 1, 3, 5, 6], 3),
              ([0], 0),
              ([100], 1), ]
for h_index in [h_index_my_bisect, h_index_bisect]:
    for citation_list, expected_h_index in test_cases:
        assert h_index(citations=citation_list) == expected_h_index, h_index.__name__

"""
test_citations = [1, 1, 2, 3, 4, 5, 7]
n_cycles = 10_000

t_bisect = Timer(partial(h_index_bisect, test_citations))
print("Bisect", t_bisect.timeit(n_cycles) / n_cycles)

t_my = Timer(partial(h_index_my_bisect, test_citations))
print("My", t_my.timeit(n_cycles) / n_cycles)

t_bisect = Timer(partial(h_index_bisect, test_citations))
print("Bisect", t_bisect.timeit(n_cycles) / n_cycles)
"""
