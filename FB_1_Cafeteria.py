import math
from typing import List


def get_max_additional_diners_count(N: int, K: int, M: int, S: List[int]) -> int:
    openings = []
    last_seat_right = 1
    for seat in sorted(S):
        seat_left = seat - K - 1
        if seat_left >= last_seat_right:
            openings.append((last_seat_right, seat_left))
        last_seat_right = seat + K + 1
    if last_seat_right < N:
        openings.append((last_seat_right, N))

    open_count = 0
    for opening_left, opening_right in openings:
        open_count += math.ceil((opening_right - opening_left + 1) / (K + 1))
    return open_count


test_cases = [
    ((10, 1, 2, [2, 6]), 3),
    ((10, 2, 2, [2, 6]), 1),
    ((15, 2, 3, [11, 6, 14]), 1),
]

for (test_N, test_K, test_M, test_S), expected_value in test_cases:
    assert get_max_additional_diners_count(test_N, test_K, test_M, test_S) == expected_value
