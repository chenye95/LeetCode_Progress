def int_to_roman(num: int) -> str:
    """
    :param num: integer within the range from 1 to 3999.
    :return: Roman representation of integer num
    """
    current_num, str_list = num, []
    for large_rank, medium_rank, small_rank, large_chr, medium_chr, small_chr in [(1000, 500, 100, 'M', 'D', 'C'),
                                                                                  (100, 50, 10, 'C', 'L', 'X'),
                                                                                  (10, 5, 1, 'X', 'V', 'I'), ]:
        large_count = current_num // large_rank
        str_list.append(large_chr * large_count)
        current_num -= large_count * large_rank

        if current_num >= large_rank - small_rank:
            str_list.append(small_chr + large_chr)
            current_num -= (large_rank - small_rank)
        elif current_num >= medium_rank:
            str_list.append(medium_chr)
            current_num -= medium_rank
        elif current_num >= medium_rank - small_rank:
            str_list.append(small_chr + medium_chr)
            current_num -= (medium_rank - small_rank)

    return ''.join(str_list) + 'I' * current_num


def roman_to_int(s: str) -> int:
    """
    :param s: a valid Roman integer
    :return: integer value of a Roman integer string
    """
    translation_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    prev_added = 0
    for s_i in s:
        will_add = translation_map[s_i]
        if will_add > prev_added:
            int_val -= (2 * prev_added)
        int_val += will_add
        prev_added = will_add
    return int_val


test_cases = [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M"),
              (3, "III"), (4, "IV"), (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV"), ]
for test_int_val, test_roman_val in test_cases:
    assert int_to_roman(test_int_val) == test_roman_val, test_int_val
    assert roman_to_int(test_roman_val) == test_int_val, test_roman_val

for i in range(1, 4000):
    assert i == roman_to_int(int_to_roman(i)), i
