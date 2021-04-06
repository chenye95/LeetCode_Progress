"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of
combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""
from typing import List


def change_coin(amount: int, coins: List[int]) -> int:
    """
    Unbound Knapsack problem

    :param amount: value to add up to
    :param coins: coins of different domination; assumed to have infinite number of each kind
    :return: number of combinations from coins to make up amount
    """
    combo_count = [1] + [0] * amount
    for coin_i in coins:
        for value in range(coin_i, amount + 1):
            combo_count[value] += combo_count[value - coin_i]
    return combo_count[-1]


test_cases = [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1), ]
for test_amount, test_coins, expected_output in test_cases:
    assert change_coin(amount=test_amount, coins=test_coins) == expected_output
