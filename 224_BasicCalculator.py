"""
Give a string s representing expression, implement a basic calculator to evaluate it.
"""


def calculate(s: str) -> int:
    """
    :param s: valid expression consists of digits, '+', '-', '(', ')', and ' '
    :return: value of the expression
    """
    operation_stack = []
    operand = eval_result = 0
    sign = 1  # 1 or -1 to keep track of + or - sign
    for c in s:
        if c == ' ':
            continue
        elif c.isdigit():
            # construct the operand
            operand = 10 * operand + int(c)
        elif c == '+':
            # evaluate expression to the left
            eval_result += sign * operand
            # set sign = 1 to keep track of +
            # reset operand
            sign, operand = 1, 0
        elif c == '-':
            # evaluate expression to the left
            eval_result += sign * operand
            # set sign = -1 to keep track of -
            # reset operand
            sign, operand = -1, 0
        elif c == '(':
            # Push eval_result and sign onto the stack, for later use
            operation_stack.append((eval_result, sign))
            sign, eval_result = 1, 0
        elif c == ')':
            # evaluate expression to the left
            # with prev_eval_result, prev_sign, current_sign and operand
            eval_result += sign * operand
            prev_eval_result, previous_sign = operation_stack.pop()
            eval_result = prev_eval_result + previous_sign * eval_result
            operand = 0

    return eval_result + sign * operand if operand else eval_result


test_cases = [("1 + 1", 2),
              ("2-1 + 2 ", 3),
              ("(1+(4+5+2)-3)+(6+8)", 23),
              ("2-4-(8+2-6+(8+4-(1)+8-10))", -15),
              ("1- (3+ 5 -2 +( 3+ 19 -(3-1-4+(9-4-(4-(1+( 3 )-2)- 5)+ 8 -(3- 5)-1)- 4)-5)-4+3-9)-4-(3+ 2-5)-10", -15), ]
for test_s, expected_output in test_cases:
    assert calculate(test_s) == expected_output
