"""
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] =
 [enqueueTimei, processingTimei] means that the i task will be available to process at enqueueTimei and will take
 processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
- If the CPU is idle and there are no available tasks to process, the CPU remains idle.
- If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If
 multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
- Once a task is started, the CPU will process the entire task without stopping.
- The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks
"""
from heapq import heappush, heappop
from typing import List, Tuple


def get_order(tasks: List[Tuple[int, int]]) -> List[int]:
    """
    :param tasks: list of n tasks [(enqueue_time_i, processing_time_i)]
    :return: order the CPU will process the tasks
    """
    tasks = sorted((task_info[0], task_info[1], task_i) for task_i, task_info in enumerate(tasks))
    i = 0
    current_time = 0
    eligible_tasks = []
    process_order = []
    while i < len(tasks) or eligible_tasks:
        if not eligible_tasks:
            enqueue_time_i, processing_time_i, task_i = tasks[i]
            current_time = enqueue_time_i + processing_time_i
            process_order.append(task_i)
            i += 1
        else:
            task_j_time, task_j = heappop(eligible_tasks)
            current_time += task_j_time
            process_order.append(task_j)
        while i < len(tasks) and tasks[i][0] <= current_time:
            heappush(eligible_tasks, (tasks[i][1], tasks[i][2]))
            i += 1

    return process_order


test_cases = [([(1, 2), (2, 4), (3, 2), (4, 1)], [0, 2, 3, 1]),
              ([(7, 10), (7, 12), (7, 5), (7, 4), (7, 2)], [4, 3, 2, 0, 1]),
              ([(19, 17), (35, 12), (44, 45), (34, 25), (2, 12), (34, 41), (49, 27), (11, 26), (45, 38), (37, 43),
                (45, 21), (41, 45), (22, 11), (4, 7), (8, 33), (17, 37), (8, 9), (44, 48), (38, 2), (27, 23)],
               [4, 13, 16, 12, 18, 1, 0, 10, 19, 3, 7, 6, 14, 15, 8, 5, 9, 2, 11, 17])]
for test_tasks, expected_order in test_cases:
    assert get_order(test_tasks) == expected_order
