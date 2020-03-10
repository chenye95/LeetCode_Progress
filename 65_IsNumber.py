"""
Validate if a given string can be interpreted as a decimal number.
- Numbers 0-9
- Exponent - "e"
- Positive/negative sign - "+"/"-"
- Decimal point - "."
"""
def isNumber(s: str) -> bool:
    def isNumberHelper(s: str, canHaveDecimal: bool = True, emptyAfterDecimal: bool = True) -> bool:
        if len(s) == 0:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if canHaveDecimal and '.' in s:
            sub_s = s.split('.')
            if sub_s[0] or sub_s[1]:
                return len(sub_s) == 2 \
                   and (not sub_s[0] or sub_s[0].isdigit()) \
                   and (emptyAfterDecimal and not sub_s[1] or sub_s[1].isdigit())
            else:
                return False
        else:
            return s.isdigit()

    proc_s = s.strip()
    if 'e' in proc_s:
        sub_s = proc_s.split('e')
        return len(sub_s) == 2 and isNumberHelper(sub_s[0], emptyAfterDecimal=False)\
               and isNumberHelper(sub_s[1], canHaveDecimal=False)
    else:
        return isNumberHelper(proc_s)


assert isNumber("0")
assert isNumber(" 0.1 ")
assert not isNumber("abc")
assert not isNumber("1 a")
assert isNumber("2e10")
assert isNumber(" -90e3   ")
assert not isNumber(" 1e")
assert not isNumber("e3")
assert isNumber(" 6e-1")
assert not isNumber(" 99e2.5 ")
assert isNumber("53.5e93")
assert not isNumber(" --6 ")
assert not isNumber("-+3")
assert not isNumber("95a54e53")
assert isNumber(".1")
assert isNumber("3.")
assert not isNumber(".")
assert not isNumber("46.e3")
