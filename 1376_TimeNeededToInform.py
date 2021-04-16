"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has is the one
with head_id.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th
employee, manager[head_id] = -1. Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. He will inform his
direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.

The i-th employee needs inform_time[i] minutes to inform all of his direct subordinates (i.e After inform_time[i] minutes,
 all his direct subordinates can start spreading the news).
"""
from typing import List


def num_of_minutes(n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
    """
    :param n: total number of employees in the company
    :param head_id: customer_id for head of the company
    :param manager: tree structures such that employee i reports to manager[i]; manager[head_id] = -1
    :param inform_time: time for a manager to inform all his direct reports
    :return: total time to inform all employees
    """

    def query_by_employee_id(employee_id: int) -> int:
        """
        :return: amount of time elapsed until employee_id is informed
        """
        if employee_id == head_id:
            time_to_know[employee_id] = 0
        elif time_to_know[employee_id] == -1:
            time_to_know[employee_id] = query_by_employee_id(manager[employee_id]) + inform_time[manager[employee_id]]
        return time_to_know[employee_id]

    time_to_know = [-1] * n
    for i in range(n):
        if time_to_know[i] == -1:
            query_by_employee_id(i)

    return max(time_to_know)


test_cases = [(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0], 1),
              (7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1], 21),
              (15, 0, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 3),
              (4, 2, [3, 3, -1, 2], [0, 0, 162, 914], 1076), ]
for test_n, test_head_id, test_managers, test_inform_time, expected_output in test_cases:
    assert num_of_minutes(test_n, test_head_id, test_managers, test_inform_time) == expected_output
