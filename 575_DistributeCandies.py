"""
Alice has n candies, where the ith candy is of type candy_types[i]. Alice noticed that she started to gain weight, so
she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much,
 and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if
she only eats n / 2 of them.
"""
from typing import List


def distribute_candies(candy_types: List[int]) -> int:
    """
    :param candy_types: n candies each of type candy_types[i]
    :return: maximum number of candy types she can have when she only eats at most n / 2 candies
    """
    return min(len(candy_types) // 2, len(set(candy_types)))


test_cases = [([1, 1, 2, 2, 3, 3], 3),
              ([1, 1, 2, 3], 2),
              ([6, 6, 6, 6], 1), ]
for test_input, expected_output in test_cases:
    assert distribute_candies(test_input) == expected_output
