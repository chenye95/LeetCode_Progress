"""
You are spectating a programming contest with N competitors, each trying to independently solve the same set of
programming problems. Each problem has a point value, which is either 1 or 2.

On the scoreboard, you observe that the ith competitor has attained a score of S_i, which is a positive integer equal to
 the sum of the point values of all the problems they have solved.

The scoreboard does not display the number of problems in the contest, nor their point values. Using the information
 available, you would like to determine the minimum possible number of problems in the contest
"""
from typing import List


def get_min_problem_count(N: int, S: List[int]) -> int:
    return max(S) // 2 + max([s % 2 for s in S])


test_cases = [
    ((6, [1, 2, 3, 4, 5, 6]), 4),
    ((4, [4, 3, 3, 4]), 3),
    ((4, [2, 4, 6, 8]), 4),
]
for (test_N, test_S), expected_value in test_cases:
    assert get_min_problem_count(test_N, test_S) == expected_value
