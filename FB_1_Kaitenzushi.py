from typing import List


def get_max_eaten_dish_count(N: int, D: List[int], K: int) -> int:
    scanning_window = [0] * K
    scanning_set = set()
    rotation_pointer = 0

    eaten_count = 0

    for i, d_i in enumerate(D):
        if d_i not in scanning_set:
            eaten_count += 1
            scanning_set.add(d_i)
            drop_dish = scanning_window[rotation_pointer]
            scanning_window[rotation_pointer] = d_i
            if drop_dish != 0:
                scanning_set.remove(drop_dish)
            rotation_pointer += 1
            if rotation_pointer == K:
                rotation_pointer = 0

    return eaten_count


test_cases = [
    ((6, [1, 2, 3, 3, 2, 1], 1), 5),
    ((6, [1, 2, 3, 3, 2, 1], 2), 4),
    ((7, [1, 2, 1, 2, 1, 2, 1], 2), 2),
]
for (test_N, test_D, test_K), expected_value in test_cases:
    assert get_max_eaten_dish_count(test_N, test_D, test_K) == expected_value
