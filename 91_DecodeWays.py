"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.
"""


def num_decoding(s: str) -> int:
    if s[0] == '0':
        return 0
    one_chr_before = two_chr_before = 1
    c_prev = s[0]
    for c_curr in s[1:]:
        if c_curr == '0':
            if c_prev == '1' or c_prev == '2':
                now_count = two_chr_before
            else:
                return 0
        elif c_prev == '1' or (c_prev == '2' and c_curr <= '6'):
            now_count = one_chr_before + two_chr_before
        else:
            now_count = one_chr_before
        one_chr_before, two_chr_before = now_count, one_chr_before
        c_prev = c_curr
    return one_chr_before


test_cases = [('226', 3), ('12', 2), ('0', 0), ('1', 1)]
for test_input, expected_output in test_cases:
    assert num_decoding(s=test_input) == expected_output, test_input
