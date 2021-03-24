"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] +
arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10**9 + 7.
"""
from collections import Counter
from typing import List


def three_sum_multiplicity_counter(array: List[int], target: int) -> int:
    _mod_value = 10 ** 9 + 7
    count = Counter(array)
    keys = sorted(count.keys())

    ans_count = 0
    # find keys[i] + keys[j] + keys[k] == target such that i <= j <= k
    for i, x in enumerate(keys):
        y_plus_z_target = target - x
        j, k = i, len(keys) - 1
        while j <= k:
            y, z = keys[j], keys[k]
            if y + z < y_plus_z_target:
                j += 1
            elif y + z > y_plus_z_target:
                k -= 1
            else:
                # calculate the count of the (keys[i], keys[j], keys[k]) pair
                if i < j < k:
                    ans_count += (count[x] * count[y] * count[z]) % _mod_value
                elif i == j < k:
                    ans_count += (count[x] * (count[x] - 1) / 2 * count[z]) % _mod_value
                elif i < j == k:
                    ans_count += (count[x] * count[y] * (count[y] - 1) / 2) % _mod_value
                else:  # i == j == k
                    ans_count += (count[x] * (count[x] - 1) * (count[x] - 2) / 6) % _mod_value
                j += 1
                k -= 1

    return int(ans_count % _mod_value)


def three_sum_multiplicity_value(array: List[int], target: int) -> int:
    """
    3 <= arr.length <= 3000
    0 <= arr[i] <= 100
    0 <= target <= 300
    """
    _val_lower, _val_upper = 0, 100
    _mod_value = 10 ** 9 + 7
    count = Counter(array)

    ans_count = 0

    # x < y < z
    for x in range(_val_lower, _val_upper + 1):
        for y in range(x + 1, _val_upper + 1):
            z = target - x - y
            if y < z <= _val_upper:
                ans_count += (count[x] * count[y] * count[z]) % _mod_value

    # x == y
    for x in range(_val_lower, _val_upper + 1):
        z = target - 2 * x
        if x < z <= _val_upper:
            ans_count += (count[x] * (count[x] - 1) / 2 * count[z]) % _mod_value

    # y == z
    for x in range(_val_lower, _val_upper + 1):
        if (target - x) % 2 == 0:
            y = (target - x) / 2
            if x < y <= _val_upper:
                ans_count += (count[x] * count[y] * (count[y] - 1) / 2) % _mod_value

    # x == y == z
    if target % 3 == 0:
        x = target / 3
        if _val_lower <= x <= _val_upper:
            ans_count += (count[x] * (count[x] - 1) * (count[x] - 2) / 6) % _mod_value

    return int(ans_count % _mod_value)


test_cases = [([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20),
              ([1, 1, 2, 2, 2, 2], 5, 12), ]
for three_sum_multiplicity in [three_sum_multiplicity_value, three_sum_multiplicity_counter]:
    for test_array, test_target, expected_output in test_cases:
        assert three_sum_multiplicity(test_array, test_target) == expected_output, three_sum_multiplicity.__name__
