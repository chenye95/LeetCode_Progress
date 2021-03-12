"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


def coin_change_dfs(coins: List[int], amount: int) -> int:
    """
    DFS implementation
    """

    def dfs_helper(remainder: int, largest_coin_i: int, used_coin_count: int, ref_coins: List[int]) -> None:
        nonlocal global_min
        if remainder == 0:
            global_min = min(global_min, used_coin_count)

        for coin_j in range(largest_coin_i, len(ref_coins)):
            coin_value_j = ref_coins[coin_j]
            if remainder >= coin_value_j * (global_min - used_coin_count):
                break
            elif remainder >= coin_value_j:
                dfs_helper(remainder - coin_value_j, coin_j, used_coin_count + 1, ref_coins)

    coins.sort(reverse=True)
    global_min = amount + 1
    dfs_helper(amount, 0, 0, coins)
    return global_min if global_min <= amount else -1


def coin_change_dp(coins: List[int], amount: int) -> int:
    """
    DP implementation
    """
    coins.sort(reverse=True)
    memory = [0] + [amount + 1] * amount
    for coin_i in coins:
        for value_j in range(coin_i, amount + 1):
            if memory[value_j] > memory[value_j - coin_i] + 1:
                memory[value_j] = memory[value_j - coin_i] + 1
    return memory[-1] if memory[-1] <= amount else -1


for coin_change in [coin_change_dfs, coin_change_dp]:
    assert 3 == coin_change(coins=[1, 2, 5], amount=11)
    assert -1 == coin_change(coins=[2], amount=3)
    assert 0 == coin_change(coins=[1], amount=0)
    assert 20 == coin_change(coins=[186, 419, 83, 408], amount=6249)
