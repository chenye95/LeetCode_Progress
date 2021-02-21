"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
"""


def int_to_english(num: int) -> str:
    """
    :param num: Positive Integer, less than a trillion
    :return: String
    """

    def int_to_english_helper(helper_three_dig: int) -> str:
        if helper_three_dig < 20:
            return to_19_translation[helper_three_dig - 1]
        elif helper_three_dig < 100:
            if helper_three_dig % 10 == 0:
                return to_tens[helper_three_dig // 10 - 2]
            else:
                return to_tens[helper_three_dig // 10 - 2] + ' ' + to_19_translation[helper_three_dig % 10 - 1]
        elif helper_three_dig % 100 == 0:
            return to_19_translation[helper_three_dig // 100 - 1] + ' Hundred'
        else:
            return to_19_translation[helper_three_dig // 100 - 1] + ' Hundred' + ' ' + \
                   int_to_english_helper(helper_three_dig % 100)

    to_19_translation = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
                        'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    to_tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    if num == 0:
        return "Zero"
    splitters = [' Trillion', ' Billion', ' Million', ' Thousand', '']
    ret_str = ""
    while num > 0:
        current_splitter = splitters.pop()
        three_dig = num % 1000
        num = num // 1000
        if three_dig > 0:
            if ret_str:
                ret_str = int_to_english_helper(three_dig) + current_splitter + ' ' + ret_str
            else:
                ret_str = int_to_english_helper(three_dig) + current_splitter
    return ret_str


def english_to_int(num: str) -> int:
    splitters = {'Thousand': 10 ** 3, 'Million': 10 ** 6, 'Billion': 10 ** 9, 'Trillion': 10 ** 12}
    trans_map = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                 'Nine': 9, 'Ten': 10, 'Eleven': 11, 'Twelve': 12, 'Thirteen': 13, 'Fourteen': 14, 'Fifteen': 15,
                 'Sixteen': 16, 'Seventeen': 17, 'Eighteen': 18, 'Nineteen': 19, 'Twenty': 20, 'Thirty': 30,
                 'Forty': 40, 'Fifty': 50, 'Sixty': 60, 'Seventy': 70, 'Eighty': 80, 'Ninety': 90}
    parts = num.split()
    ret_val = 0
    remainder = 0
    for part in parts:
        if part in splitters:
            ret_val += remainder * splitters[part]
            remainder = 0
        elif part == 'Hundred':
            remainder *= 100
        else:
            remainder += trans_map[part]
    return ret_val + remainder


test_cases = (0, 1_234_567, 1_230_567, 1_000_567, 1_000_700, 1_000_067, 123, 1_000, 1_020_345_000_900)
for test_num in test_cases:
    assert test_num == english_to_int(int_to_english(test_num))
