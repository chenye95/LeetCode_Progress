from typing import List


def get_seconds_required(N: int, F: int, P: List[int]) -> int:
    """
    Best Strategy:
    - Starting from the lowest position
    - Move to the next occupied frog
    - Start leap frogging over each other, until reaching the next occupied position (time: P[i + 1] - P[i] - 1)
    - Repeat with the group
    - Until all frogs line up at the end;
    - Then again starting from the lowest position, jump off the trail (time F)
    """
    """ Raw implementation
    P_sorted = sorted(P + [N])
    step = 0
    for i in range(F):
        step += P_sorted[i + 1] - P_sorted[i] - 1
    step += F
    return step
    """

    """ Simplified version
    return (N - min(P) - F) + F
    """

    """ Further simplified
    """
    return N - min(P)


test_cases = [
    ((3, 1, [1]), 2),
    ((6, 3, [5, 2, 4]), 4),
]
for (test_N, test_F, test_P), expected_value in test_cases:
    assert get_seconds_required(test_N, test_F, test_P) == expected_value
