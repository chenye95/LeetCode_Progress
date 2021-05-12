"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
"""


def is_valid(s: str) -> bool:
    """
    :param s: string of characters '(', ')', '{', '}', '[' and ']'
    :return: whether s is a valid parentheses string
    """
    if len(s) % 2:
        # len of s has to be an even number
        return False

    open_stack = [None]
    pair_map = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c not in pair_map:
            open_stack.append(c)
        elif open_stack.pop() != pair_map[c]:
            return False

    return len(open_stack) == 1


test_cases = [("()", True), ("()[]{}", True), ("(]", False), ("([)]", False), ("{[]}", True), ("[", False),
              ("[({(())}[()])]", True),
              ("[[[[[[[[[[[[[[[[[[[", False),
              ("[)[}[[{]}][]){[()]{[]]}", False), ]
for test_s, expected_output in test_cases:
    assert is_valid(test_s) is expected_output
