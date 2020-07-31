"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you
would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range
[30, 100].
"""
from typing import List


def dailyTemperatures(T: List[int]) -> List[int]:
    """
    :param T: list of temperatures on each day
    :return: how many days you would have to wait until a warmer temperature
    """
    day_warmer_than_today = []
    return_result = [0] * len(T)

    for today in range(len(T)):
        while day_warmer_than_today and T[today] > T[day_warmer_than_today[-1]]:
            cold_day = day_warmer_than_today.pop()
            return_result[cold_day] = today - cold_day
        day_warmer_than_today.append(today)

    return return_result


assert dailyTemperatures(T=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]) == [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
assert dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
