"""
You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that
 calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:
1. If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise,
    copy the last m elements of the stream to a separate container.
2. Remove the smallest k elements and the largest k elements from the container.
3. Calculate the average value for the rest of the elements rounded down to the nearest integer.

Implement the MKAverage class:
- MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
- void addElement(int num) Inserts a new element num into the stream.
- int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest
    integer.
"""
from collections import deque
from typing import List, Optional

from sortedcontainers import SortedList


class MKAverage:
    LESS_THAN_M_ELEMENT = -1

    def __init__(self, m: int, k: int):
        """
        :param m: 3 <= m <= 1e5
        :param k: 1 <= 2 * k <= m
        """
        self.k = k
        self.m = m
        # stream of last m elements
        self.stream = deque()
        # sorted list of the last m elements
        self.sorted_m = SortedList()
        # sum of k smallest elements
        self.sum_bottom_k = 0
        # sum of m - k smallest elements
        self.sum_bottom_m_minus_k = 0

    def add_element(self, num: int) -> None:
        """
        :param num: 1 <= num <= 1e5
        """
        self.stream.append(num)

        if len(self.stream) > self.m:
            drop_off_num = self.stream.popleft()
            r = self.sorted_m.bisect_right(drop_off_num)
            # Update self.sum_bottom_k
            if r <= self.k:
                self.sum_bottom_k -= drop_off_num
                self.sum_bottom_k += self.sorted_m[self.k]
            # Update self.sum_bottom_m_minus_k
            if r <= self.m - self.k:
                self.sum_bottom_m_minus_k -= drop_off_num
                self.sum_bottom_m_minus_k += self.sorted_m[self.m - self.k]
            self.sorted_m.remove(drop_off_num)

        r = self.sorted_m.bisect_right(num)
        # Update self.sum_bottom_k
        if r < self.k:
            if len(self.sorted_m) >= self.k:
                self.sum_bottom_k -= self.sorted_m[self.k - 1]
            self.sum_bottom_k += num
        # Update self.sum_bottom_m_minus_k
        if r < self.m - self.k:
            if len(self.sorted_m) >= self.m - self.k:
                self.sum_bottom_m_minus_k -= self.sorted_m[self.m - self.k - 1]
            self.sum_bottom_m_minus_k += num
        self.sorted_m.add(num)

    def calculate_mk_average(self) -> int:
        """
        :return: return average of the middle (m - 2 * k) values if stream have reached m elements,
            else LESS_THAN_M_ELEMENT
        """
        if len(self.sorted_m) < self.m:
            return MKAverage.LESS_THAN_M_ELEMENT
        return (self.sum_bottom_m_minus_k - self.sum_bottom_k) // (self.m - self.k * 2)


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = MKAverage(parameters[0][0], parameters[0][1])
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "addElement":
            test_object.add_element(parameters[i][0])
        else:
            assert test_object.calculate_mk_average() == expected_value


test_cases = [(["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage",
                "addElement", "addElement", "addElement", "calculateMKAverage"],
               [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []],
               [None, None, None, MKAverage.LESS_THAN_M_ELEMENT, None, 3, None, None, None, 5]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
