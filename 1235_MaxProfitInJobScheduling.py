"""
We have n jobs, where every job is scheduled to be done from start_time[i] to end_time[i], obtaining a profit of
profit[i].

You're given the start_time , end_time and profit arrays, you need to output the maximum profit you can take such that
there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
"""
from bisect import bisect
from typing import List


def job_scheduling(start_time: List[int], end_time: List[int], profit: List[int]) -> int:
    """
    :param start_time: length of n, job i starts at start_time[i]
    :param end_time: length of n, job i ends at end_time[i]
    :param profit: length of n, job i yields of a profit of profit[i]
    :return: max profit you can make without 2 overlapping jobs
    """
    jobs = sorted(zip(start_time, end_time, profit), key=lambda job_i: job_i[1])
    profit_by_time = [[0, 0]]  # max profit through end_t [(end_t, profit_end_t)]
    for start_i, end_i, profit_i in jobs:
        # find the max profit ending at or before start_i
        i = bisect(profit_by_time, [start_i + 1]) - 1
        if profit_by_time[i][1] + profit_i > profit_by_time[-1][1]:
            profit_by_time.append([end_i, profit_by_time[i][1] + profit_i])
    return profit_by_time[-1][1]


test_cases = [([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
              ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
              ([43, 13, 36, 31, 40, 5, 47, 13, 28, 16, 2, 11], [44, 22, 41, 41, 47, 13, 48, 35, 48, 26, 21, 39],
               [8, 20, 3, 19, 16, 8, 11, 13, 2, 15, 1, 1], 66),
              ([341, 22, 175, 424, 574, 687, 952, 439, 51, 562, 962, 890, 250, 47, 945, 914, 835, 937, 419, 343, 125,
                809, 807, 959, 403, 861, 296, 39, 802, 562, 811, 991, 209, 375, 78, 685, 592, 409, 369, 478, 417, 162,
                938, 298, 618, 745, 888, 463, 213, 351, 406, 840, 779, 299, 90, 846, 58, 235, 725, 676, 239, 256, 996,
                362, 819, 622, 449, 880, 951, 314, 425, 127, 299, 326, 576, 743, 740, 604, 151, 391, 925, 605, 770, 253,
                670, 507, 306, 294, 519, 184, 848, 586, 593, 909, 163, 129, 685, 481, 258, 764],
               [462, 101, 820, 999, 900, 692, 991, 512, 655, 578, 996, 979, 425, 893, 975, 960, 930, 991, 987, 524, 208,
                901, 841, 961, 878, 882, 412, 795, 937, 807, 957, 994, 963, 716, 608, 774, 681, 637, 635, 660, 750, 632,
                948, 771, 943, 801, 985, 476, 532, 535, 929, 943, 837, 565, 375, 854, 174, 698, 820, 710, 566, 464, 997,
                551, 884, 844, 830, 916, 970, 965, 585, 631, 785, 632, 892, 954, 803, 764, 283, 477, 970, 616, 794, 911,
                771, 797, 776, 686, 895, 721, 917, 920, 975, 984, 996, 471, 770, 656, 977, 922],
               [85, 95, 14, 72, 17, 3, 86, 65, 50, 50, 42, 75, 40, 87, 35, 78, 47, 74, 92, 10, 100, 29, 55, 57, 51, 34,
                10, 96, 14, 71, 63, 99, 8, 37, 16, 71, 10, 71, 83, 88, 68, 79, 27, 87, 3, 58, 56, 43, 89, 31, 16, 9, 49,
                84, 62, 30, 35, 7, 27, 34, 24, 33, 100, 25, 90, 79, 58, 21, 31, 30, 61, 46, 36, 45, 85, 62, 91, 54, 28,
                63, 50, 69, 48, 36, 77, 39, 19, 97, 20, 39, 48, 72, 37, 67, 72, 46, 54, 37, 53, 30], 998), ]
for test_start, test_end, test_profit, expected_output in test_cases:
    assert job_scheduling(test_start, test_end, test_profit) == expected_output
