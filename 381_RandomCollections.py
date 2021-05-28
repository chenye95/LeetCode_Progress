"""
Implement the RandomizedCollection class:
- RandomizedCollection() Initializes the RandomizedCollection object.
- bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present,
    false otherwise.
- bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false
    otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
- int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one
    element exists when this method is called). The probability of each element being returned is linearly related to
    the number of same values the multiset contains.
"""
from typing import List, Union, Set

from _Randomized_Collection import RandomizedCollection


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Union[bool, Set[int], None]]) -> None:
    test_object = RandomizedCollection()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "insert":
            assert test_object.insert(next_parameter[0]) is expected_value
        elif next_instruction == "remove":
            assert test_object.remove(next_parameter[0]) is expected_value
        else:
            assert test_object.get_random() in expected_value


# Placeholder for running test cases
test_cases = [(["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"],
               [[], [1], [1], [2], [], [1], []],
               [None, True, False, True, {1, 2}, True, {1, 2}]),
              (["RandomizedCollection", "insert", "getRandom", "getRandom", "getRandom", "insert", "insert", "insert",
                "insert", "insert", "getRandom", "getRandom", "insert", "getRandom", "insert", "insert", "getRandom",
                "getRandom", "getRandom", "getRandom", "remove", "insert", "getRandom", "getRandom", "insert", "remove",
                "remove", "insert", "getRandom", "getRandom", "insert", "insert", "getRandom", "remove", "remove",
                "insert", "remove", "getRandom", "getRandom", "remove", "getRandom", "insert", "insert", "getRandom",
                "remove", "remove", "remove", "getRandom", "insert", "insert", "insert", "insert", "getRandom",
                "insert", "getRandom", "remove", "insert", "insert", "insert", "getRandom", "getRandom", "insert",
                "getRandom", "insert", "insert", "getRandom", "getRandom", "remove", "getRandom", "remove", "insert",
                "getRandom", "insert", "insert", "insert", "getRandom", "insert", "insert", "getRandom", "insert",
                "getRandom", "insert", "getRandom", "getRandom", "getRandom", "insert", "getRandom", "getRandom",
                "insert", "insert", "insert", "getRandom", "remove", "insert", "insert", "getRandom", "insert",
                "insert", "insert", "insert"],
               [[], [-7], [], [], [], [6], [7], [10], [3], [8], [], [], [-8], [], [6], [-8], [], [], [], [], [2], [2],
                [], [], [5], [-5], [-8], [-8], [], [], [-4], [10], [], [7], [-1], [8], [-6], [], [], [9], [], [7], [0],
                [], [-10], [-4], [-3], [], [-4], [-5], [8], [-2], [], [-9], [], [7], [-2], [7], [4], [], [], [-6], [],
                [-8], [2], [], [], [9], [], [-1], [3], [], [0], [-3], [-1], [], [-8], [-10], [], [3], [], [4], [], [],
                [], [-10], [], [], [0], [-2], [5], [], [-2], [5], [10], [], [9], [0], [7], [-2]],
               [None, True, {-7}, {-7}, {-7}, True, True, True, True, True, {3, 6, 7, 8, 10, -7}, {3, 6, 7, 8, 10, -7},
                True, {3, 6, 7, 8, 10, -8, -7}, False, False, {3, 6, 7, 8, 10, -8, -7}, {3, 6, 7, 8, 10, -8, -7},
                {3, 6, 7, 8, 10, -8, -7}, {3, 6, 7, 8, 10, -8, -7}, False, True, {2, 3, 6, 7, 8, 10, -8, -7},
                {2, 3, 6, 7, 8, 10, -8, -7}, True, False, True, False, {2, 3, 5, 6, 7, 8, 10, -8, -7},
                {2, 3, 5, 6, 7, 8, 10, -8, -7}, True, False, {2, 3, 5, 6, 7, 8, 10, -8, -7, -4}, True, False, False,
                False, {2, 3, 5, 6, 8, 10, -8, -7, -4}, {2, 3, 5, 6, 8, 10, -8, -7, -4}, False,
                {2, 3, 5, 6, 8, 10, -8, -7, -4}, True, True, {0, 2, 3, 5, 6, 7, 8, 10, -8, -7, -4}, False, True, False,
                {0, 2, 3, 5, 6, 7, 8, 10, -8, -7}, True, True, False, True,
                {0, 2, 3, 5, 6, 7, 8, 10, -8, -7, -5, -4, -2}, True, {0, 2, 3, 5, 6, 7, 8, 10, -9, -8, -7, -5, -4, -2},
                True, False, True, True, {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -5, -4, -2},
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -5, -4, -2}, True,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -6, -5, -4, -2}, False, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -6, -5, -4, -2},
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -6, -5, -4, -2}, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -6, -5, -4, -2}, False, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -9, -8, -7, -6, -5, -4, -2}, False, True, True,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -1, -9, -8, -7, -6, -5, -4, -3, -2}, False, True,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10}, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10}, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10},
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10},
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10}, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10},
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10}, False, False, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10}, True, False, False,
                {0, 2, 3, 4, 5, 6, 7, 8, 10, -2, -9, -8, -7, -6, -5, -4, -3, -1, -10}, True, False, False, False]),
              ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
