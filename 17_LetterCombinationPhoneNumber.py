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


def letter_combinations_recurse(digits: str) -> List[str]:
    """
    Recursive call methods

    :param digits: a string containing digits from 2-9 inclusive
    :return: all possible letter combinations that the number can represent on a phone
    """

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


def letter_combinations_product(digits: str) -> List[str]:
    """
    Use itertools.product

    :param digits: a string containing digits from 2-9 inclusive
    :return: all possible letter combinations that the number can represent on a phone
    """
    if not digits:
        return []
    A = [num_to_chr[d] for d in digits]
    return [''.join(a) for a in product(*A)]


test_cases = [("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
              ("", []),
              ("2", ["a", "b", "c"]), ]
for letter_combination_fn in [letter_combinations_recurse, letter_combinations_product]:
    for test_digits, expected_output in test_cases:
        assert sorted(letter_combination_fn(digits=test_digits)) == sorted(expected_output), \
            letter_combination_fn.__name__
