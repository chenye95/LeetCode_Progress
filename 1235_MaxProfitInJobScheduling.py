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


assert job_scheduling(start_time=[1, 2, 3, 4, 6], end_time=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]) == 150
assert job_scheduling(start_time=[1, 2, 3, 3], end_time=[3, 4, 5, 6], profit=[50, 10, 40, 70]) == 120
