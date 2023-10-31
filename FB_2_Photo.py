def get_artistic_photograph_count(N: int, C: str, X: int, Y: int) -> int:
    # get acceptable B position for every available A position in PAB combo
    B_forward_count = [0] * N
    # get acceptable P position for every available A position in BAP combo
    P_forward_count = [0] * N

    sliding_window_len = Y - X + 1
    sliding_window = list(C[X: Y]) + ['#']
    current_position = sliding_window_len - 1
    sliding_window_B_count = sum(c_i == 'B' for c_i in sliding_window)
    sliding_window_P_count = sum(c_i == 'P' for c_i in sliding_window)

    for i, c_i in enumerate(C):
        if i > 0:
            if sliding_window[current_position] == 'B':
                sliding_window_B_count -= 1
            elif sliding_window[current_position] == 'P':
                sliding_window_P_count -= 1

        if i + Y < N:
            sliding_window[current_position] = C[i + Y]
            if sliding_window[current_position] == 'B':
                sliding_window_B_count += 1
            if sliding_window[current_position] == 'P':
                sliding_window_P_count += 1
        else:
            sliding_window[current_position] = '#'

        current_position = (current_position + 1) % sliding_window_len

        if c_i == 'A':
            B_forward_count[i] = sliding_window_B_count
            P_forward_count[i] = sliding_window_P_count

    position_count = 0
    sliding_window_B = B_forward_count[X: Y] + [0]
    sliding_window_P = P_forward_count[X: Y] + [0]
    current_position = sliding_window_len - 1
    sliding_sum_B = sum(sliding_window_B)
    sliding_sum_P = sum(sliding_window_P)

    for i, c_i in enumerate(C):
        if i > 0:
            sliding_sum_B -= sliding_window_B[current_position]
            sliding_sum_P -= sliding_window_P[current_position]

        if i + Y < N:
            sliding_window_B[current_position] = B_forward_count[i + Y]
            sliding_sum_B += B_forward_count[i + Y]
            sliding_window_P[current_position] = P_forward_count[i + Y]
            sliding_sum_P += P_forward_count[i + Y]
        else:
            sliding_window_P[current_position] = 0
            sliding_window_B[current_position] = 0

        current_position = (current_position + 1) % sliding_window_len

        if c_i == 'P':
            position_count += sliding_sum_B
        elif c_i == 'B':
            position_count += sliding_sum_P

    return position_count


test_cases = [
    ((5, 'APABA', 1, 2), 1),
    ((5, 'APABA', 2, 3), 0),
    ((8, '.PBAAP.B', 1, 3), 3),

    ((8, '.PBAAP.B', 1, 1), 0),
    ((8, '.PBAAP.B', 1, 8), 4),

    ((15, '.PBAAP.BABPPABP.', 3, 10), 7),
]
for (test_N, test_C, test_X, test_Y), expected_value in test_cases:
    assert get_artistic_photograph_count(test_N, test_C, test_X, test_Y) == expected_value
