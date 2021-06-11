"""
Given a list of daily temperatures temperature_list, return a list such that, for each day in the input, tells you how
many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put
0 instead.

For example, given the list of temperatures temperature_list = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range
[30, 100].
"""
from typing import List


def daily_temperatures(temperature_list: List[int]) -> List[int]:
    """
    :param temperature_list: list of temperatures on each day
    :return: how many days you would have to wait until a warmer temperature
    """
    day_warmer_than_today = []
    return_result = [0] * len(temperature_list)

    for today, today_temperature in enumerate(temperature_list):
        while day_warmer_than_today and today_temperature > temperature_list[day_warmer_than_today[-1]]:
            cold_day = day_warmer_than_today.pop()
            return_result[cold_day] = today - cold_day
        day_warmer_than_today.append(today)

    return return_result


test_cases = [([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]),
              ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
              ([30, 40, 50, 60], [1, 1, 1, 0]),
              ([30, 60, 90], [1, 1, 0]),
              ([64, 40, 49, 73, 72, 35, 68, 83, 35, 73, 84, 88, 96, 43, 74, 63, 41, 95, 48, 46, 89, 72, 34, 85, 72, 59,
                87, 49, 30, 32, 47, 34, 74, 58, 31, 75, 73, 88, 64, 92, 83, 64, 100, 99, 81, 41, 48, 83, 96, 92, 82, 32,
                35, 68, 68, 92, 73, 92, 52, 33, 44, 38, 47, 88, 71, 50, 57, 95, 33, 65, 94, 44, 47, 79, 41, 74, 50, 67,
                97, 31, 68, 50, 37, 70, 77, 55, 48, 30, 77, 100, 31, 100, 69, 60, 47, 95, 68, 47, 33, 64],
               [3, 1, 1, 4, 3, 1, 1, 3, 1, 1, 1, 1, 30, 1, 3, 2, 1, 25, 2, 1, 19, 2, 1, 3, 2, 1, 11, 5, 1, 1, 2, 1, 3,
                2, 1, 2, 1, 2, 1, 3, 2, 1, 0, 46, 3, 1, 1, 1, 30, 18, 5, 1, 1, 2, 1, 12, 1, 10, 5, 1, 2, 1, 1, 4, 3, 1,
                1, 11, 1, 1, 8, 1, 1, 5, 1, 3, 1, 1, 11, 1, 3, 2, 1, 1, 5, 3, 2, 1, 1, 0, 1, 0, 3, 2, 1, 0, 0, 2, 1,
                0]), ]
for test_temperature, expected_output in test_cases:
    assert daily_temperatures(test_temperature) == expected_output
