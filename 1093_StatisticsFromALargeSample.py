"""
We sampled integers between 0 and 255, and stored the results in an array count:  count[k] is the number of integers we
sampled equal to k.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating point numbers.
The mode is guaranteed to be unique.

(Recall that the median of a sample is:
- The middle element, if the elements of the sample were sorted and the number of elements is odd;
- The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.)
"""
from bisect import bisect
from cmath import isclose
from typing import List

N = 256


def sampleStats(count: List[int]) -> List[float]:
    """
    :param count: list of length N, where count[i] is the number of occurrence for integer i
    :return: [sample_min, sample_max, sample_median, sample_mode]
    """
    total_count = sum(count)
    # sample_min: first integer for which count[i] is non-zero
    sample_min = next(i for i in range(N) if count[i]) * 1.0
    # sample_max: last integer for which count[i] is non-zero
    sample_max = next(i for i in range(N - 1, -1, -1) if count[i]) * 1.0
    # sample_mean: weighted average of i * c_i
    sample_mean = sum(i * c_i for i, c_i in enumerate(count)) * 1.0 / total_count
    # sample_mode: integer with largest c_i
    sample_mode = count.index(max(count)) * 1.0

    # Accumulate count
    for i in range(N - 1):
        count[i + 1] += count[i]
    if total_count % 2 == 0:
        sample_median1 = bisect(count, (total_count - 1) // 2)
        sample_median2 = bisect(count, total_count // 2)
        sample_median = (sample_median1 + sample_median2) / 2.0
    else:
        sample_median = float(bisect(count, (total_count - 1) // 2))
    return [sample_min, sample_max, sample_mean, sample_median, sample_mode]


test_cases = [([1.00000, 3.00000, 2.37500, 2.50000, 3.00000],
               [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
              ([1.00000, 4.00000, 2.18182, 2.00000, 1.00000],
               [0, 4, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
              ]

for i, (expected_output, input) in enumerate(test_cases):
    get_output = sampleStats(input)
    assert all([isclose(expected_output[j], get_output[j], rel_tol=0.0001) for j in range(4)]), i
