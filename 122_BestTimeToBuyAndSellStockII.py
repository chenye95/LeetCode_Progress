"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    # purchase or hold on day t if prices rises on day t + 1
    return sum([max(0, p_t_1 - p_t) for p_t_1, p_t in zip(prices[1:], prices[:-1])])


assert max_profit(prices=[7, 1, 5, 3, 6, 4]) == 7
assert max_profit(prices=[1, 2, 3, 4, 5]) == 4
assert max_profit(prices=[7, 6, 4, 3, 1]) == 0
