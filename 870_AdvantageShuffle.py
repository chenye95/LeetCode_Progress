"""
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which
A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.
"""
from collections import deque
from itertools import permutations
from typing import List


def advantage_sort_b(a: List[int], b: List[int]) -> List[int]:
    """
    Greedy algorithm： pair the largest of remaining a with the largest of b_i among remaining of b
    Pair by b
    """
    a = sorted(a)
    # use list as b can contain duplicates
    pair_map = {b_i: [] for b_i in b}
    for b_i in sorted(b)[::-1]:
        # largest of remainder a[-1] since a is sorted
        if b_i < a[-1]:
            pair_map[b_i].append(a.pop())
    # for b_i that is larger than any values in a, randomly pair with any values will work
    return [(pair_map[b_i] or a).pop() for b_i in b]


def advantage_sort_a(a: List[int], b: List[int]) -> List[int]:
    """
    Greedy algorithm： pair the smallest of remaining a with the smallest of remaining b
    Pair by a
    """
    return_list = [-1] * len(a)
    # need to support pop from both sides
    b_list = deque(sorted([(b_i, i) for i, b_i in enumerate(b)]))

    for a_i in sorted(a):
        # b_list is sorted, smallest of remainder is b_list[0][0]
        if a_i > b_list[0][0]:
            _, idx = b_list.popleft()
        else:
            # pair with the biggest of remaining b
            _, idx = b_list.pop()

        return_list[idx] = a_i
    return return_list


def is_max_advantage_sort(candidate_a: List[int], b: List[int]) -> bool:
    assert len(candidate_a) == len(b)
    candidate_advantage = sum(a_i > b_i for a_i, b_i in zip(candidate_a, b))
    return candidate_advantage == max(sum(a_i > b_i for a_i, b_i in zip(per_a, b))
                                      for per_a in permutations(candidate_a))


test_cases = [([2, 7, 11, 15], [1, 10, 4, 11]),
              ([12, 24, 8, 32], [13, 25, 32, 11]), ]
for advantage_sort in [advantage_sort_a, advantage_sort_b]:
    for test_a, test_b in test_cases:
        assert is_max_advantage_sort(advantage_sort(test_a, test_b), test_b)
