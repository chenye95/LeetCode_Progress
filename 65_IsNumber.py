"""
Validate if a given string can be interpreted as a decimal number.
- Numbers 0-9
- Exponent - "e"
- Positive/negative sign - "+"/"-"
- Decimal point - "."
"""


def is_number(s: str) -> bool:
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


assert is_number("0")
assert is_number(" 0.1 ")
assert not is_number("abc")
assert not is_number("1 a")
assert is_number("2e10")
assert is_number(" -90e3   ")
assert not is_number(" 1e")
assert not is_number("e3")
assert is_number(" 6e-1")
assert not is_number(" 99e2.5 ")
assert is_number("53.5e93")
assert not is_number(" --6 ")
assert not is_number("-+3")
assert not is_number("95a54e53")
assert is_number(".1")
assert is_number("3.")
assert not is_number(".")
assert not is_number("46.e3")
