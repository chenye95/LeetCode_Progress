"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find the two trade separately, not using DP;
    For DP solution please refer to 188
    :param prices: daily prices of the stock
    :return: max profit from trading the stock
    """
    if not prices:
        return 0

    n = len(prices)

    # best trade if we sell before day i, including day i
    max_profit_before_day_i = [0] * n
    min_price_before_day_i = prices[0]

    # best trade if we buy after day i, including day i
    max_profit_after_day_i = [0] * n
    max_price_after_day_i = prices[-1]

    for i in range(1, n):
        min_price_before_day_i = min(min_price_before_day_i, prices[i])
        max_profit_before_day_i[i] = max(max_profit_before_day_i[i - 1], prices[i] - min_price_before_day_i)
        max_price_after_day_i = max(max_price_after_day_i, prices[-1 - i])
        max_profit_after_day_i[-1 - i] = max(max_profit_after_day_i[-i], max_price_after_day_i - prices[-1 - i])

    return max(max_profit_before_day_i[i] + max_profit_after_day_i[i] for i in range(n))


assert max_profit(prices=[2, 4, 1]) == 2
assert max_profit(prices=[3, 2, 6, 5, 0, 3]) == 7
assert max_profit(prices=[3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert max_profit(prices=[0, 1, 1, 2, 2, 3, 3, 4]) == 4
assert max_profit(prices=[0, 1, 1, 2, 2, 3, 3, 4, 2, 1]) == 4
