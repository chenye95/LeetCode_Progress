from typing import List


# Write any import statements here


def get_min_code_entry_time(N: int, M: int, C: List[int]) -> int:
    current_position = 1
    total_time = 0
    for next_position in C:
        total_time += min(abs(next_position - current_position), N - abs(next_position - current_position))
        """
        if next_position > current_position:
            total_time += min(next_position - current_position, current_position + N - next_position)
        else:
            total_time += min(current_position - next_position, next_position + N - current_position)
        """

        current_position = next_position

    return total_time


test_cases = [
    ((3, 3, [1, 2, 3]), 2),
    ((10, 4, [9, 4, 4, 8]), 11),
]
for (test_N, test_M, test_C), expected_value in test_cases:
    assert get_min_code_entry_time(test_N, test_M, test_C) == expected_value
