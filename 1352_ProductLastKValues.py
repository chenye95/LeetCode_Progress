"""
Implement the class ProductOfNumbers that supports two methods:

- 1. add(int num)
    Adds the number num to the back of the current list of numbers.
- 2. getProduct(int k)
    Returns the product of the last k numbers in the current list.

You can assume that always the current list has at least k numbers.

At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing
"""
from typing import List, Optional


class ProductOfNumbers:

    def __init__(self):
        self.product_first_k: List[int] = [1]

    def add_number(self, number: int) -> None:
        """
        :param number: add number to the data structure
        """
        if number == 0:
            # Note if last k values contains 0, then the product will be 0
            self.product_first_k = [1]
        else:
            self.product_first_k.append(number * self.product_first_k[-1])

    def get_product(self, k: int) -> int:
        """
        :param k: assume the current list has at least k numbers
        :return: product of the last k numbers
        """
        if k >= len(self.product_first_k):
            # product_first_k has been reset
            # last k values contains at least one 0
            return 0
        else:
            return self.product_first_k[-1] // self.product_first_k[-k - 1]


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = ProductOfNumbers()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "add":
            test_object.add_number(next_parameter[0])
        else:
            assert test_object.get_product(next_parameter[0]) == expected_value


test_cases = [(["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add",
                "getProduct"], [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]],
               [None, None, None, None, None, None, 20, 40, 0, None, 32]),
              (["ProductOfNumbers", "add", "getProduct", "getProduct", "add", "add", "getProduct", "add", "getProduct",
                "add", "getProduct", "add", "getProduct", "getProduct", "add", "getProduct"],
               [[], [7], [1], [1], [4], [5], [3], [4], [4], [3], [4], [8], [1], [6], [2], [3]],
               [None, None, 7, 7, None, None, 140, None, 560, None, 240, None, 8, 13440, None, 48]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
