"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from copy import deepcopy
from typing import List


def coin_change_dfs(coins: List[int], amount: int) -> int:
    """
    DFS implementation

    :param coins: list of denominations
    :param amount: total amount of money that exchange should add up to
    :return: number of ways coins combinations add up to amount, or -1 if no such combination exists
    """

    def dfs_helper(remainder: int, largest_coin_i: int, used_coin_count: int) -> None:
        nonlocal global_min
        if remainder == 0:
            global_min = min(global_min, used_coin_count)

        for coin_j in range(largest_coin_i, len(coins)):
            coin_value_j = coins[coin_j]
            if remainder >= coin_value_j * (global_min - used_coin_count):
                break
            elif remainder >= coin_value_j:
                dfs_helper(remainder - coin_value_j, coin_j, used_coin_count + 1)

    coins.sort(reverse=True)
    global_min = amount // min(coins) + 1
    dfs_helper(amount, 0, 0)
    return global_min if global_min < (amount // min(coins) + 1) else -1


def coin_change_dp(coins: List[int], amount: int) -> int:
    """
    DP implementation

    :param coins: list of denominations
    :param amount: total amount of money that exchange should add up to
    :return: number of ways coins combinations add up to amount, or -1 if no such combination exists
    """
    coins.sort(reverse=True)
    memory = [0] + [amount + 1] * amount
    for coin_i in coins:
        for value_j in range(coin_i, amount + 1):
            if memory[value_j] > memory[value_j - coin_i] + 1:
                memory[value_j] = memory[value_j - coin_i] + 1
    return memory[-1] if memory[-1] <= amount else -1


test_cases = [([1, 2, 5], 11, 3),
              ([2], 3, -1),
              ([1], 0, 0),
              ([186, 419, 83, 408], 6249, 20),
              ([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864, 24), ]
for test_coins, test_amount, expected_count in test_cases:
    assert coin_change_dp(deepcopy(test_coins), test_amount) == expected_count
for test_coins, test_amount, expected_count in test_cases[:-1]:
    # DFS records TLE on the last test
    assert coin_change_dfs(deepcopy(test_coins), test_amount) == expected_count
