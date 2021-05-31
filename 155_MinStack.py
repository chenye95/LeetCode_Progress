"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
"""
from typing import List, Tuple, Optional


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # each pushes push (x, current_min) onto the stack
        self.internal_stack: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        """
        :param val: pushes val onto the stack
        """
        current_min = self.get_min()
        if current_min is None or val < current_min:
            current_min = val
        self.internal_stack.append((val, current_min))

    def pop(self) -> Optional[int]:
        """
        :return: pop from top the stack, or None if stack is empty
        """
        if self.internal_stack:
            return self.internal_stack.pop()[0]
        else:
            return None

    def top(self) -> Optional[int]:
        """
        :return: top of the stack, or None if stack is empty
        """
        if self.internal_stack:
            return self.internal_stack[-1][0]
        else:
            return None

    def get_min(self) -> Optional[int]:
        """
        :return: current min value of the stack, or None if stack is empty
        """
        if self.internal_stack:
            return self.internal_stack[-1][1]
        else:
            return None


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[bool]]) -> None:
    test_object = MinStack()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "push":
            test_object.push(next_parameter[0])
        elif next_instruction == "pop":
            assert test_object.pop() == expected_value
        elif next_instruction == "top":
            assert test_object.top() == expected_value
        else:
            assert test_object.get_min() == expected_value


test_cases = [(["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
               [[], [-2], [0], [-3], [], [], [], []],
               [None, None, None, None, -3, -3, 0, -2]),
              (["MinStack", "push", "push", "push", "getMin", "push", "push", "push", "push", "push", "top", "push",
                "push", "getMin", "push", "getMin", "push", "push", "getMin", "push", "top", "push", "getMin", "push",
                "push", "push", "push", "getMin", "push", "push", "top", "push", "push", "getMin", "pop", "getMin",
                "push", "push", "getMin", "getMin", "push", "getMin", "pop", "push", "push", "push", "getMin", "push",
                "getMin", "getMin", "getMin", "pop", "getMin", "push", "push", "getMin", "top", "getMin", "push",
                "getMin", "getMin", "getMin", "getMin", "push", "getMin", "getMin", "getMin", "push", "getMin", "push",
                "getMin", "push", "getMin", "getMin", "getMin", "getMin", "pop", "getMin", "push", "getMin", "getMin",
                "push", "push", "pop", "push", "getMin", "push", "top", "top", "push", "push", "getMin", "pop",
                "getMin", "push", "top", "push", "getMin", "push", "getMin", "getMin"],
               [[], [85], [-99], [67], [], [-27], [61], [-97], [-27], [35], [], [99], [-66], [], [-89], [], [4], [-70],
                [], [52], [], [54], [], [94], [-41], [-75], [-32], [], [5], [29], [], [-78], [-74], [], [], [], [-58],
                [-44], [], [], [-64], [], [], [-45], [-99], [-27], [], [-96], [], [], [], [], [], [26], [-58], [], [],
                [], [25], [], [], [], [], [33], [], [], [], [71], [], [-62], [], [-78], [], [], [], [], [], [], [-30],
                [], [], [85], [-15], [], [-40], [], [72], [], [], [18], [59], [], [], [], [-59], [], [10], [], [9], [],
                []],
               [None, None, None, None, -99, None, None, None, None, None, 35, None, None, -99, None, -99, None, None,
                -99, None, 52, None, -99, None, None, None, None, -99, None, None, 29, None, None, -99, -74, -99, None,
                None, -99, -99, None, -99, -64, None, None, None, -99, None, -99, -99, -99, -96, -99, None, None, -99,
                -58, -99, None, -99, -99, -99, -99, None, -99, -99, -99, None, -99, None, -99, None, -99, -99, -99, -99,
                -78, -99, None, -99, -99, None, None, -15, None, -99, None, 72, 72, None, None, -99, 59, -99, None, -59,
                None, -99, None, -99, -99]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
