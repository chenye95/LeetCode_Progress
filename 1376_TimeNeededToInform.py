"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has is the one
with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th
employee, manager[headID] = -1. Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. He will inform his
direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e After informTime[i] minutes,
 all his direct subordinates can start spreading the news).
"""
from typing import List


def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    def query_by_id(id: int):
        if id == headID:
            time_to_know[id] = 0
        elif time_to_know[id] == -1 and manager[id] != -1:
            time_to_know[id] = query_by_id(manager[id]) + informTime[manager[id]]
        return time_to_know[id]

    time_to_know = [-1] * n
    for i in range(n):
        if time_to_know[i] == -1:
            query_by_id(i)

    return max(time_to_know)


assert numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]) == 1
assert numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]) == 21
assert numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                    informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 3
assert numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]) == 1076
