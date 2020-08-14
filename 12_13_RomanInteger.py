def IntToRoman(num: int) -> str:
    """
    :param num: integer within the range from 1 to 3999.
    :return: Roman representation of integer num
    """

    def IntToRomanHelper(current_num: int, lag_rank: int, mid_rank: int, sml_rank: int,
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
    hundred_part, remainder = IntToRomanHelper(remainder, 1000, 500, 100, 'M', 'D', 'C')
    tens_part, remainder = IntToRomanHelper(remainder, 100, 50, 10, 'C', 'L', 'X')
    ind_part, remainder = IntToRomanHelper(remainder, 10, 5, 1, 'X', 'V', 'I')
    roman_int = hundred_part + tens_part + ind_part
    
    while remainder > 0:
        roman_int += 'I'
        remainder -= 1
    return roman_int


def RomanToInt(s: str) -> int:
    """
    :return: convert Roman integer string to int
    """
    trans_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    prev_added = 0
    for i in range(len(s)):
        will_add = trans_map[s[i]]
        if will_add > prev_added:
            int_val -= (2 * prev_added)
        int_val += will_add
        prev_added = will_add
    return int_val


assert IntToRoman(3) == "III"
assert IntToRoman(4) == "IV", IntToRoman(4)
assert IntToRoman(9) == "IX"
assert IntToRoman(58) == "LVIII"

assert RomanToInt("III") == 3
assert RomanToInt("IV") == 4
assert RomanToInt("IX") == 9
assert RomanToInt("LVIII") == 58
assert RomanToInt("MCMXCIV") == 1994
