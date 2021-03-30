"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very
right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job
is to output the median array for each window in the original array.
"""
from heapq import heappop, heappush
from typing import List, Tuple


def median_sliding_window(nums: List[int], k: int) -> List[float]:
    """
    :param nums: stream of integers that we need to process
    :param k: window size of the sliding window
    :return: median values of each sliding window
    """

    def move_heap(from_heap: List[Tuple[int, int]], to_heap: List[Tuple[int, int]]) -> None:
        """
        Move top of from_heap to to_heap; one of from_heap is a max_heap, the other is a min_heap
        """
        x, i = heappop(from_heap)
        heappush(to_heap, (-x, i))

    def get_window_median() -> float:
        """
        :return: median of current sliding window
        """
        # if k is odd, the median is stored as the smallest value in large_half, a min_heap
        # if k is even, the median is average of smallest value in large_half and the largest value in small_half
        return large_half[0][0] if k & 1 else (large_half[0][0] - small_half[0][0]) / 2.

    # Keep smaller half of the list in a max_heap, and bigger half in a min_heap
    # Enforce in the active sliding window, len(small_half) <= len(large_half) <= len(small_half) + 1
    small_half: List[Tuple[int, int]] = []
    large_half: List[Tuple[int, int]] = []

    for i, x in enumerate(nums[:k]):
        heappush(small_half, (-x, i))
    for _ in range((k + 1) // 2):
        # move half to large_half, round up the middle
        move_heap(small_half, large_half)

    window_medians = [get_window_median()]

    for i, x in enumerate(nums[k:]):
        # i starts from 0 again, need to offset by +k
        if x >= large_half[0][0]:
            # x belongs in large_half
            heappush(large_half, (x, i + k))
            # nums[i] would have fallen out sliding window
            # do not move one element from big_half to small_half, unless nums[i] belongs to small_half
            if nums[i] <= large_half[0][0]:
                move_heap(large_half, small_half)
        else:
            # x belongs in small_half
            heappush(small_half, (-x, i + k))
            # nums[i] would have fallen out sliding window
            # do not move one element from small_half to large_half, unless nums[i] belongs to large_half
            if nums[i] >= large_half[0][0]:
                move_heap(small_half, large_half)

        # all elements outside of [i + 1, i + k] falls out of scope
        while small_half and small_half[0][1] <= i:
            heappop(small_half)
        while large_half and large_half[0][1] <= i:
            heappop(large_half)

        window_medians.append(get_window_median())

    return window_medians


test_cases = [([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]), ]
for test_nums, test_k, expected_output in test_cases:
    assert median_sliding_window(nums=test_nums, k=test_k) == expected_output, test_nums
