"""
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.
"""


def has_all_codes_set(s: str, k: int) -> bool:
    if len(s) - k + 1 < 1 << k:
        return False

    got_segments = {s[i - k: i] for i in range(k, len(s) + 1)}
    return len(got_segments) == 1 << k


def has_all_codes_bits(s: str, k: int) -> bool:
    if len(s) - k + 1 < 1 << k:
        return False

    need_to_find = 1 << k
    find_in_string = [False] * need_to_find
    binary_all_one = need_to_find - 1
    current_val = 0

    for i, s_i in enumerate(s):
        current_val = (current_val << 1) & binary_all_one
        if s_i == '1':
            current_val |= 1

        if i >= k - 1 and not find_in_string[current_val]:
            find_in_string[current_val] = True
            need_to_find -= 1
            if need_to_find == 0:
                return True

    return False


test_cases = [("00110110", 2, True),
              ("00110", 2, True),
              ("0110", 1, True),
              ("0110", 2, False),
              ("0000000001011100", 4, False), ]
for has_all_code in [has_all_codes_bits, has_all_codes_set]:
    for test_s, test_k, expected_output in test_cases:
        assert has_all_code(test_s, test_k) is expected_output
