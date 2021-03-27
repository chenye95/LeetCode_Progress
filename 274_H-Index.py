"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the
researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
citations each, and the other N − h papers have no more than h citations each."
"""
from typing import List


def h_index(citations: List[int]) -> int:
    """
    :param citations: array of citations
    :return: h-index of the researcher
    """
    h_index = 0
    n = len(citations)
    above_h_count = [0] * (n + 1)
    for c in citations:
        if c >= h_index:
            above_h_count[min(c, n)] += 1
            if above_h_count[h_index] > 0:
                above_h_count[h_index] -= 1
            else:
                h_index += 1
    return h_index


test_cases = [([3, 0, 6, 1, 5], 3),
              ([1, 3, 1], 1),
              ([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3], 6), ]
for citation_list, expected_h_index in test_cases:
    assert h_index(citations=citation_list) == expected_h_index
