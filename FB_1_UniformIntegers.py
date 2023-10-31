from typing import Tuple


def parse_int(n: int) -> Tuple[int, int]:
    str_n = str(n)
    return len(str_n), int(str_n[0])


def get_uniform_ones(len_n) -> int:
    return int('1' * len_n)


def get_uniform_integer_count_in_interval(A: int, B: int) -> int:
    len_A, left_A = parse_int(A)
    len_B, left_B = parse_int(B)

    return_count = 0
    if len_A == len_B:
        if left_A == left_B:
            return_count += (A <= get_uniform_ones(len_B) * left_B <= B)
        else:
            # left_A < left_B
            return_count += left_B - left_A - 1
            return_count += (get_uniform_ones(len_A) * left_A >= A)
            return_count += (get_uniform_ones(len_B) * left_B <= B)

    else:
        # len_A < len_B
        return_count += 9 * (len_B - len_A - 1)
        return_count += left_B - 1 + (get_uniform_ones(len_B) * left_B <= B)
        return_count += 9 - left_A + (get_uniform_ones(len_A) * left_A >= A)

    return return_count


test_cases = [
    ((75, 333), 6),
    ((75, 300), 5),
    ((1, 9), 9),
    ((75, 3000), 3 + 9 + 2),
    ((999999999999, 999999999999), 1),
]
for (test_A, test_B), expected_value in test_cases:
    assert get_uniform_integer_count_in_interval(test_A, test_B) == expected_value, expected_value
