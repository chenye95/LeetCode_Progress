"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times) with the following restrictions:
- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cool down 1 day)
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    :param prices: prices of the asset of day i
    :return: max profit buying and selling of the stock, with cool down
    """
    if not prices:
        return 0
    state_sold = 0
    state_hold = -prices[0]
    state_rest = 0
    for t in range(len(prices)):
        previous_sold = state_sold
        # can only sell a stock that previously own
        state_sold = state_hold + prices[t]
        # hold a stock previously own or purchase one unit of stock
        state_hold = max(state_hold, state_rest - prices[t])
        # no holding nor action this period
        state_rest = max(state_rest, previous_sold)
    return max(state_sold, state_rest)


test_cases = [([1, 2, 3, 0, 2], 3), ([1], 0), ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9], 15), ]
for test_prices, expected_profit in test_cases:
    assert max_profit(prices=test_prices) == expected_profit
