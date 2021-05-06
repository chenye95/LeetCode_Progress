"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.
"""


def calculate(s: str) -> int:
    """
    :param s: valid expression consists of int and operators '+', '-', '*', '/' separated by some number of spaces
    :return: value of the expression
    """
    current_operand = previous_operand = running_result = 0
    previous_sign = '+'

    # add a trailing + to force calculation of the final result
    for c in s + '+':
        if c == ' ':
            continue
        if c.isdigit():
            current_operand = 10 * current_operand + int(c)
            continue

        # c is a sign
        if previous_sign == '+':
            running_result += previous_operand
            previous_operand = current_operand
        elif previous_sign == '-':
            running_result += previous_operand
            previous_operand = -current_operand
        elif previous_sign == '*':
            previous_operand *= current_operand
        elif previous_sign == '/':
            previous_operand = int(previous_operand / current_operand)

        current_operand, previous_sign = 0, c

    return running_result + previous_operand


test_cases = [("3+2*2", 7),
              (" 3/2 ", 1),
              (" 3+5 / 2 ", 5),
              ("14-3/2", 13),
              ("0-2147483647", -2147483647),
              ("100-1-2-3-4-5-6-7-8-9-10", 45),
              ("876-142-978*2/8+4/2*2+40*2+282/2-137+855", 1433), ]
for test_s, expected_output in test_cases:
    assert calculate(test_s) == expected_output
