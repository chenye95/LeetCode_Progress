"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


def to_lower_case(input_str: str) -> str:
    """
    :param input_str: a string of all kinds of character
    :return: return the same string in lowercase wherever there is an uppercase english letter
    """
    steps = ord('a') - ord('A')
    return ''.join([c if 'a' <= c <= 'z' else chr(ord(c) + steps) if 'A' <= c <= 'Z' else c for c in input_str])


test_cases = [("here", "here"), ("Hello", "hello"), ("LOVELY", "lovely"), ]
for test_input, expected_output in test_cases:
    assert to_lower_case(test_input) == expected_output
