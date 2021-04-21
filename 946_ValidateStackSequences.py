"""
Given two sequences pushed and popped with _distinct_ values, return true if and only if this could have been the result
of a sequence of push and pop operations on an initially empty stack.
"""
from typing import List


def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    """
    Simulation to reconstruct push and pop sequence
    :param pushed: order in which numbers are added to the stack
    :param popped: proposed order in which numbers are popped out of stack
    :return: whether popped sequence is valid given pushed sequence
    """
    valid_until = 0
    stack = []
    for x in pushed:
        stack.append(x)
        while stack and valid_until < len(popped) and stack[-1] == popped[valid_until]:
            stack.pop()
            valid_until += 1

    return valid_until == len(popped)


test_cases = [([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
              ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
              ([10, 4, 11, 14, 3, 7, 0, 6, 12, 5, 1, 2, 8, 13, 9],
               [10, 3, 14, 7, 11, 4, 6, 12, 1, 8, 2, 5, 0, 9, 13], True), ]
for test_push, test_pop, expected_output in test_cases:
    assert validate_stack_sequences(test_push, test_pop) is expected_output
