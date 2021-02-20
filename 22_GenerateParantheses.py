"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List


def generate_parenthesis(n: int) -> List[str]:
    def generate_helper(current_string: str, left_count: int, right_count: int) -> None:
        if left_count == n and right_count == n:
            return_list.append(current_string)
            return

        if left_count < n:
            generate_helper(current_string + '(', left_count + 1, right_count)
        if right_count < left_count:
            generate_helper(current_string + ')', left_count, right_count + 1)

    return_list = []
    generate_helper('', 0, 0)
    return return_list


test_cases = [(3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
              (1, {"()"})]
for n, expected_output in test_cases:
    assert expected_output == set(generate_parenthesis(n))
