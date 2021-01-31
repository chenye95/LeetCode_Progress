"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode
would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only
finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after
finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to
start the corresponding project. Initially, you have W capital. When you finish a project, you will obtain its pure
profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output
your final maximized capital.
"""
from heapq import heappush, heappop
from typing import List


def find_maximized_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    working_capital = w
    projects = sorted(zip(capital, profits))
    max_profit_doable = []
    unavailable_project = 0

    for _ in range(k):
        while unavailable_project < len(projects) and projects[unavailable_project][0] <= working_capital:
            # as working_capital accumulates, unlock new project opportunities
            heappush(max_profit_doable, -projects[unavailable_project][1])
            unavailable_project += 1
        if max_profit_doable:
            # implement the project that yields the most profit
            working_capital -= heappop(max_profit_doable)
        else:
            break

    return working_capital


assert find_maximized_capital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]) == 4
