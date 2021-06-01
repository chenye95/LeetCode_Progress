"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [A_i, B_i]
 and values[i] represent the equation A_i / B_i = values[i]. Each A_i or B_i is a string that represents a single
 variable.

You are also given some queries, where queries[j] = [C_j, D_j] represents the jth query where you must find the answer
 for C_j / D_j = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that
 there is no contradiction.
"""
from collections import defaultdict
from typing import List, Tuple


def calculate_division(equations: List[Tuple[str, str]], values: List[float],
                       queries: List[Tuple[str, str]]) -> List[float]:
    """
    :param equations: 1 <= len(equations) <= 20, a list of (a_i, b_i)
    :param values: len(values) == len(equations), such that a_i / b_i == value_i
    :param queries: 1 <= len(queries) <= 20, list of (c_j, d_j)
    :return: list of c_j / d_j if it can be determined or -1
    """

    def evaluate_query(variable_x_y: Tuple[str, str]) -> float:
        """
        BFS algorithm to compute variable_x / variable_y

        :param variable_x_y: (variable_x, variable_y)
        :return: variable_x / variable_y if can be determined else -1.
        """
        variable_x, variable_y = variable_x_y
        if variable_x not in evaluation_map or variable_y not in evaluation_map:
            return -1.
        elif variable_x == variable_y:
            return 1.
        elif variable_y in evaluation_map[variable_x]:
            return evaluation_map[variable_x][variable_y]

        visiting_queue = [(variable_x, 1.0), ]
        visited = {variable_x, }
        while visiting_queue:
            current_variable, current_product = visiting_queue.pop(0)
            for next_variable, next_product in evaluation_map[current_variable].items():
                if next_variable == variable_y:
                    return current_product * next_product
                if next_variable not in visited:
                    visiting_queue.append((next_variable, current_product * next_product))
                    visited.add(next_variable)

        return -1.

    evaluation_map = defaultdict(dict)
    for (numerator, denominator), result in zip(equations, values):
        evaluation_map[numerator][denominator] = result
        evaluation_map[denominator][numerator] = 1.0 / result
    return list(map(evaluate_query, queries))


test_cases = [([("a", "b"), ("b", "c")],
               [2, 3],
               [("a", "c"), ("b", "a"), ("a", "e"), ("a", "a"), ("x", "x")],
               [6, .5, -1, 1, -1]),
              ([("a", "c"), ("b", "e"), ("c", "d"), ("e", "d")],
               [2, 3, .5, 5],
               [("a", "b")],
               [2. / 30]),
              ([("a", "b"), ("b", "c"), ("bc", "cd")],
               [1.5, 2.5, 5],
               [("a", "c"), ("c", "b"), ("bc", "cd"), ("cd", "bc")],
               [3.75, 0.4, 5., 0.2]),
              ([("a", "b")],
               [.5],
               [("a", "b"), ("b", "a"), ("a", "c"), ("x", "y")],
               [.5, 2, -1, -1]),
              ([("a", "b"), ("b", "c"), ("a", "c"), ("d", "e")],
               [2, 3, 6, 1],
               [("a", "c"), ("b", "c"), ("a", "e"), ("a", "a"), ("x", "x"), ("a", "d")],
               [6, 3, -1, 1, -1, -1]),
              ([("a", "b"), ("a", "c"), ("a", "d"), ("a", "e"), ("a", "f"), ("a", "g"), ("a", "h"), ("a", "i"),
                ("a", "j"), ("a", "k"), ("a", "l"), ("a", "aa"), ("a", "aaa"), ("a", "aaaa"), ("a", "aaaaa"),
                ("a", "bb"), ("a", "bbb"), ("a", "ff")],
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 1, 1, 1, 1, 3, 5],
               [("d", "f"), ("e", "g"), ("e", "k"), ("h", "a"), ("aaa", "k"), ("aaa", "i"), ("aa", "e"), ("aaa", "aa"),
                ("aaa", "ff"), ("bbb", "bb"), ("bb", "h"), ("bb", "i"), ("bb", "k"), ("aaa", "k"), ("k", "l"),
                ("x", "k"), ("l", "ll")],
               [5. / 3, 1.5, 2.5, 1. / 7, 10, 8, 4, 1, 5, 1. / 3, 7, 8, 10, 10, 1.1, -1, -1],),
              ]
for test_equations, test_values, test_queries, expected_values in test_cases:
    get_result = calculate_division(test_equations, test_values, test_queries)
    for get_i, expected_i in zip(get_result, expected_values):
        assert abs(get_i - expected_i) < .05, (get_i, expected_i)
