"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


def is_palindrome(s: str) -> bool:
    alpha_numeric_s = ''.join(x for x in s if x.isalpha() or x.isdigit()).lower()
    rev_s = alpha_numeric_s[::-1]
    return rev_s == alpha_numeric_s


assert is_palindrome("0P") is False
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False
