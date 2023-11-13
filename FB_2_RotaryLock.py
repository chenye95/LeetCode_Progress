from typing import List, Dict, Tuple


def turn_digit_time(N: int, current_position: int, next_position: int) -> int:
    return min(abs(next_position - current_position), N - abs(next_position - current_position))
    """
    # alternatively can use this if branching
    if next_position > current_position:
        return min(next_position - current_position, current_position + N - next_position)
    else:
        return min(current_position - next_position, next_position + N - current_position)
    """


def get_min_code_entry_time(N: int, M: int, C: List[int]) -> int:
    last_step_time: Dict[Tuple[int, int], int] = {(1, 1): 0}

    for next_position in C:
        current_step_time = {}
        for current_combo, current_time in last_step_time.items():
            current_position = current_combo[0]
            next_time = current_time + turn_digit_time(N, current_position, next_position)
            proposed_combo = (next_position, current_combo[1])
            if proposed_combo not in current_step_time:
                current_step_time[proposed_combo] = next_time
            else:
                current_step_time[proposed_combo] = min(next_time, current_step_time[proposed_combo])

            current_position = current_combo[1]
            next_time = current_time + turn_digit_time(N, current_position, next_position)
            proposed_combo = (current_combo[0], next_position)
            if proposed_combo not in current_step_time:
                current_step_time[proposed_combo] = next_time
            else:
                current_step_time[proposed_combo] = min(next_time, current_step_time[proposed_combo])

        last_step_time = current_step_time

    return min(value for value in last_step_time.values())


test_cases = [
    ((3, 3, [1, 2, 3]), 2),
    ((10, 4, [9, 4, 4, 8]), 6),
]
for (test_N, test_M, test_C), expected_value in test_cases:
    assert get_min_code_entry_time(test_N, test_M, test_C) == expected_value
