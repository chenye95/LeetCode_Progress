"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending
 order.

Note:
- Input contains only lowercase English letters.
- Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc"
or "zerone" are not permitted.
- Input length is less than 50,000.
"""
from collections import Counter


def origin_digits_counter_loop(s: str) -> str:
    """
    :param s: string of only lowercase English letters, containing an out-of-order representations of some digits 0-9.
    It is guaranteed to be valid
    :return: digits in ascending order
    """
    # Find in order of 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 by looking at character count of z, w, u, x, g, o, t, f, s, n
    look_up_order = [(0, 'z', Counter('zero')),
                     (2, 'w', Counter('two')),
                     (4, 'u', Counter('four')),
                     (6, 'x', Counter('six')),
                     (8, 'g', Counter('eight')),
                     (1, 'o', Counter('one')),
                     (3, 't', Counter('three')),
                     (5, 'f', Counter('five')),
                     (7, 's', Counter('seven')),
                     (9, 'i', Counter('nine')), ]
    count_s = Counter(s)
    found = [0] * len(look_up_order)
    for digit_i, c_i, representation_i in look_up_order:
        found[digit_i] = count_s[c_i]
        for _ in range(found[digit_i]):
            count_s -= representation_i

    return ''.join([str(i) * found_i for i, found_i in enumerate(found)])


def origin_digits_counter_embed(s: str) -> str:
    """
    Spell out the search order through counter calculations

    :param s: string of only lowercase English letters, containing an out-of-order representations of some digits 0-9.
    It is guaranteed to be valid
    :return: digits in ascending order
    """
    count_s = Counter(s)
    digit_counts = [
        count_s["z"],  # 0
        count_s["o"] - count_s["z"] - count_s["w"] - count_s["u"],  # 1
        count_s["w"],  # 2
        count_s["t"] - count_s["w"] - count_s["g"],  # 3
        count_s["u"],  # 4
        count_s["f"] - count_s["u"],  # 5
        count_s["x"],  # 6
        count_s["s"] - count_s["x"],  # 7
        count_s["g"],  # 8
        count_s["i"] - count_s["x"] - count_s["g"] - (count_s["f"] - count_s["u"]),  # 9
    ]
    return "".join(str(digit) * count_digit for digit, count_digit in enumerate(digit_counts))


test_cases = [("owoztneoer", "012"), ("fviefuro", "45"), ("zeroonetwothreefourfivesixseveneightnine", "0123456789"), ]
for origin_digits in [origin_digits_counter_embed, origin_digits_counter_loop]:
    for test_s, expected_output in test_cases:
        assert origin_digits(s=test_s) == expected_output, origin_digits.__name__
