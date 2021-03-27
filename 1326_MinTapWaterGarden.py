"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The
length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water
the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return
-1.
"""
from typing import List


def min_tap_water_garden(n: int, ranges: List[int]) -> int:
    """
    Similar to 1024 Video Stitching

    :param n: garden covers [0, n]
    :param ranges: ith tap covers [i-range[i], i+range[i]] for i in [0,...N]
    :return: min number of taps to be open to water the whole garden
    """
    # compute tap coverage, disregard all coverage left of origin (not inside the garden)
    # ensure coverage length is greater than 0
    tap_coverage = [(max(0, i - range_i), i + range_i) for i, range_i in enumerate(ranges) if range_i > 0]
    cover_without_last_tap, farthest_all_taps, min_count = -1, 0, 0

    # Greedy algorithm: at every step takes the tap that extends the range farthest
    # sort taps by coverage_start, and then coverage_end
    # i.e. order taps with same coverage_start by coverage length
    for coverage_start, coverage_end in sorted(tap_coverage):
        if farthest_all_taps >= n or coverage_start > farthest_all_taps:
            # have covered [0, n] or a gap cannot be filled by any clip
            break
        elif cover_without_last_tap < coverage_start:
            # - else statement guarantees  coverage_start <= farthest_all_taps
            # - cover_without_last_tap < coverage_start means this is the first clip that doesn't cover
            # [cover_without_last_tap, coverage_start - 1], cannot be used for previous round last clip
            # - greedily takes in any clip that can extends stitch length
            # - replace with longer tap_coverage in next iterations
            min_count, cover_without_last_tap = min_count + 1, farthest_all_taps
        # else:
        # replace last clip with longer tap_coverage
        # maintain cover_without_last_tap, and extend farthest_all_taps

        farthest_all_taps = max(farthest_all_taps, coverage_end)

    return min_count if farthest_all_taps >= n else -1


test_cases = ([(5, [3, 4, 1, 1, 0, 0], 1),
               (3, [0, 0, 0, 0], -1),
               (7, [1, 2, 1, 0, 2, 1, 0, 1], 3),
               (8, [4, 0, 0, 0, 0, 0, 0, 0, 4], 2),
               (8, [4, 0, 0, 0, 4, 0, 0, 0, 4], 1), ])
for test_n, test_ranges, expected_output in test_cases:
    assert min_tap_water_garden(n=test_n, ranges=test_ranges) == expected_output
