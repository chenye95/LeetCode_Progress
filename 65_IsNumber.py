"""
Validate if a given string can be interpreted as a decimal number.
- Numbers 0-9
- Exponent - "e"
- Positive/negative sign - "+"/"-"
- Decimal point - "."
"""


def is_number(s: str) -> bool:
    """
    :return: whether s is a valid decimal number
    """

    def is_number_helper(s: str, can_have_decimal: bool = True, allow_empty_after_decimal: bool = True) -> bool:
        if len(s) == 0:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if can_have_decimal and '.' in s:
            sub_s = s.split('.')
            if sub_s[0] or sub_s[1]:
                return len(sub_s) == 2 \
                       and (not sub_s[0] or sub_s[0].isdigit()) \
                       and (allow_empty_after_decimal and not sub_s[1] or sub_s[1].isdigit())
            else:
                return False
        else:
            return s.isdigit()

    s = s.strip()
    if 'e' in s:
        sub_s = s.split('e')
        return len(sub_s) == 2 and is_number_helper(sub_s[0], allow_empty_after_decimal=False) \
               and is_number_helper(sub_s[1], can_have_decimal=False)
    else:
        return is_number_helper(s)


test_cases = [("0", True),
              (" 0.1 ", True),
              ("abc", False),
              ("1 a", False),
              ("2e10", True),
              (" -90e3   ", True),
              (" 1e", False),
              ("e3", False),
              (" 6e-1", True),
              (" 99e2.5 ", False),
              ("53.5e93", True),
              (" --6 ", False),
              ("-+3", False),
              ("95a54e53", False),
              (".1", True),
              ("3.", True),
              (".", False),
              ("46.e3", False), ]
for test_input, expected_output in test_cases:
    assert is_number(test_input) is expected_output
