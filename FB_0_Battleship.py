from typing import List


def get_hit_probability(R: int, C: int, G: List[List[int]]) -> float:
    contain_ship = sum([sum(i) for i in zip(*G)])
    return float(contain_ship) / R / C


test_cases = [
    ((2, 3, [[0, 0, 1], [1, 0, 1]]), .5),
    ((2, 2, [[1, 1], [1, 1]]), 1.),
]
for (test_R, test_C, test_G), expected_value in test_cases:
    assert get_hit_probability(test_R, test_C, test_G) == expected_value
