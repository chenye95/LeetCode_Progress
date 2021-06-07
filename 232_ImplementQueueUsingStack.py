"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the
 functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty
    operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque
    (double-ended queue) as long as you use only a stack's standard operations.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words,
 performing n operations will take overall O(n) time even if one of those operations may take longer.
"""
from typing import List, Optional


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack_1 = []
        self._stack_2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        pass

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        pass

    def peek(self) -> int:
        """
        Get the front element.
        """
        pass

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        pass


class MyQueueHeavyPush(MyQueue):
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self._stack_1:
            self._front = x
        while self._stack_1:
            self._stack_2.append(self._stack_1.pop())
        self._stack_1.append(x)
        while self._stack_2:
            self._stack_1.append(self._stack_2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._stack_1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._stack_1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._stack_1


class MyQueueHeavyPop(MyQueue):
    def __init__(self):
        super().__init__()
        self._front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Complexity: O(1)
        """
        if not self._stack_1:
            self.front = x
        self._stack_1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        Complexity: Amortized O(1); Worst Case O(n)
        """
        if not self._stack_2:
            while self._stack_1:
                self._stack_2.append(self._stack_1.pop())
        return self._stack_2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        Complexity: O(1)
        """
        return self._stack_2[-1] if self._stack_2 else self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._stack_1 and not self._stack_2


def run_simulation(object_class, instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = object_class()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "push":
            test_object.push(next_parameter[0])
        elif next_instruction == "pop":
            assert test_object.pop() == expected_value
        elif next_instruction == "peek":
            assert test_object.peek() == expected_value
        else:
            assert test_object.empty() is expected_value


test_cases = [(["MyQueue", "push", "push", "pop", "push", "push", "pop", "peek"],
               [[], [1], [2], [], [3], [4], [], []],
               [None, None, None, 1, None, None, 2, 3]),
              (["MyQueue", "push", "push", "peek", "pop", "empty"],
               [[], [1], [2], [], [], []],
               [None, None, None, 1, 1, False]), ]
for object_class in [MyQueueHeavyPush, MyQueueHeavyPop, ]:
    for test_instructions, test_parameters, test_expected_values in test_cases:
        run_simulation(object_class, test_instructions, test_parameters, test_expected_values)
