"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
from typing import List


def max_profit(k: int, prices: List[int]) -> int:
    """
    Dynamic Programming approach

    :param k: at most transactions to be made
    :param prices: daily prices of the stock
    :return: max profit from trading the stock with at most k transactions
    """
    if not prices or k == 0:
        return 0

    if 2 * k >= len(prices):
        # we can complete as many transactions as we want
        return sum(price_tomorrow - price_today
                   for price_today, price_tomorrow in zip(prices[:-1], prices[1:]) if price_tomorrow > price_today)

    n = len(prices)
    # prev_day = curr_day = [purchased_times][current_hold]
    # where 0 <= purchased_times <= k
    # and current_hold in (0, 1)
    max_price = max(prices)
    prev_day = [[-max_price, -max_price] for _ in range(k + 1)]
    curr_day = [[-max_price, -max_price] for _ in range(k + 1)]

    # set starting value, whether buy stock on day 0
    prev_day[0][0] = 0
    prev_day[1][1] = -prices[0]

    # fill the array
    for day_i in range(1, n):
        for buy_count in range(min(day_i, k) + 1):
            # no holding after day_i: either sit out or sell previously owned stock
            curr_day[buy_count][0] = max(prev_day[buy_count][0], prev_day[buy_count][1] + prices[day_i])
            # holding stock means at least 1 buy in the past
            if buy_count > 0:
                # holding stock after day_i: either hold previously owned stock or bought new stock
                curr_day[buy_count][1] = max(prev_day[buy_count][1], prev_day[buy_count - 1][0] - prices[day_i])
        prev_day = curr_day
        curr_day = [[-max_price, -max_price] for _ in range(k + 1)]

    return max(prev_day[j][0] for j in range(k + 1))


test_cases = [([2, 4, 1], 2, 2),
              ([3, 2, 6, 5, 0, 3], 2, 7),
              ([3, 3, 5, 0, 0, 3, 1, 4], 2, 6), ]
for test_prices, test_k, expected_output in test_cases:
    assert max_profit(prices=test_prices, k=test_k) == expected_output
