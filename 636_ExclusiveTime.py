"""
On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means
the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end
 of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any
recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.
"""
from typing import List


def exclusive_time(n: int, logs: List[str]) -> List[int]:
    """
    :param n: n unique process with process_id between 0 and n-1
    :param logs: list of entries of format process_id:operation:timestamp, operation can either be start or end
    :return:
    """
    tracker = [0] * (n + 1)
    stack = []
    current_process_id = -1
    for entry in logs:
        process_id, operation, timestamp = entry.split(':')
        next_process_id, int_timestamp = int(process_id), int(timestamp)
        if operation == "start":
            # Hold current process
            # Append to stack for tracking
            tracker[current_process_id] += int_timestamp
            stack.append(current_process_id)
            # Start next process
            tracker[next_process_id] -= int_timestamp
            current_process_id = next_process_id
        elif operation == "end":
            # End current process
            # Process ends at end of timestamp period
            int_timestamp += 1
            tracker[next_process_id] += int_timestamp
            # Retrieve last process from the stack
            # Restart the process
            current_process_id = stack.pop()
            tracker[current_process_id] -= int_timestamp
    return tracker[:n]


assert exclusive_time(n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]) == [3, 4]
