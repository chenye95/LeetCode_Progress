"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:
- push(int x), which pushes an integer x onto the stack.
- pop(), which removes and returns the most frequent element in the stack.
    If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
"""
from collections import Counter, defaultdict
from typing import Any


class FrequencyStack(object):
    def __init__(self):
        # a map that records the frequency for each element, used to compute max_frequency
        self.frequency_map = Counter()
        # a list of stack to track the order in which the i_th occurrence of each element gets pushed onto the stack
        self.i_th_occurrence = defaultdict(list)
        # max frequency of any element in the stack
        self.max_frequency = 0

    def push(self, x: Any) -> None:
        """
        :param x: pushes an element x onto the stack
        """
        f = self.frequency_map[x] + 1
        self.frequency_map[x] = f
        if f > self.max_frequency:
            self.max_frequency = f
        self.i_th_occurrence[f].append(x)

    def pop(self) -> Any:
        """
        Removes and returns the most frequent element in the stack.
        If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned

        :return: most frequent element in the stack
        """
        x = self.i_th_occurrence[self.max_frequency].pop()
        self.frequency_map[x] -= 1
        while self.max_frequency and not self.i_th_occurrence[self.max_frequency]:
            self.max_frequency -= 1
        return x


test_stack = FrequencyStack()
for test_in in [5, 7, 5, 7, 4, 5]:
    test_stack.push(test_in)
expected_output = [5, 7, 5, 4, 7, 5]
assert [test_stack.pop() for _ in range(len(expected_output))] == expected_output
