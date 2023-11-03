"""
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the
 ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many icecream bars as
 possible.

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.
"""
from typing import List


def max_ice_cream_bars(costs: List[int], coins: int) -> int:
    """
    :param costs: list of n integers representing costs of n ice cream bars
    :param coins: initial endowments
    :return: max number of ice cream bar that the boy can buy with coins
    """
    if not costs:
        return 0
    costs.sort()
    accumulator, i = costs[0], 1
    while i < len(costs) and accumulator <= coins:
        accumulator += costs[i]
        i += 1
    return i - 1 if accumulator > coins else i


test_cases = [([1, 3, 2, 4, 1], 7, 4),
              ([10, 6, 8, 7, 7, 8], 5, 0),
              ([1, 6, 3, 1, 2, 5], 20, 6),
              ([27, 23, 33, 26, 46, 86, 70, 85, 89, 82, 57, 66, 42, 18, 18, 5, 46, 56, 42, 82, 52, 78, 4, 27, 96, 74,
                74, 52, 2, 24, 78, 18, 42, 10, 12, 10, 80, 30, 60, 38, 32, 7, 98, 26, 18, 62, 50, 42, 15, 14, 32, 86,
                93, 98, 47, 46, 58, 42, 74, 69, 51, 53, 58, 40, 66, 46, 65, 2, 10, 82, 94, 26, 6, 78, 2, 101, 97, 16,
                12, 18, 71, 5, 46, 22, 58, 12, 18, 62, 61, 51, 2, 18, 34, 12, 36, 58, 20, 12, 17, 70], 241, 24), ]
for test_costs, test_coins, expected_output in test_cases:
    assert max_ice_cream_bars(test_costs, test_coins) == expected_output
