"""
Given an integer array nums, handle multiple queries of the following types:
- Update the value of an element in nums.
- Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
 (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
from typing import List, Optional

from _Range_Query import RangeQueryActiveSumReplacement


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[bool]]) -> None:
    test_object = RangeQueryActiveSumReplacement(parameters[0][0])
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "update":
            test_object.update_segment_tree(next_parameter[0], next_parameter[1])
        else:
            assert test_object.query_segment_tree(next_parameter[0], next_parameter[1]) == expected_value


test_cases = [(["NumArray", "sumRange", "update", "sumRange"],
               [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]],
               [None, 9, None, 8]),
              (["NumArray", "sumRange", "update", "sumRange", "update", "update", "update", "sumRange", "sumRange",
                "update", "update"],
               [[[41, -53, -11, -58, 94, -18, -80, 10, -98, -3]], [5, 6], [1, 77], [0, 3], [5, 21], [0, -45], [8, 6],
                [7, 7], [9, 9], [4, 70], [5, 61]],
               [None, -98, None, 49, None, None, None, 10, -3, None, None]),
              (["NumArray", "update", "sumRange", "sumRange", "update", "sumRange"],
               [[[9, -8]], [0, 3], [1, 1], [0, 1], [1, -3], [0, 1]],
               [None, None, -8, -5, None, 0]),
              ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
