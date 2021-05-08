"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively.
 All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At
 each step:

- If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the
 queue.
- Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith sandwich in the
 stack (i = 0 is the top of the stack) and students[j] is the preference of the jth student in the initial queue (j = 0
 is the front of the queue). Return the number of students that are unable to eat.
"""
from collections import Counter
from typing import List


def count_students(students: List[int], sandwiches: List[int]) -> int:
    """
    :param students: list of 0s and 1s, representing preference of sandwiches for each student in the list
    :param sandwiches: list of 0s and 1s, representing types of sandwiches in the pile
    :return: number of students that cannot eat
    """
    student_type_count = Counter(students)
    sandwich_i = 0

    while sandwich_i < len(sandwiches) and student_type_count[sandwiches[sandwich_i]]:
        # processing sandwich_i
        # if any student left still prefers sandwiches[sandwich_i], it will be removed from the pile at some point,
        # or otherwise, the queue will be stuck
        student_type_count[sandwiches[sandwich_i]] -= 1
        sandwich_i += 1

    return len(students) - sandwich_i


test_cases = [([1, 1, 0, 0], [0, 1, 0, 1], 0),
              ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
              ([0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 5),
              ([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0], 5), ]
for test_students, test_sandwiches, expected_output in test_cases:
    assert count_students(test_students, test_sandwiches) == expected_output
