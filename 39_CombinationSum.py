"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
 of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the
given input.
"""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    :param candidates: array of distinct positive integers 1 <= candidates[i] <= 200
    :param target: integer value
    :return: list of all unique combinations of candidates that add to target
    """

    def back_track(combination: List[int], remainder: int, start_from: int, ref_return_list) -> None:
        if remainder == 0:
            ref_return_list.append(list(combination))

        for next_pick in range(start_from, len(candidates)):
            if candidates[next_pick] > remainder:
                # since candidates is sorted, prune back_track here
                break

            combination.append(candidates[next_pick])
            back_track(combination, remainder - candidates[next_pick], next_pick, ref_return_list)
            combination.pop()

    candidates.sort()
    combination_tracker, return_list = [], []
    back_track(combination_tracker, target, 0, return_list)
    return return_list


test_cases = [([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
              ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
              ([2], 1, []),
              ([1], 1, [[1]]),
              ([1], 2, [[1, 1]]),
              ([2, 7, 6, 3, 5, 1], 9, [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 3],
                                       [1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 2, 3], [1, 1, 1, 1, 5], [1, 1, 1, 2, 2, 2],
                                       [1, 1, 1, 3, 3], [1, 1, 1, 6], [1, 1, 2, 2, 3], [1, 1, 2, 5], [1, 1, 7],
                                       [1, 2, 2, 2, 2], [1, 2, 3, 3], [1, 2, 6], [1, 3, 5], [2, 2, 2, 3], [2, 2, 5],
                                       [2, 7], [3, 3, 3], [3, 6]]), ]
for test_candidates, test_target, expected_output in test_cases:
    assert sorted(combination_sum(candidates=test_candidates, target=test_target)) == sorted(expected_output)
