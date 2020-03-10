"""
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""
def isUgly(num: int) -> bool:
    factors = [2, 3, 5]
    if num <= 0:
        return False
    for factor_i in factors:
        while num % factor_i == 0:
            num = num // factor_i
    return num == 1


assert isUgly(6)
assert isUgly(8)
assert not isUgly(14)
