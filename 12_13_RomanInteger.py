def int_to_roman(num: int) -> str:
    """
    :param num: integer within the range from 1 to 3999.
    :return: Roman representation of integer num
    """

    def int_to_roman_helper(current_num: int, lag_rank: int, mid_rank: int, sml_rank: int,
                            lag_chr: chr, mid_chr: chr, sml_chr: chr):
        ret_str = ""
        while current_num >= lag_rank:
            ret_str += lag_chr
            current_num -= lag_rank
        if current_num >= (lag_rank - sml_rank):
            ret_str += (sml_chr + lag_chr)
            current_num -= (lag_rank - sml_rank)
        elif current_num >= mid_rank:
            ret_str += mid_chr
            current_num -= mid_rank
        elif current_num >= (mid_rank - sml_rank):
            ret_str += (sml_chr + mid_chr)
            current_num -= (mid_rank - sml_rank)
        return ret_str, current_num

    remainder = num
    hundred_part, remainder = int_to_roman_helper(remainder, 1000, 500, 100, 'M', 'D', 'C')
    tens_part, remainder = int_to_roman_helper(remainder, 100, 50, 10, 'C', 'L', 'X')
    ind_part, remainder = int_to_roman_helper(remainder, 10, 5, 1, 'X', 'V', 'I')

    return hundred_part + tens_part + ind_part + 'I' * remainder


def roman_to_int(s: str) -> int:
    """
    :return: convert Roman integer string to int
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


test_cases = [(3, "III"), (4, "IV"), (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV")]
for test_int_val, test_roman_val in test_cases:
    assert int_to_roman(test_int_val) == test_roman_val, test_int_val
    assert roman_to_int(test_roman_val) == test_int_val, test_roman_val

for i in range(1, 4000):
    assert i == roman_to_int(int_to_roman(i)), i
