"""
In a country popular for train travel, you have planned some train travelling one year in advance. The days of the year
that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:
- a 1-day pass is sold for costs[0] dollars;
- a 7-day pass is sold for costs[1] dollars;
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel
for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""
from typing import List, Dict


def min_cost_tickets(days: List[int], costs: List[int]) -> int:
    """
    :param days: list of days that travel on in strictly ascending order
            1 <= days.length <= 365
            1 <= days[i] <= 365
    :param costs: list of 3 costs, [for_1_day, for_7_day, for_30_day]
            1 <= costs[i] <= 1000
    :return: min cost for tickets to travel on days
    """
    total_days = len(days)
    durations = [1, 7, 30]

    def dynamic_programming_approach(day_start: int, ref_cost_cache: Dict[int, int]) -> int:
        """
        :param day_start: starting from days[day_start]
                0 <= day_start < total_days
        :param ref_cost_cache: cache reference to store {day_j: min cost for tickets after days[day_j]}
        :return: min cost of tickets to travel after days[day_start]
        """
        if day_start >= total_days:
            return 0
        elif day_start in ref_cost_cache:
            return ref_cost_cache[day_start]

        cost_after_day = float("inf")
        day_j = day_start
        for cost_i, duration_i in zip(costs, durations):
            while day_j < total_days and days[day_j] < days[day_start] + duration_i:
                day_j += 1
            cost_after_day = min(cost_after_day, dynamic_programming_approach(day_j, ref_cost_cache) + cost_i)

        ref_cost_cache[day_start] = cost_after_day
        return cost_after_day

    # {day_j: min cost for tickets after days[day_j]}
    cost_cache = {}
    return dynamic_programming_approach(0, cost_cache)


assert min_cost_tickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]) == 11
assert min_cost_tickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]) == 17
