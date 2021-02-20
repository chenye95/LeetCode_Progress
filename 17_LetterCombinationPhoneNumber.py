"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
letters.
"""
from itertools import product
from typing import List

num_to_chr = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z']}


def letter_combinations_1(digits: str) -> List[str]:
    def letter_combination_helper(prefix: str, ref_digits: str, idx: int) -> None:
        if idx < len(ref_digits) - 1:
            for c in num_to_chr[ref_digits[idx]]:
                letter_combination_helper(prefix + c, ref_digits, idx + 1)
        else:
            for c in num_to_chr[ref_digits[idx]]:
                return_result.append(prefix + c)

    if not digits:
        return []

    return_result = []
    letter_combination_helper('', digits, 0)
    return return_result


def letter_combinations_2(digits: str) -> List[str]:
    if not digits:
        return []
    A = [num_to_chr[d] for d in digits]
    return [''.join(a) for a in product(*A)]


for letter_combination_fn in [letter_combinations_1, letter_combinations_2]:
    assert letter_combination_fn("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert letter_combination_fn("") == []
    assert letter_combination_fn("2") == ["a", "b", "c"]
