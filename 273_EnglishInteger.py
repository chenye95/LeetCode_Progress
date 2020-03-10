"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
"""
def IntToEnglish(num: int) -> str:
    """
    :param num: Positive Integer, less than a trillion
    :return: String
    """
    def IntToEnglishHelper(three_dig: int) -> str:
        if three_dig < 20:
            ret_str = to19Translation[three_dig-1]
        elif three_dig < 100:
            ret_str = toTens[int(three_dig/10)-2]
            if three_dig % 10 != 0:
                ret_str += ' ' + to19Translation[three_dig % 10 - 1]
        else:
            ret_str = to19Translation[int(three_dig/100)-1] + ' Hundred'
            if three_dig % 100 != 0:
                ret_str += (' ' + IntToEnglishHelper(three_dig % 100))
        return ret_str

    to19Translation = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
                      'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    toTens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    if num == 0:
        return "Zero"
    splitters = [' Trillion', ' Billion', ' Million', ' Thousand', '']
    ret_str = ""
    while num > 0:
        current_splitter = splitters.pop()
        three_dig = num % 1000
        num = int(num / 1000)
        if three_dig > 0:
            if ret_str:
                ret_str = IntToEnglishHelper(three_dig) + current_splitter + ' ' + ret_str
            else:
                ret_str = IntToEnglishHelper(three_dig) + current_splitter
    return ret_str


def EnglishToInt(num: str) -> int:
    splitters = {'Thousand': 10**3, 'Million': 10**6, 'Billion': 10**9, 'Trillion': 10**12}
    trans_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
                 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                 'Eleven': 11, 'Twelve': 12, 'Thirteen': 13, 'Fourteen': 14, 'Fifteen': 15,
                 'Sixteen': 16, 'Seventeen': 17, 'Eighteen': 18, 'Nineteen': 19,
                 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50, 'Sixty': 60,
                 'Seventy': 70, 'Eighty': 80, 'Ninety':90}
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


test_cases = (1234567, 1230567, 1000567, 1000700, 1000067, 123, 1000, 1020345000900)
for num in test_cases:
    assert num == EnglishToInt(IntToEnglish(num))
