"""
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such
 that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with
 exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too
 large, return it modulo 10^9 + 7.
"""
from typing import List


def dice_simulator_build_up(n: int, consecutive_roll_max: List[int]) -> int:
    """
    :param n: simulate n dice rolls
    :param consecutive_roll_max: roll number i no more than consecutive_roll_max[i] times consecutively
    :return: distinct sequences that can be obtained with n rolls
    """
    _mod_value = 10 ** 9 + 7
    faces_count = 6
    dp_memory = [[0] * (faces_count + 1) for _ in range(n + 1)]
    # dp_memory[i][j] for 0 <= j < faces_count: # combinations with i rolls and the last face as j
    # dp_memory[i][faces_count]: # combinations with i rolls

    # Initialization
    # Roll i = 0 time, total combination is 1, by definition
    dp_memory[0][faces_count] = 1

    # Roll i = 1 time, each face will have 1 combination
    for j in range(faces_count):
        dp_memory[1][j] = 1
    # in total face_count combinations
    dp_memory[1][-1] = faces_count

    # Simulate from 2nd roll onwards
    for i in range(2, n + 1):
        for j in range(faces_count):
            # consider combinations ending with k * js, and not a j before that
            # 1 <= k <= min(i, consecutive_roll_max[j]
            for k in range(1, min(i, consecutive_roll_max[j]) + 1):
                dp_memory[i][j] += dp_memory[i - k][-1] - dp_memory[i - k][j]
        dp_memory[i][-1] = sum(dp_memory[i]) % _mod_value

    return dp_memory[-1][-1] % _mod_value


def dice_simulator_remove(n: int, consecutive_roll_max: List[int]) -> int:
    """
    :param n: simulate n dice rolls
    :param consecutive_roll_max: roll number i no more than consecutive_roll_max[i] times consecutively
    :return: distinct sequences that can be obtained with n rolls
    """
    _mod_value = 10 ** 9 + 7
    faces_count = 6
    dp_memory = [[0] * (faces_count + 1) for _ in range(n + 1)]
    # dp_memory[i][j] for 0 <= j < faces_count: # combinations with i rolls and the last face as j
    # dp_memory[i][faces_count]: # combinations with i rolls

    # Initialization
    # Roll i = 0 time, total combination is 1, by definition
    dp_memory[0][faces_count] = 1

    # Roll i = 1 time, each face will have 1 combination
    for j in range(faces_count):
        dp_memory[1][j] = 1
    # in total face_count combinations
    dp_memory[1][-1] = faces_count

    # Simulate from 2nd roll onwards
    for i in range(2, n + 1):
        for j in range(faces_count):
            # add j to all previous dp_memory[i - 1][-1] combinations
            # then subtract the ones that violate the consecutive_roll_max[j] rules
            dp_memory[i][j] = dp_memory[i - 1][-1]
            # remove combinations that now has (consecutive_roll_max[j] + 1) * js
            # i.e. with k - 1 = i - consecutive_roll_max[j] - 1 rolls, all combinations that does not end with j
            # note with k - 1 rolls, all combinations that ends with j already is excluded from dp_memory[i - 1][-1]
            k = i - consecutive_roll_max[j]
            if k >= 1:
                dp_memory[i][j] -= (dp_memory[k - 1][-1] - dp_memory[k - 1][j])

        dp_memory[i][-1] = sum(dp_memory[i]) % _mod_value

    return dp_memory[-1][-1] % _mod_value


test_cases = [(2, [1, 1, 2, 2, 2, 3], 34),
              (2, [1, 1, 1, 1, 1, 1], 30),
              (3, [1, 1, 1, 2, 2, 3], 181),
              (20, [8, 5, 10, 8, 7, 2], 822005673), ]
for dice_simulator in [dice_simulator_build_up, dice_simulator_remove]:
    for test_n, test_max_rolls, expected_output in test_cases:
        assert dice_simulator(test_n, test_max_rolls) == expected_output
