"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums
 is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
    - "a->b" if a != b
    - "a" if a == b
"""
from typing import List


def summary_range(nums: List[int]) -> List[str]:
    """
    :param nums: sorted list of integers and 0 <= len(nums) <= 20
    :return: list of strings to summarize the nums list
    """
    if not nums:
        return []
    last_seen = interval_left = nums[0]

    return_list: List[str] = []

    for next_num in nums + [nums[-1] + 2]:
        if next_num > last_seen + 1:
            if last_seen > interval_left:
                return_list.append(str(interval_left) + '->' + str(last_seen))
            else:
                return_list.append(str(interval_left))
            interval_left = last_seen = next_num
        elif next_num > last_seen:
            last_seen = next_num

    return return_list


test_cases = [
    ([0, 1, 2, 4, 5, 7],
     ["0->2", "4->5", "7"]),
    ([0, 2, 3, 4, 6, 8, 9],
     ["0", "2->4", "6", "8->9"]),
    ([0, 1, 2, 4, 5, 7, 9, 10, 12, 14, 15, 16, 27, 28],
     ["0->2", "4->5", "7", "9->10", "12", "14->16", "27->28"]),
    ([-1],
     ["-1"]),
    ([-2147483648, -2147483647, 2147483647],
     ["-2147483648->-2147483647", "2147483647"]),
]
for test_nums, expected_output in test_cases:
    assert summary_range(test_nums) == expected_output
