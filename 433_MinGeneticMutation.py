"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as
 one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene
 string.

Given the two gene strings start and end and the gene bank, return the minimum number of mutations needed to mutate
 from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
"""
from collections import deque
from typing import List

UNABLE_TO_FIND = -1
GENE_STR = "ACGT"


def min_mutation(start: str, end: str, bank: List[str]) -> int:
    if start == end:
        return 0
    elif len(start) != len(end) or not bank:
        return UNABLE_TO_FIND

    str_len = len(start)

    queue = deque([(start, 0)])
    seen = {start}

    while queue:
        current_str, current_steps = queue.popleft()

        for c in GENE_STR:
            for i in range(str_len):
                next_str = current_str[:i] + c + current_str[i + 1:]
                if next_str in bank:
                    if next_str == end:
                        return current_steps + 1
                    if next_str not in seen:
                        queue.append((next_str, current_steps + 1))
                        seen.add(next_str)

    return UNABLE_TO_FIND


test_cases = [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AAAAAAAA", "AAGTAAAA", ["CAAAAAAA", "CCAAAAAA", "CCATAAAA", "CCGTAAAA", "CAGTAAAA", "AAGTAAAA"], 6),
    ("AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"], -1),
    ("AACCGGTT", "AACCGGTA", [], -1),
    ("AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"], -1),
    ("AAAAAAAA", "AAGTAAAA", ["CAAAAAAA", "CCAAAAAA", "CCATAAAA", "CCGTAAAA", "CAGTAAAA", "AAGTAAAA"], 6),
]
for test_start, test_end, test_bank, expected_steps in test_cases:
    assert min_mutation(test_start, test_end, test_bank) == expected_steps
