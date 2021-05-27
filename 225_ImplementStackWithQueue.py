"""
Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions
 of a normal queue (push, top_value, pop, and empty).

Implement the MyStack class:
- void push(int x) Pushes element x to the top_value of the stack.
- int pop() Removes the element on the top_value of the stack and returns it.
- int top_value() Returns the element on the top_value of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
- You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is
    empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque
    (double-ended queue), as long as you use only a queue's standard operations.
"""
from collections import deque
from typing import Optional, List, Union


class MyStack:
    def __init__(self):
        """
        Simulate Last In First Out (LIFO) with 2 First In First Out (FIFO) queue
        """
        self.internal_queue = deque()
        self.top_value = None

    def push(self, x: int) -> None:
        """
        O(n) for push

        :param x: Push element x onto stack.
        """
        tmp_queue = deque([x])
        self.top_value = x
        while self.internal_queue:
            tmp_queue.append(self.internal_queue.popleft())
        self.internal_queue = tmp_queue

    def pop(self) -> Optional[int]:
        """
        O(1) for pop()

        :return: Removes the element on top_value of the stack and returns that element.
        """
        if not self.internal_queue:
            return None

        return_val = self.internal_queue.popleft()
        self.top_value = self.internal_queue[0] if self.internal_queue else None
        return return_val

    def top(self) -> Optional[int]:
        """
        :return: top_value element.
        """
        return self.top_value

    def empty(self) -> bool:
        """
        :return: whether the stack is empty.
        """
        return self.top_value is None


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[Union[int, bool]]]) -> None:
    test_object = MyStack()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "push":
            test_object.push(next_parameter[0])
        elif next_instruction == "pop":
            assert test_object.pop() == expected_value
        elif next_instruction == "top":
            assert test_object.top() == expected_value
        else:
            assert test_object.empty() is expected_value


test_cases = [(["MyStack", "push", "push", "top", "pop", "empty"],
               [[], [1], [2], [], [], []],
               [None, None, None, 2, 2, False]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
