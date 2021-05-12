"""
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following
 procedure :
- let x be the sum of all elements currently in your array.
- choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
- You may repeat this procedure as many times as needed.

Return True if it is possible to construct the target array from A otherwise return False.
"""
import heapq
from typing import List


def is_possible(target: List[int]) -> bool:
    """
    Continuously subtract array total from the largest value in array to get the original value in that position

    :param target: starting array
    :return: if target_array is composed from [1] * len(target_array)
    """
    sum_total_except_biggest = sum(target)
    array_max_heap = [-num_i for num_i in target]
    heapq.heapify(array_max_heap)

    while True:
        biggest_value = -heapq.heappop(array_max_heap)
        sum_total_except_biggest -= biggest_value
        if biggest_value == 1 or sum_total_except_biggest == 1:
            return True

        if biggest_value < sum_total_except_biggest or sum_total_except_biggest == 0 or \
                biggest_value % sum_total_except_biggest == 0:
            return False

        # Handle significantly big cases
        biggest_value %= sum_total_except_biggest
        sum_total_except_biggest += biggest_value
        heapq.heappush(array_max_heap, -biggest_value)


test_cases = [([1], True),
              ([2], False),
              ([1, 2], True),
              ([1, 1, 2], False),
              ([1, 1000000000], True),
              ([5, 50], False),
              ([358, 524, 850, 152, 655, 941, 255, 980, 766, 131, 386, 478, 645, 863, 681, 270, 974, 852, 201, 203, 699,
                833, 198, 867, 779, 250, 173, 512, 832, 183, 935, 576, 388, 459, 531, 256, 596, 489, 941, 122, 511, 615,
                82, 239, 377], False),
              ([1441, 1, 1101, 11, 1, 41, 2601, 1, 1, 1, 1], True),
              ([1, 1, 1, 1, 593, 35521, 1, 142081, 1, 568321, 71041, 1, 1, 297, 1, 38, 1, 1, 9473, 1, 1, 17761, 1, 149,
                1, 4737, 1, 1, 284161, 1, 1, 1, 2369, 1, 75, 1, 1, 1], True), ]
for test_target_array, expected_output in test_cases:
    assert is_possible(test_target_array) is expected_output, test_target_array
