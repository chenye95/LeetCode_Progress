"""
Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2],
... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are
worth 1 point.

For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points
because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If
there are multiple answers, return the smallest such index K.
"""
from typing import List

def bestRotation(A: List[int]) -> int:
    """
    Interval Stabbing Approach
    :param A:
    :return:
    """
    N = len(A)
    interval_overlap = [0] * N
    for i, a in enumerate(A):
        # Calculate the interval of rotation steps for which A[i] = a will not score point
        # left inclusive, right exclusive
        interval_left, interval_right = (i - a + 1) % N, (i + 1) % N
        interval_overlap[interval_left] -= 1
        interval_overlap[interval_right] += 1

        if interval_left > interval_right:
            # loop around then break into two intervals
            interval_overlap[0] -= 1
            # doesn't have to keep track of interval_overlap[N]

    smallest_overlap = -N
    rotation_steps = current_overlap = 0
    for i, score in enumerate(interval_overlap):
        current_overlap += score
        if current_overlap > smallest_overlap:
            smallest_overlap = current_overlap
            rotation_steps = i

    return rotation_steps

test_cases = [([2, 3, 1, 4, 0], 3)]
for input, expected_value in test_cases:
    assert bestRotation(input) == expected_value, "Expected %d Got %d" % (expected_value, bestRotation(input))