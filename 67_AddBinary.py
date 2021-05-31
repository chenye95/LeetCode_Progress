"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
"""


def add_binary(a: str, b: str) -> str:
    """
    :param a: non-empty binary string of 0 or 1, no leading 0s
    :param b: non-empty binary string of 0 or 1, no leading 0s
    :return: return sum of two binary strings, a and b, in binary format, no leading 0s
    """
    if a == '0':
        return b
    elif b == '0':
        return a

    singe_bit_lookup_map = {('0', '0', 0): ('0', 0),
                            ('0', '1', 0): ('1', 0),
                            ('1', '0', 0): ('1', 0),
                            ('1', '1', 0): ('0', 1),
                            ('0', '0', 1): ('1', 0),
                            ('0', '1', 1): ('0', 1),
                            ('1', '0', 1): ('0', 1),
                            ('1', '1', 1): ('1', 1), }

    # Ensure the two strings of same length
    short_str, long_str = (a[::-1], b[::-1]) if len(a) < len(b) else (b[::-1], a[::-1])

    result = ['0'] * len(long_str)
    carry_bit = 0

    bit_i = 0
    while bit_i < len(short_str):
        result[bit_i], carry_bit = singe_bit_lookup_map[(short_str[bit_i], long_str[bit_i], carry_bit)]
        bit_i += 1

    while bit_i < len(long_str) and carry_bit:
        result[bit_i], carry_bit = singe_bit_lookup_map[('0', long_str[bit_i], carry_bit)]
        bit_i += 1

    if bit_i < len(long_str):
        return ''.join(long_str[bit_i:])[::-1] + ''.join(result[:bit_i])[::-1]
    elif carry_bit:
        return '1' + ''.join(result[:bit_i])[::-1]
    else:
        return ''.join(result[:bit_i])[::-1]


test_cases = [("1010", "1011", "10101"),
              ("11", "1", "100"),
              ("100", "110010", "110110"), ]
for test_a, test_b, expected_c in test_cases:
    assert add_binary(a=test_a, b=test_b) == expected_c
