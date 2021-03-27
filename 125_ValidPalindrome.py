"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


def is_palindrome(s: str) -> bool:
    """
    :return: whether the alphanumeric characters of s make a valid palindrome
    """
    alpha_numeric_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return alpha_numeric_s == alpha_numeric_s[::-1]


test_cases = [("0P", False),
              ("A man, a plan, a canal: Panama", True),
              ("race a car", False), ]
for test_s, expected_output in test_cases:
    assert is_palindrome(s=test_s) is expected_output
