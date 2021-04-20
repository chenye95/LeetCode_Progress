"""
The XOR sum of a list is the bitwise XOR of all its elements. If the list only contains one element, then its XOR sum
 will be equal to this element. For example, the XOR sum of [1,2,3,4] is equal to 1 XOR 2 XOR 3 XOR 4 = 4, and the XOR
 sum of [3] is equal to 3.

You are given two 0-indexed arrays arr1 and arr2 that consist only of non-negative integers.

Consider the list containing the result of arr1[i] AND arr2[j] (bitwise AND) for every (i, j) pair where 0 <= i <
 arr1.length and 0 <= j < arr2.length.

Return the XOR sum of the aforementioned list.
"""
from functools import reduce
from operator import xor
from typing import List


def get_xor_sum(arr1: List[int], arr2: List[int]) -> int:
    """
    Notice (a1&b1) ^ (a1&b2) ^ (a2&b1) ^ (a2&b2) = (a1^a2) & (b1^b2)

    :param arr1: array of non-negative integers
    :param arr2: array of non-negative integers
    :return: xor sum of bitwise and over pairs arr1[i] & arr2[j]
    """
    return reduce(xor, arr1) & reduce(xor, arr2)


test_cases = [([1, 2, 3], [6, 5], 0),
              ([12], [4], 4),
              ([9624, 6193, 1255, 9351, 9015, 3665, 9272, 1339, 4370, 5978, 4842, 9247, 8753, 1872, 7500, 4541, 1765,
                749, 4845, 202, 238, 1502, 6775, 1885, 655, 3078, 3926, 9614, 6897, 2654, 1893, 7387, 2742, 3955, 2604,
                1684, 7128, 6197, 8895, 4817, 9014, 4151, 7815, 5152, 1640, 3401, 5200, 649, 446, 172, 4842, 9774, 5246,
                7370, 6410, 5132, 6529, 1031, 1051, 5199, 9854, 7468, 1824, 4097, 3525, 8895, 7682, 5829, 4244, 3001,
                8873, 3405, 5035, 3263, 4036, 5905, 1333, 4600, 1464],
               [7338, 1482, 9410, 5552, 3726, 6397, 5026, 672, 5361, 3060, 5189, 9486, 4961, 4027, 5477, 1653, 8916,
                9486, 9764, 1508, 4015, 3607, 333, 3993, 6582, 1185, 4391, 9030, 1161, 1230, 352, 162, 4764, 5884, 8081,
                7681, 2526, 1653, 8215, 5375, 1263, 8343, 2838, 2942, 2450, 2318, 5239, 5007, 1751, 8427, 9861, 4808,
                2069, 3387, 2321, 8937, 520, 5178, 9059, 3365, 2918, 4897, 7088, 8806, 2586, 795, 4051, 4138, 1055,
                7318, 7047, 8999, 4099, 8869, 7199, 8815, 7427, 178, 6483, 5548, 2810, 4226, 7959, 399, 6826, 9348, 309,
                1021, 5815, 9503, 2265, 9724, 2050, 2269, 4245, 4536, 6517], 8704), ]
for test_arr1, test_arr2, expected_output in test_cases:
    assert get_xor_sum(test_arr1, test_arr2) == expected_output
