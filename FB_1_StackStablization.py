from typing import List


def get_min_deflated_disc_count(N: int, R: List[int]) -> int:
    this_disc_max = R[-1] - 1
    deflate_count = 0
    for d_i in reversed(R[:-1]):
        if this_disc_max <= 0:
            return -1
        elif d_i > this_disc_max:
            deflate_count += 1
        this_disc_max = min(d_i - 1, this_disc_max - 1)

    return deflate_count


test_cases = [
    ((5, [2, 5, 3, 6, 5]), 3),
    ((3, [100, 100, 100]), 2),
    ((4, [6, 5, 4, 3]), -1),
]
for (test_N, test_R), expected_value in test_cases:
    assert get_min_deflated_disc_count(test_N, test_R) == expected_value
