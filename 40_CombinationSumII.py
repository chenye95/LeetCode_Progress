"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
from typing import List


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Backtrack to generate all possible combinations

    :param candidates: list of integers may contain duplicates
    :param target: integer target number
    :return: all unique combinations in candidates that sum to target, and each item in candidates is used at most once
    """

    def back_track(combination: List[int], remainder: int, start_from: int, ref_results: List[List[int]]) -> None:
        if remainder == 0:
            # make a deep copy of the combination .append(list())
            ref_results.append(list(combination))
            return

        for next_pick in range(start_from, len(candidates)):
            if next_pick > start_from and candidates[next_pick] == candidates[next_pick - 1]:
                # avoid back_tracking from duplicated values
                continue

            if candidates[next_pick] > remainder:
                # since candidates are sorted, we can prune the back_tracking here
                break

            combination.append(candidates[next_pick])
            back_track(combination, remainder - candidates[next_pick], next_pick + 1, ref_results)
            combination.pop()

    candidates.sort()
    combination_tracker, result_list = [], []
    back_track(combination_tracker, target, 0, result_list)

    return result_list


test_cases = [([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
              ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]), ]
for test_candidates, test_target, expected_output in test_cases:
    assert sorted(combination_sum_2(candidates=test_candidates, target=test_target)) == sorted(expected_output)
