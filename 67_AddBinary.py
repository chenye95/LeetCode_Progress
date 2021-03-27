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

    singe_bit_lookup_map = {('0', '0'): 0,
                            ('0', '1'): 1,
                            ('1', '0'): 1,
                            ('1', '1'): 2}

    # Ensure the two strings of same length
    len_diff = len(a) - len(b)
    if len_diff > 0:
        b = '0' * len_diff + b
    else:
        a = '0' * (-len_diff) + a

    result = ['0'] * len(a)

    carry_bit = 0
    l = len(a) - 1
    while l >= 0:
        s = singe_bit_lookup_map[(a[l], b[l])] + carry_bit
        if s >= 2:
            carry_bit = 1
            if s == 3:
                result[l] = '1'
        else:
            carry_bit = 0
            if s == 1:
                result[l] = '1'
        l -= 1
    if carry_bit:
        return '1' + ''.join(result)
    else:
        return ''.join(result)


test_cases = [("1010", "1011", "10101"),
              ("11", "1", "100"), ]
for test_a, test_b, expected_c in test_cases:
    assert add_binary(a=test_a, b=test_b) == expected_c
