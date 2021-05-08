from typing import List


def sub_array_divisible_by(nums: List[int], k: int) -> int:
    """
    :param nums: array of  integers
    :param k: target to sum up to
    :return: number of pairs (i, j) such that sum(nums[i:j]) % k == 0
    """
    # compute sum(nums[:i]) and count number of times sum(nums[:i]) % k appears
    remainder_count = [1] + [0] * (k - 1)
    accumulator = 0
    return_count = 0
    for num_i in nums:
        accumulator += num_i
        # note when sum(nums[i+1:j]) % k == 0
        # (sum(nums[:j]) - sum(nums[:i])) % k == 0
        # i.e. sum(nums[:i]) % k == sum(nums[:j]) % k
        return_count += remainder_count[accumulator % k]
        remainder_count[accumulator % k] += 1
    return return_count


test_cases = [([4, 5, 0, -2, -3, 1], 5, 7),
              ([-499, 194, -115, -651, -57, -180, 138, 17, -377, -286, 676, -498, 121, -976, 483], 343, 0),
              ([7, -5, 5, -8, -6, 6, -4, 7, -8, -7], 7, 11), ]
for test_nums, test_k, expected_output in test_cases:
    assert sub_array_divisible_by(test_nums, test_k) == expected_output
