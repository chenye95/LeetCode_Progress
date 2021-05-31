"""
You are given two integer arrays nums1 and nums2 of length n.

The XOR sum of the two integer arrays is
- (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).
- For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.

Rearrange the elements of nums2 such that the resulting XOR sum is minimized.

Return the XOR sum after the rearrangement.
"""
from functools import cache
from typing import List


def min_xor_sum(nums_1: List[int], nums_2: List[int]) -> int:
    """
    :param nums_1: 1 <= len(nums_1) <= 14 and 0 <= nums_1[i] <= 10**7
    :param nums_2: len(nums_2) == len(nums_1) <= 14 and 0 <= nums_2[i] <= 10**7
    :return: minimum sum xor of permutation of nums_1 and permutation of nums_2
    """

    # fix nums_1 and try to match with permutation of nums_2
    n = len(nums_1)
    if n == 1:
        return nums_1[0] ^ nums_2[0]

    @cache
    def match_i(i: int, used_nums_2_mask: int) -> int:
        """
        :param i: matching position i
        :param used_nums_2_mask: binary mask to represents which integers n nums_2 have been used
        :return: min xor sum for nums_1[i:]
        """
        if i == n:
            return 0

        nums_1_i = nums_1[i]

        return min((nums_1_i ^ nums_2[j]) + match_i(i + 1, used_nums_2_mask + (1 << j))
                   for j in range(n) if not (used_nums_2_mask & (1 << j)))

    return match_i(0, 0)


test_cases = [([0], [2877579], 2877579),
              ([1, 2], [2, 3], 2),
              ([1, 0, 3], [5, 3, 4], 8),
              ([70, 29, 44, 29, 86, 28, 97, 58, 37, 2], [53, 71, 82, 12, 23, 80, 92, 37, 15, 95], 254),
              ([2486049, 4395362, 7707310, 8834753, 2726898, 2325653, 2316899, 7393406, 6058081, 5196941, 6723570,
                4034813, 1943421, 3459280],
               [5125370, 1144646, 1784851, 3818824, 6660686, 5391696, 8260455, 1677288, 3133334, 754650, 928502, 390631,
                3633236, 582394],
               31083367),
              ([65022, 4657711, 8572489, 3336640, 7744043, 8672352, 6861299, 5122697, 2857375, 7539481, 8907966,
                3311170],
               [6030101, 8828015, 59043, 6529065, 9719816, 7144904, 6799001, 5637315, 9805075, 1136584, 8266168,
                4154565],
               15088819),
              ([9606269, 5221932, 7334481, 8439484, 5986425, 8864979, 5430580, 14172, 2078710, 7420803, 7542233],
               [5875595, 5113681, 9047874, 6700866, 5693602, 9586753, 8259408, 1897425, 6334375, 6415366, 3421110],
               22257895),
              ([100, 26, 12, 62, 3, 49, 55, 77, 97], [98, 0, 89, 57, 34, 92, 29, 75, 13], 200),
              ]
for test_nums_1, test_nums_2, expected_value in test_cases:
    assert min_xor_sum(test_nums_1, test_nums_2) == expected_value, expected_value
