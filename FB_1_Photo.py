def get_artistic_photograph_count(N: int, C: str, X: int, Y: int) -> int:
    # get acceptable B position for every available A position in PAB combo
    B_forward_count = [0] * N
    # get acceptable P position for every available A position in BAP combo
    P_forward_count = [0] * N
    for i, c_i in enumerate(C):
        if c_i == 'A':
            B_forward_count[i] = sum([c_i == 'B' for c_i in C[i + X: i + Y + 1]])
            P_forward_count[i] = sum([c_i == 'P' for c_i in C[i + X: i + Y + 1]])

    position_count = 0
    for i, c_i in enumerate(C):
        if c_i == 'P':
            position_count += sum(B_forward_count[i + X: i + Y + 1])
        if c_i == 'B':
            position_count += sum(P_forward_count[i + X: i + Y + 1])

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
