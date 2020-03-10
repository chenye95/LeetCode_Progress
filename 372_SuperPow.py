"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer
given in the form of an array.
"""
from typing import List


def superPow(a: int, b: List[int]) -> int:
    mod_int = 1337
    return_val = 1
    for b_i in b:
        return_val = (return_val ** 10) * (a ** b_i) % mod_int
    return return_val


assert superPow(a=2, b=[1, 0]) == 1024
assert superPow(a=2, b=[3]) == 8
