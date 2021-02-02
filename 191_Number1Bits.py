"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming
weight).
"""


def hamming_weight(n: int) -> int:
    counter = 0
    while n > 0:
        counter += (n % 2)
        n >>= 1
    return counter


assert hamming_weight(n=int('00000000000000000000000000001011', 2)) == 3
assert hamming_weight(n=int('00000000000000000000000010000000', 2)) == 1
assert hamming_weight(n=int('11111111111111111111111111111101', 2)) == 31
