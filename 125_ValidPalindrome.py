"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


def is_palindrome(s: str) -> bool:
    alpha_numeric_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return alpha_numeric_s == alpha_numeric_s[::-1]


assert is_palindrome("0P") is False
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False
