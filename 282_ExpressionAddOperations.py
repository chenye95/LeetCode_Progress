"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not
unary) +, -, or * between the digits so that evaluate to the target value
"""
from typing import List


def add_operators(num: str, target: int) -> List[str]:
    """
    :param num: string that contains only digits 0-9
    :param target: target values to evaluate to
    :return: all possibilities to add binary operators +, -, or * between the digits so that evaluate to target value
    """
    return_result = []
    N = len(num)

    def recurse(curr_index: int, prev_operand: int, running_value: int, running_equation: str):
        # all digits have been processed
        if curr_index == N:
            if running_value == target:
                return_result.append(running_equation)
            return

        # Pruning: with +/-/*/No_Op, max value come out of num[curr_index:] is int(num[curr_index:]) with all No_Op
        # Prune if abs(prev_operand) * int(num[curr_index:]) < difference to target if prev_operand is not zero
        # or if int(num[curr_index:]) < difference to target if prev_operand is zero
        if max(1, abs(prev_operand)) * int(num[curr_index:]) < abs(target - running_value):
            return

        for i in range(curr_index, N):
            # take care of No_Op without recursion
            str_operand = num[curr_index:i + 1]
            if len(str_operand) > 1 and str_operand[0] == '0':
                # no leading 0s
                break

            curr_operand = int(str_operand)
            if curr_index == 0:
                # no leading operator
                recurse(i + 1, curr_operand, curr_operand, str_operand)
            else:
                # try out +/-/*
                recurse(i + 1, curr_operand, running_value + curr_operand, running_equation + '+' + str_operand)
                recurse(i + 1, -curr_operand, running_value - curr_operand, running_equation + '-' + str_operand)
                # * prioritize over +/-
                recurse(i + 1, prev_operand * curr_operand,
                        (running_value - prev_operand) + (prev_operand * curr_operand),
                        running_equation + '*' + str_operand)

    recurse(0, 0, 0, "")
    return return_result


assert set(add_operators(num="123", target=6)) == {"1+2+3", "1*2*3"}
assert set(add_operators(num="232", target=8)) == {"2*3+2", "2+3*2"}
assert set(add_operators(num="105", target=5)) == {"1*0+5", "10-5"}
assert set(add_operators(num="00", target=0)) == {"0+0", "0-0", "0*0"}
assert set(add_operators("123456789", 45)) == {"1*2*3*4*5-6-78+9", "1*2*3*4+5+6-7+8+9", "1*2*3+4+5+6+7+8+9",
                                               "1*2*3+4+5-6*7+8*9", "1*2*3+4-5*6+7*8+9", "1*2*3+4-5*6-7+8*9",
                                               "1*2*3-4*5+6*7+8+9", "1*2*3-4*5-6+7*8+9", "1*2*3-4*5-6-7+8*9",
                                               "1*2*3-45+67+8+9", "1*2*34+56-7-8*9", "1*2*34-5+6-7-8-9",
                                               "1*2+3*4-56+78+9", "1*2+3+4+5*6+7+8-9", "1*2+3+4-5+6*7+8-9",
                                               "1*2+3+4-5-6+7*8-9", "1*2+3+45+67-8*9", "1*2+3-45+6+7+8*9",
                                               "1*2+34+5-6-7+8+9", "1*2+34+56-7*8+9", "1*2+34-5+6+7-8+9",
                                               "1*2+34-56+7*8+9", "1*2+34-56-7+8*9", "1*2-3*4+5+67-8-9",
                                               "1*2-3+4-5-6*7+89", "1*2-3-4*5+67+8-9", "1*2-3-4+56-7-8+9",
                                               "1*2-34+5*6+7*8-9", "1*23+4*5-6+7-8+9", "1*23-4-56-7+89",
                                               "1+2*3*4*5+6+7-89", "1+2*3*4+5*6+7-8-9", "1+2*3*4-5+6*7-8-9",
                                               "1+2*3+4*5*6+7-89", "1+2*3+4*5-6+7+8+9", "1+2*3-4-5-6*7+89",
                                               "1+2*34-5*6+7+8-9", "1+2+3*4*5+6-7-8-9", "1+2+3*4+5+6*7-8-9",
                                               "1+2+3*45-6-78-9", "1+2+3+4+5+6+7+8+9", "1+2+3+4+5-6*7+8*9",
                                               "1+2+3+4-5*6+7*8+9", "1+2+3+4-5*6-7+8*9", "1+2+3-4*5+6*7+8+9",
                                               "1+2+3-4*5-6+7*8+9", "1+2+3-4*5-6-7+8*9", "1+2+3-45+67+8+9",
                                               "1+2-3*4*5+6+7+89", "1+2-3*4+5*6+7+8+9", "1+2-3*4-5+6*7+8+9",
                                               "1+2-3*4-5-6+7*8+9", "1+2-3*4-5-6-7+8*9", "1+2-3+4*5+6*7-8-9",
                                               "1+2-3+45+6-7-8+9", "1+2-3+45-6+7+8-9", "1+2-3-4-5*6+7+8*9",
                                               "1+2-3-45-6+7+89", "1+2-34+5+6+7*8+9", "1+2-34+5+6-7+8*9",
                                               "1+2-34-5-6+78+9", "1+23*4+5-6-7*8+9", "1+23*4-5-6*7+8-9",
                                               "1+23*4-56+7-8+9", "1+23+4+5+6+7+8-9", "1+23+4-5*6+7*8-9",
                                               "1+23+4-5-67+89", "1+23-4*5+6*7+8-9", "1+23-4*5-6+7*8-9",
                                               "1+23-4-5+6+7+8+9", "1+23-4-5-6*7+8*9", "1+23-45+67+8-9",
                                               "1-2*3*4+5-6+78-9", "1-2*3*4-5-6+7+8*9", "1-2*3+4*5+6+7+8+9",
                                               "1-2*3+4*5-6*7+8*9", "1-2*3+4+5+6*7+8-9", "1-2*3+4+5-6+7*8-9",
                                               "1-2*3+4+56+7-8-9", "1-2*3+45-67+8*9", "1-2*3-4+5*6+7+8+9",
                                               "1-2*3-4-5+6*7+8+9", "1-2*3-4-5-6+7*8+9", "1-2*3-4-5-6-7+8*9",
                                               "1-2*34+5*6-7+89", "1-2+3*4*5-6-7+8-9", "1-2+3+4-5*6+78-9",
                                               "1-2+3+45+6-7+8-9", "1-2+3-4*5-6+78-9", "1-2+3-45+6-7+89",
                                               "1-2-3*4+5+6+7*8-9", "1-2-3*4-5-6+78-9", "1-2-3+4-5+67-8-9",
                                               "1-2-3+45-6-7+8+9", "1-2-34+5+6+78-9", "1-2-34+56+7+8+9",
                                               "1-2-34-5+6+7+8*9", "1-23*4+5+6*7+89", "1-23+4*5-6*7+89",
                                               "1-23+4-5+67-8+9", "1-23+45-67+89", "1-23-4+5+67+8-9", "1-23-4-5-6-7+89",
                                               "12*3*4-5*6-78+9", "12*3+4+5+6-7-8+9", "12*3+4+5-6+7+8-9",
                                               "12*3-4-5-6+7+8+9", "12*3-4-56+78-9", "12+3*4+5+6-7+8+9",
                                               "12+3*45-6-7-89", "12+3+4-56-7+89", "12+3-4*5+67-8-9", "12+3-45+6+78-9",
                                               "12+34-5-6-7+8+9", "12-3*4*5+6+78+9", "12-3*4-5+67-8-9",
                                               "12-3+4*5+6-7+8+9", "12-3+4+56-7-8-9", "12-3-4+5*6-7+8+9",
                                               "12-3-4-56+7+89", "12-3-45-6+78+9"}
assert add_operators(num="3456237490", target=9191) == []
