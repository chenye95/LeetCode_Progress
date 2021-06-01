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
from functools import cache
from typing import List


def min_cost_tickets_cache(days: List[int], costs: List[int]) -> int:
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

    @cache
    def dynamic_programming_approach(day_start: int) -> int:
        """
        :param day_start: starting from days[day_start]; 0 <= day_start < total_days
        :return: min cost of tickets to travel after days[day_start]
        """
        if day_start >= total_days:
            return 0

        cost_after_day = float("inf")
        day_j = day_start
        for cost_i, duration_i in zip(costs, durations):
            while day_j < total_days and days[day_j] < days[day_start] + duration_i:
                day_j += 1
            cost_after_day = min(cost_after_day, dynamic_programming_approach(day_j) + cost_i)

        return cost_after_day

    return dynamic_programming_approach(0)


def min_cost_tickets_dp(days: List[int], costs: List[int]) -> int:
    """
    :param days: list of days that travel on in strictly ascending order
            1 <= days.length <= 365
            1 <= days[i] <= 365
    :param costs: list of 3 costs, [for_1_day, for_7_day, for_30_day]
            1 <= costs[i] <= 1000
    :return: min cost for tickets to travel on days
    """
    min_costs = [0] * (days[-1] + 1)
    durations = [1, 7, 30]
    days_set = set(days)
    for day_i in range(1, days[-1] + 1):
        if day_i not in days_set:
            min_costs[day_i] = min_costs[day_i - 1]
        else:
            min_costs[day_i] = min(min_costs[max(0, day_i - duration_i)] + cost_i
                                   for duration_i, cost_i in zip(durations, costs))

    return min_costs[-1]


test_cases = [([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
              ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
              ([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37,
                38, 39, 41, 43, 44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84,
                85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134], 423),
              ([6, 9, 10, 14, 15, 16, 17, 18, 20, 22, 23, 24, 29, 30, 31, 33, 35, 37, 38, 40, 41, 46, 47, 51, 54, 57,
                59, 65, 70, 76, 77, 81, 85, 87, 90, 91, 93, 94, 95, 97, 98, 100, 103, 104, 105, 106, 107, 111, 112, 113,
                114, 116, 117, 118, 120, 124, 128, 129, 135, 137, 139, 145, 146, 151, 152, 153, 157, 165, 166, 173, 174,
                179, 181, 182, 185, 187, 188, 190, 191, 192, 195, 196, 204, 205, 206, 208, 210, 214, 218, 219, 221, 225,
                229, 231, 233, 235, 239, 240, 245, 247, 249, 251, 252, 258, 261, 263, 268, 270, 273, 274, 275, 276, 280,
                283, 285, 286, 288, 289, 290, 291, 292, 293, 296, 298, 299, 301, 303, 307, 313, 314, 319, 323, 325, 327,
                329, 334, 339, 340, 341, 342, 344, 346, 349, 352, 354, 355, 356, 357, 358, 359, 363, 364],
               [21, 115, 345], 3040), ]
for min_cost_tickets in [min_cost_tickets_cache, min_cost_tickets_dp, ]:
    for test_days, test_costs, expected_value in test_cases:
        assert min_cost_tickets(test_days, test_costs) == expected_value, min_cost_tickets.__name__
