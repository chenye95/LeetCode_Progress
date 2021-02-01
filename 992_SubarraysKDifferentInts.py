"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) sub array of A good if the number
of different integers in that sub array is exactly K. (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good sub arrays of A.
"""
from typing import List


def sub_array_with_k_distinct(a: List[int], k: int) -> int:
    """
    1. Sub_arrays that ends at a_j must have starting position in a range [left_1_j, left_2_j]
            - if a[i_1, ... j] and a[i_1 + 2, ... j] are both valid, then a[i_1 + 1, ..., j] must be valid
    2. left_1_j must be monotonically non-decreasing with j
            - if a[left_1_j, ..., j] is valid and a[left_1_j+1, ..., j+1] is valid then left_1_j <= left_1_j+1
    3. left_2_j must be monotonically non-decreasing with j
    """
    if k > len(a):
        return 0

    sub_array_count = left_1 = left_2 = 0
    window_count = {}

    for a_j in a:
        if a_j in window_count:
            window_count[a_j] += 1
        else:
            window_count[a_j] = 1

        if len(window_count) == k + 1:
            # more than k distinctive integers!
            # since left_2 represents barely has k elements, it is guaranteed that window_count[a[left_2]] == 1
            # or otherwise there is some elements in between a[left_2] and a_j that equals to a[left_2]
            # and left_2 will be further increased in previous rounds
            del window_count[a[left_2]]
            left_2 += 1
            left_1 = left_2

        if len(window_count) == k:
            while window_count[a[left_2]] > 1:
                window_count[a[left_2]] -= 1
                left_2 += 1
            sub_array_count += left_2 - left_1 + 1

    return sub_array_count


assert sub_array_with_k_distinct(a=[1, 2, 1, 2, 3], k=2) == 7
assert sub_array_with_k_distinct(a=[1, 2, 1, 3, 4], k=3) == 3
