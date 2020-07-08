"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
and empty spaces.
"""


def calculate(s: str) -> int:
    # stack used to handle parenthesis;
    # memory to store states before (, to be retrieved after encountering )
    parentheses_stack = []
    sign = 1  # 1 or -1 to keep track of + or minus
    operand = 0
    eval_result = 0

    for c in s:
        if c.isdigit():
            # construct the number/operand
            operand = 10 * operand + int(c)
        elif c == '+':
            # Evaluate expression to the left
            eval_result += sign * operand
            # Set sign = 1 to keep track of +
            # Reset operand
            sign, operand = 1, 0
        elif c == '-':
            # Evaluate expression to the left
            eval_result += sign * operand
            # Set sign = -1 to keep track of -
            # Reset operand
            sign, operand = -1, 0
        elif c == '(':
            # Push current eval_result and sign on to the parentheses_stack, for later use
            parentheses_stack.append((eval_result, sign))
            # Reset to fresh start and calculate the sub-string between parentheses
            sign, eval_result = 1, 0
        elif c == ')':
            # Evaluate the expression to the left
            eval_result += sign * operand
            # Retrieve state before ( and evaluate with previous_result and sign
            previous_eval_result, sign = parentheses_stack.pop()
            eval_result = previous_eval_result + sign * eval_result
            # Reset operand to 0 for next step
            operand = 0
    return eval_result + sign * operand if operand != 0 else eval_result


test_cases = [('1 + 1 ', 2),
              ('2-1+ 2 ', 3),
              ('(1+(4+5+2)-3)+(6+8)', 23),
              ('    0    ', 0),
              ]
for s, expected in test_cases:
    assert calculate(s) == expected
