"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and
 the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""
from typing import List


def two_city_scheduling(costs: List[List[int]]) -> int:
    """
    Sort city by saving from choosing A over B; Schedule the first half to A, and remainder to B
    :param costs: list of pair [cost_a, cost_b], cost to fly to city A and city B respectively
    :return: minimum cost to fly N person to A and N to B
    """
    costs.sort(key=lambda c_i: c_i[0] - c_i[1])
    return sum(costs[i][0] for i in range(len(costs) // 2)) + \
           sum(costs[i][1] for i in range(len(costs) // 2, len(costs)))


assert two_city_scheduling([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
