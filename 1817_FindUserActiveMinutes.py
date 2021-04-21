"""
You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array
 logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an
 action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of
 users whose UAM equals j.

Return the array answer as described above.
"""
from collections import defaultdict
from typing import List, Tuple


def find_user_active_minutes(logs: List[Tuple[int, int]], k: int) -> List[int]:
    """
    :param logs: list of [user_i, time_i] representing user_i is active at time_i
    :param k: k >= maximum User Active Minutes among all users
    :return: 1-indexed list such that return_list[(t - 1)] = number of users whose User Active Minute is t
    """
    active_min_by_person = defaultdict(set)
    for person_i, t_i in logs:
        active_min_by_person[person_i].add(t_i)

    return_list = [0] * k
    for person_i in active_min_by_person:
        # k >= maximum User Active Minutes among all users
        return_list[len(active_min_by_person[person_i]) - 1] += 1

    return return_list


test_cases = [([(0, 5), (1, 2), (0, 2), (0, 5), (1, 3)], 5, [0, 2, 0, 0, 0]),
              ([(1, 1), (2, 2), (2, 3)], 4, [1, 1, 0, 0]), ]
for test_logs, test_k, expected_output in test_cases:
    assert find_user_active_minutes(test_logs, test_k) == expected_output
