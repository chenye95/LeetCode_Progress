"""
You are given a data structure of employee information, which includes the employee's unique employee_id, their importance value
 and their direct subordinates' employee_id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance
 value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has
 [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the
 relationship is not direct.

Now given the employee information of a company, and an employee employee_id, you need to return the total importance value of
 this employee and all their subordinates.
"""
from typing import List


class Employee:
    def __init__(self, employee_id: int, importance: int, subordinates: List[int]):
        """
        :param employee_id: unique id of the employee
        :param importance: importance value of the employee themselves
        :param subordinates: list of employee ids for direct subordinates of the current employee
        """
        self.id = employee_id
        self.importance = importance
        self.subordinates = subordinates


def get_importance(employees: List[Employee], employee_id: int) -> int:
    """
    :param employees: org chart of the company:
        - One employee has at most one direct leader and may have several subordinates.
        - The maximum number of employees won't exceed 2000.
    :param employee_id: a person in the organization.
    :return: importance of employee_id and his org
    """
    employee_id_lookup = {person.id: person for person in employees}

    org_chart = [employee_id]
    org_importance = 0
    while org_chart:
        current_employee = employee_id_lookup[org_chart.pop()]
        org_importance += current_employee.importance
        org_chart.extend(current_employee.subordinates)

    return org_importance


test_cases = [([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1, 11),
              ([[1, 84, [2, 3]], [2, 86, []], [3, 84, [4]], [4, 81, [5, 8]], [5, 92, [6]], [6, 92, [7]], [7, 61, []],
                [8, 70, [9, 50]], [9, 98, [10]], [10, 93, [11, 13]], [11, 60, [12]], [12, 85, []], [13, 86, [14, 15]],
                [14, 73, []], [15, 68, [16]], [16, 59, [17, 18]], [17, 85, []], [18, 57, [19, 45]], [19, 71, [20, 24]],
                [20, 71, [21, 22]], [21, 77, []], [22, 87, [23]], [23, 57, []], [24, 64, [25, 44]], [25, 87, [26, 43]],
                [26, 89, [27]], [27, 70, [28, 33]], [28, 53, [29, 30]], [29, 55, []], [30, 96, [31]], [31, 71, [32]],
                [32, 77, []], [33, 94, [34, 36]], [34, 57, [35]], [35, 58, []], [36, 63, [37]], [37, 87, [38, 42]],
                [38, 59, [39]], [39, 79, [40]], [40, 60, [41]], [41, 68, []], [42, 66, []], [43, 83, []], [44, 51, []],
                [45, 91, [46, 49]], [46, 50, [47, 48]], [47, 70, []], [48, 78, []], [49, 52, []], [50, 90, [51, 52]],
                [51, 90, []], [52, 67, [53]], [53, 96, []]], 47, 70),
              ([[1, 81, [2, 5]], [2, 58, [3]], [3, 89, [4]], [4, 68, []], [5, 79, []]], 2, 215), ]
for test_employee_list, test_id, expected_value in test_cases:
    test_employees = [Employee(current_id, current_importance, current_subordinates)
                      for current_id, current_importance, current_subordinates in test_employee_list]
    assert get_importance(test_employees, test_id) == expected_value
