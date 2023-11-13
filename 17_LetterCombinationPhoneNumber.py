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

    def letter_combination_helper(prefix: str, idx: int) -> None:
        if idx < len(digits) - 1:
            for c in num_to_chr[digits[idx]]:
                letter_combination_helper(prefix + c, idx + 1)
        else:
            for c in num_to_chr[digits[idx]]:
                return_result.append(prefix + c)

    if not digits:
        return []

    return_result = []
    letter_combination_helper('', 0)
    return return_result


def letter_combination_iterative(digits: str) -> List[str]:
    """
    Iterative list comprehension

    :param digits: a string containing digits from 2-9 inclusive
    :return: all possible letter combinations that the number can represent on a phone
    """
    if not digits:
        return []

    combination_list = ['']
    for digit in digits:
        combination_list = [rest + c for c in num_to_chr[digit] for rest in combination_list]
    return combination_list


def letter_combinations_product(digits: str) -> List[str]:
    """
    Use itertools.product

    :param digits: a string containing digits from 2-9 inclusive
    :return: all possible letter combinations that the number can represent on a phone
    """
    if not digits:
        return []
    chr_list = [num_to_chr[d] for d in digits]
    return [''.join(a) for a in product(*chr_list)]


test_cases = [("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
              ("", []),
              ("234",
               ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei",
                "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]),
              ("2", ["a", "b", "c"]),
              ("5678",
               ["jmpt", "jmpu", "jmpv", "jmqt", "jmqu", "jmqv", "jmrt", "jmru", "jmrv", "jmst", "jmsu", "jmsv", "jnpt",
                "jnpu", "jnpv", "jnqt", "jnqu", "jnqv", "jnrt", "jnru", "jnrv", "jnst", "jnsu", "jnsv", "jopt", "jopu",
                "jopv", "joqt", "joqu", "joqv", "jort", "joru", "jorv", "jost", "josu", "josv", "kmpt", "kmpu", "kmpv",
                "kmqt", "kmqu", "kmqv", "kmrt", "kmru", "kmrv", "kmst", "kmsu", "kmsv", "knpt", "knpu", "knpv", "knqt",
                "knqu", "knqv", "knrt", "knru", "knrv", "knst", "knsu", "knsv", "kopt", "kopu", "kopv", "koqt", "koqu",
                "koqv", "kort", "koru", "korv", "kost", "kosu", "kosv", "lmpt", "lmpu", "lmpv", "lmqt", "lmqu", "lmqv",
                "lmrt", "lmru", "lmrv", "lmst", "lmsu", "lmsv", "lnpt", "lnpu", "lnpv", "lnqt", "lnqu", "lnqv", "lnrt",
                "lnru", "lnrv", "lnst", "lnsu", "lnsv", "lopt", "lopu", "lopv", "loqt", "loqu", "loqv", "lort", "loru",
                "lorv", "lost", "losu", "losv"]), ]
for letter_combination_fn in [letter_combination_iterative, letter_combinations_recurse, letter_combinations_product, ]:
    for test_digits, expected_output in test_cases:
        assert sorted(letter_combination_fn(digits=test_digits)) == sorted(expected_output), \
            letter_combination_fn.__name__
