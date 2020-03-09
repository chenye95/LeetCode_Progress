"""
On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0]
and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently
landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch
(either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.


Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped,
after dropping squares represented by positions[0], positions[1], ..., positions[i].
"""
from typing import List


def fallingSquares(positions: List[List[int]]) -> List[int]:
    # Block (Square Root) Decomposition
    # RunTime O(N*sqrt(N))
    # Divide coordinates into sqrt(N) groups, each with sqrt(N) coordinates
    # block_lo[i] represents the lowest among the ith group
    # block_hi[i] represents the highest among the ith group
    def tallest_in_range(left: int, right: int):
        tallest = 0
        if left % B and left <= right:
            tallest = max(tallest, blocks_lo[left // B])
            while left % B and left <= right:
                tallest = max(tallest, heights[left])
                left += 1
        if (right + 1) % B and left <= right:
            tallest = max(tallest, blocks_lo[right // B])
            while (right + 1) % B and left <= right:
                tallest = max(tallest, heights[right])
                right -= 1
        while left <= right:
            tallest = max(tallest, blocks_lo[left // B], blocks_hi[left // B])
            left += B
        return tallest

    def update_in_range(left: int, right: int, h: int):
        if left % B:
            blocks_hi[left // B] = max(blocks_hi[left // B], h)
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                left += 1
        if (right + 1) % B:
            blocks_hi[right // B] = max(blocks_hi[right // B], h)
            while right % B != B - 1 and left <= right:
                heights[right] = max(heights[right], h)
                right -= 1
        while left <= right:
            blocks_lo[left // B] = max(blocks_lo[left // B], h)
            left += B

    # Coordinates Compression
    coordinates = set()
    for left, size in positions:
        coordinates.add(left)
        coordinates.add(left + size - 1)
    index = {x: i for i, x in enumerate(sorted(coordinates))}

    W = len(index)
    B = int(W ** .5)
    heights = [0] * W
    blocks_lo = [0] * (B + 2)  # Lowest Height in a Block
    blocks_hi = [0] * (B + 2)  # Tallest Height in a Block

    tallest_so_far = 0
    ans = []
    for left, size in positions:
        L = index[left]
        R = index[left + size - 1]
        h = tallest_in_range(L, R) + size
        update_in_range(L, R, h)
        tallest_so_far = max(tallest_so_far, h)
        ans.append(tallest_so_far)

    return ans


test_cases = [([[1, 2], [2, 3], [6, 1]], [2, 5, 5]),
              ([[100, 100], [200, 100]], [100, 100]),
              ([[7, 1], [3, 3], [7, 5]], [1, 3, 6])]
for input, output in test_cases:
    assert fallingSquares(input) == output

from random import randint
from datetime import datetime, timedelta

total_runs = 1000
cumulative_time = timedelta()
for i in range(total_runs):
    if i % 100 == 0:
        print("Test %d" % i)
    N = randint(1, 1000)
    input = []
    for _ in range(N):
        input.append([randint(1, 10**8), randint(1, 10**6)])
    start_time = datetime.now()
    fallingSquares(input)
    cumulative_time += (datetime.now() - start_time)
print('%d Tests total ' % total_runs, cumulative_time)
