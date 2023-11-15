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

    :param k: at most transactions to be made, 1 <= k <= 100
    :param prices: daily prices of the stock, 1 <= len(prices) <= 1000, 0 <= prices[i] <= 1000
    :return: max profit from trading the stock with at most k transactions
    """
    _MAX_PRICES = 1000
    if not prices or k == 0:
        return 0

    if 2 * k >= len(prices):
        # we can complete as many transactions as we want
        return sum(max(price_tomorrow - price_today, 0) for price_today, price_tomorrow in zip(prices[:-1], prices[1:]))

    # prev_day = curr_day = [purchased_times][current_hold]
    # where 0 <= purchased_times <= k
    # and current_hold in (0, 1)
    prev_day = [[-_MAX_PRICES, -_MAX_PRICES] for _ in range(k + 1)]
    curr_day = [[-_MAX_PRICES, -_MAX_PRICES] for _ in range(k + 1)]

    # set starting value, whether buy stock on day 0
    prev_day[0][0] = 0
    prev_day[1][1] = -prices[0]

    # fill the array
    for day_i in range(1, len(prices)):
        for buy_count in range(min(day_i, k) + 1):
            # no holding after day_i: either sit out or sell previously owned stock
            curr_day[buy_count][0] = max(prev_day[buy_count][0], prev_day[buy_count][1] + prices[day_i])
            # holding stock means at least 1 buy in the past
            if buy_count > 0:
                # holding stock after day_i: either hold previously owned stock or bought new stock
                curr_day[buy_count][1] = max(prev_day[buy_count][1], prev_day[buy_count - 1][0] - prices[day_i])
        prev_day, curr_day = curr_day, prev_day

    return max(max(prev_day))


test_cases = [([2, 4, 1], 2, 2),
              ([3, 2, 6, 5, 0, 3], 2, 7),
              ([3, 3, 5, 0, 0, 3, 1, 4], 2, 6), ]
for test_prices, test_k, expected_output in test_cases:
    assert max_profit(prices=test_prices, k=test_k) == expected_output
