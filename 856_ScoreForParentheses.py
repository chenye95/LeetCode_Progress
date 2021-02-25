"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:
- () has score 1
- AB has score A + B, where A and B are balanced parentheses strings.
- (A) has score 2 * A, where A is a balanced parentheses string.
"""


def score_of_parentheses_stack(s: str) -> int:
    parentheses_stack = [0]

    for s_i in s:
        if s_i == '(':
            parentheses_stack.append(0)
        else:
            v = parentheses_stack.pop()
            parentheses_stack[-1] += max(2 * v, 1)

    return parentheses_stack.pop()


def score_of_parentheses_bit(s: str) -> int:
    if not s:
        return 0

    return_value = current_level = 0
    for i, s_i in enumerate(s):
        if s_i == '(':
            current_level += 1
        else:
            current_level -= 1
            if s[i - 1] == '(':
                return_value += 1 << current_level

    return return_value


test_cases = [("()", 1), ("(())", 2), ("()()", 2), ("(()(()))", 6)]
for score_of_parentheses in [score_of_parentheses_stack, score_of_parentheses_bit]:
    for test_input, expected_output in test_cases:
        assert score_of_parentheses(test_input) == expected_output
