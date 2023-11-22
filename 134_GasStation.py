"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank, and it costs cost[i] of gas to travel from the ith station to its next
 (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once
 in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""
from typing import List


def can_complete_circle(gas: List[int], cost: List[int]) -> int:
    """
    :param gas: at station i the car can add gas[i] oil
    :param cost: gas required to travel from station i to station i + 1
    :return: start with an empty gas tank, at station i, the car can complete the circle;
        the solution is guaranteed to be unique, if exists; else return -1
    """
    # Note if sum(gas) >= sum(cost) a solution is guaranteed to exist
    # if sum(gas) < sum(cost) no solution exist
    total_gas = total_cost = 0
    current_leg_gas_remain = 0
    start_station = 0

    i = -1
    for gas_i, cost_i in zip(gas, cost):
        i += 1
        current_leg_gas_remain += (gas_i - cost_i)
        total_gas += gas_i
        total_cost += cost_i

        if current_leg_gas_remain < 0:
            # try starting from the next station
            start_station = i + 1
            current_leg_gas_remain = 0

    # Guaranteed by set up that solution, if exists, will be unique
    return -1 if total_gas < total_cost else start_station


test_cases = [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
              ([2, 3, 4], [3, 4, 3], -1),
              ([1, 2, 3, 4, 3, 2, 4, 1, 5, 3, 2, 4], [1, 1, 1, 3, 2, 4, 3, 6, 7, 4, 3, 1], -1),
              ([31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8,
                9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
               [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], 15), ]
for test_gas, test_cost, expected_output in test_cases:
    assert can_complete_circle(test_gas, test_cost) == expected_output
