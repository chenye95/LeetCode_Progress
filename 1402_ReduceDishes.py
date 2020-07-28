"""
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by
its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
"""
from typing import List


def max_satisfaction(satisfaction: List[int]) -> int:
    """
    Observation 1: finish dishes, if chosen to cook, in ascending order of satisfaction
    Observation 2: only cook a dish if it increases like-time coefficient
    Observation 3: adding dish i to the list add cumulative satisfaction level of all chosen dishes + satisfaction[i]
    :param satisfaction: satisfaction level for n dishes
    :return: like-time coefficient for finished dishes
    """
    max_like_time = chosen_dishes_cumulative_satisfaction = 0
    satisfaction.sort()
    i = len(satisfaction) - 1
    while i >= 0 and satisfaction[i] + chosen_dishes_cumulative_satisfaction > 0:
        chosen_dishes_cumulative_satisfaction += satisfaction[i]
        max_like_time += chosen_dishes_cumulative_satisfaction
        i -= 1
    return max_like_time


assert max_satisfaction(satisfaction=[-1, -8, 0, 5, -9]) == 14
assert max_satisfaction(satisfaction=[4, 3, 2]) == 20
assert max_satisfaction(satisfaction=[-1, -4, -5]) == 0
assert max_satisfaction(satisfaction=[-2, 5, -1, 0, 3, -3]) == 35
