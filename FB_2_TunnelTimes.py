from typing import List


def quick_lookup(sorted_list: List[int], target: int) -> int:
    """
    :param sorted_list: assuming no duplicate in the list
    :param target: attempting to find target in sorted_list, such that sorted_list[i] <= target < sorted_list[i + 1]
    :return: the index i, such that sorted_list[i] <= target < sorted_list[i + 1]
    """
    if not sorted_list:
        return 0
    left, right = 0, len(sorted_list)
    mid_point = (left + right) // 2
    while left < mid_point:
        if sorted_list[mid_point] < target:
            left = mid_point
        elif sorted_list[mid_point] > target:
            right = mid_point
        else:
            return mid_point
        mid_point = (left + right) // 2

    return mid_point


def get_seconds_elapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    tunnel_list = [(A[i], B[i]) for i in range(N)]
    tunnel_list.sort()

    cumulative_tunnel = [0] * (N + 1)
    total_so_far = 0
    for i in range(N):
        total_so_far += tunnel_list[i][1] - tunnel_list[i][0]
        cumulative_tunnel[i + 1] = total_so_far

    if K % total_so_far == 0:
        completed_round = max(K // total_so_far - 1, 0)
        return completed_round * C + tunnel_list[-1][1]

    seconds_lapse = K // total_so_far * C
    left_to_travel = K % total_so_far
    crossed_tunnel_count = quick_lookup(cumulative_tunnel, left_to_travel)
    if cumulative_tunnel[crossed_tunnel_count] == left_to_travel:
        seconds_lapse += tunnel_list[crossed_tunnel_count - 1][1]
    else:
        seconds_lapse += tunnel_list[crossed_tunnel_count][0] + \
                         left_to_travel - cumulative_tunnel[crossed_tunnel_count]

    return seconds_lapse


test_cases = [
    ((10, 2, [1, 6], [3, 7], 7), 22),
    ((10, 2, [1, 6], [3, 7], 8), 23),
    ((10, 2, [1, 6], [3, 7], 9), 27),
    ((50, 3, [39, 19, 28], [49, 27, 35], 15), 35),
    ((50, 3, [39, 19, 28], [49, 27, 35], 8), 27),
    ((50, 3, [39, 19, 28], [49, 27, 35], 3), 22),
]
for (test_C, test_N, test_A, test_B, test_K), expected_value in test_cases:
    assert get_seconds_elapsed(test_C, test_N, test_A, test_B, test_K) == expected_value
