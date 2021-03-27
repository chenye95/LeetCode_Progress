"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    :param prices: price of a stock by day
    :return: maximum profit from unlimited trade
    """
    # purchase or hold on day t if prices rises on day t + 1
    return sum([max(0, p_t_1 - p_t) for p_t_1, p_t in zip(prices[1:], prices[:-1])])


test_cases = [([7, 1, 5, 3, 6, 4], 7),
              ([1, 2, 3, 4, 5], 4),
              ([7, 6, 4, 3, 1], 0), ]
for test_prices, expected_profit in test_cases:
    assert max_profit(prices=test_prices) == expected_profit
