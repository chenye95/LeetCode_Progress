"""
On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0]
and side length positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently
landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch
(either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.


Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped,
after dropping squares represented by positions[0], positions[1], ..., positions[i].
"""
from datetime import datetime, timedelta
from random import randint
from typing import List, Tuple

from _Range_Query import LazyQueryRange


def falling_squares_two(positions: List[Tuple[int, int]]) -> List[int]:
    """
    :param positions: list of (left_point, side_length) represents the list of square block that drop from the sky
    :return: list of tallest point after dropping each block
    """
    # Lazy Range Query Approach

    # Coordinates Compression
    coordinates = set()
    for left, size in positions:
        coordinates.add(left)
        coordinates.add(left + size - 1)
    index = {x: i for i, x in enumerate(sorted(coordinates))}

    tallest_range_query = LazyQueryRange([0] * len(index), merge_function=max,
                                         range_update_function=lambda old_value, lo, hi, new_value: new_value)

    ans = []
    tallest_so_far = 0
    for left, size in positions:
        L = index[left]
        R = index[left + size - 1]
        current_range_tallest = tallest_range_query.query_segment_tree(L, R)
        tallest_range_query.range_update(L, R, size + current_range_tallest)
        tallest_so_far = max(tallest_so_far, size + current_range_tallest)
        ans.append(tallest_so_far)

    return ans


test_cases = [([(1, 2), (2, 3), (6, 1)], [2, 5, 5]),
              ([(100, 100), (200, 100)], [100, 100]),
              ([(7, 1), (3, 3), (7, 5)], [1, 3, 6]), ]
for test_input, expected_output in test_cases:
    assert falling_squares_two(test_input) == expected_output

total_runs = 1000
cumulative_time = timedelta()
for i in range(total_runs):
    if i % 100 == 0:
        print("Test %d" % i)
    N = randint(1, 1000)
    test_input = []
    for _ in range(N):
        test_input.append((randint(1, 10 ** 8), randint(1, 10 ** 6)))
    start_time = datetime.now()
    falling_squares_two(test_input)
    cumulative_time += (datetime.now() - start_time)
print('%d Tests total ' % total_runs, cumulative_time)
