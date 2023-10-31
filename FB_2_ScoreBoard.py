from typing import List


def get_min_problem(N: int, S: List[int]) -> int:
    max_S = max(S)
    if max_S % 3 == 0:
        # if needed, trade one 3 for a pair of 1 + 2, to get residuals
        return max_S // 3 + any(s % 3 != 0 for s in S)
    elif max_S % 3 == 1 and 1 not in S and max_S - 1 not in S:
        # trade a pair of 1 + 3 for 2 + 2, to get the 2 when needed
        return max_S // 3 + 1
    return max_S // 3 + any(s % 3 == 1 for s in S) + any(s % 3 == 2 for s in S)


test_cases = [
    ((5, [1, 2, 3, 4, 5]), 3),
    ((4, [4, 3, 3, 4]), 2),
    ((4, [2, 4, 6, 8]), 4),
    ((1, [8]), 3),
    ((1, [9]), 3),
    ((2, [3, 9]), 3),
    ((2, [2, 8]), 3),
    ((3, [1, 2, 9]), 4),
    ((3, [1, 2, 8]), 4),
    ((3, [2, 4, 6]), 3),
    ((3, [2, 4, 7]), 3),  # 2 + 2 + 3
]
for (test_N, test_S), expected_value in test_cases:
    assert get_min_problem(test_N, test_S) == expected_value
