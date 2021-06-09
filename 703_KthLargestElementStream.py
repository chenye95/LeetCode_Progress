"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order,
 not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Returns the element representing the kth largest element in the stream.
"""
import heapq
from typing import List, Optional


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        :param k: 1 <= k <= 10000
        :param nums: 0 <= len(nums) <= 10000, -1e4 <= nums[i] <= 1e4
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        """
        guaranteed that there will be at least k elements in the array, i.e. len(nums) >= k - 1 when you search for the
         kth element.

        :param val: -1e4 <= val <= 1e4
        :return: kth largest element in the stream
        """
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = KthLargest(parameters[0][0], parameters[0][1])
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        assert test_object.add(parameters[i][0]) == expected_value, expected_value


test_cases = [(["KthLargest"] + ["add"] * 5000,
               [[1, []], ] + [[i] for i in range(5000)],
               [None] + list(range(5000))),
              (["KthLargest", "add", "add", "add", "add", "add"],
               [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
               [None, 4, 5, 5, 8, 8]),
              (["KthLargest", "add", "add", "add", "add", "add"],
               [[1, []], [-3], [-2], [-4], [0], [4]],
               [None, -3, -2, -2, 0, 4]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
