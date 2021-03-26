"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


def to_lower_case(input_str: str) -> str:
    steps = ord('a') - ord('A')
    return ''.join([c if 'a' <= c <= 'z' else chr(ord(c) + steps) if 'A' <= c <= 'Z' else c for c in input_str])


assert to_lower_case("here") == "here"
assert to_lower_case("Hello") == "hello"
assert to_lower_case("LOVELY") == "lovely"
