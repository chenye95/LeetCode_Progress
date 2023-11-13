from typing import List


def get_max_profits(N: int, V: List[int], C: int, S: float) -> float:
    retention_prob = 1. - S
    best_pick_up_schedule = [0.] * N
    for end_of_day in range(N):
        if end_of_day == 0:
            best_pick_up_schedule[0] = V[0] - C
        else:
            best_strategy = -C
            left_on_table = V[end_of_day]
            discount_factor = 1.
            for last_picked_up in range(end_of_day - 1, -1, -1):
                this_strategy = best_pick_up_schedule[last_picked_up] + left_on_table - C
                if this_strategy > best_strategy:
                    best_strategy = this_strategy
                discount_factor *= retention_prob
                left_on_table += V[last_picked_up] * discount_factor

            best_pick_up_schedule[end_of_day] = max(left_on_table - C, best_strategy)

    # Special Case: never picking up anything at all
    return max(max(best_pick_up_schedule), 0.)


test_cases = [
    ((5, [10, 2, 8, 6, 4], 5, 0.0), 25.),
    ((5, [10, 2, 8, 6, 4], 5, 1.0), 9.),
    ((5, [10, 2, 8, 6, 4], 3, 0.5), 17.),
    ((5, [10, 2, 8, 6, 4], 3, 0.15), 20.10825),
    ((5, [10, 2, 8, 6, 4], 1000, 0.15), 0.),
]
epsilon = 0.00001
for (test_N, test_V, test_C, test_S), expected_value in test_cases:
    got_value = get_max_profits(test_N, test_V, test_C, test_S)
    assert expected_value - epsilon <= got_value <= expected_value + epsilon, (got_value, expected_value)
