"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter
represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit
of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter
in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.
"""
from collections import Counter
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    """
    :param tasks: list of tasks to be scheduled on CPU, each task is represented by a capital letter A ... Z
    :param n: at least n units of cool down period apart between two tasks of the same letter
    :return: least CPU time needed to finish all given tasks
    """
    # find the most repetitive tasks and arrange them first
    count_by_task = list(Counter(tasks).values())
    most_repetition = max(count_by_task)
    top_contender = count_by_task.count(most_repetition)
    # if top_contender <= n + 1, arrange the top contenders in group and ensure n units apart;
    # - if gap > len(remainder), fill in the gaps with remainder, len: (most_repetition - 1) * (n + 1) + top_contender
    # - if gap <= len(remainder), extend out to len(tasks)
    # if top_contender > n + 1, arrange the top contenders in group
    # - append the remainder to the end, or insert in between groups
    # - total length, len(tasks)
    return max(len(tasks), (most_repetition - 1) * (n + 1) + top_contender)


assert least_interval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
assert least_interval(tasks=["A", "A", "A", "B", "B", "B"], n=0) == 6
assert least_interval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2) == 16
