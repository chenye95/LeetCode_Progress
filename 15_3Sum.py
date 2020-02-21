from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    less_than_target = {}
    more_than_target = {}
    zero_count = 0

    return_set = set()
    for num in nums:
        if num < 0:
            less_than_target[num] = less_than_target.get(num, 0) + 1
        elif num > 0:
            more_than_target[num] = more_than_target.get(num, 0) + 1
        else:
            zero_count += 1

    for num_i in set(nums):
        if num_i < 0:
            for num_j in more_than_target:
                num_k = -num_i - num_j
                if num_k in more_than_target and (num_k != num_j or more_than_target[num_j] >= 2):
                    return_set.add(tuple(sorted((num_i, num_j, num_k))))
                #elif num_k in less_than_target and (num_k != num_i or less_than_target[num_i] >= 2):
                #    return_set.add(tuple(sorted((num_i, num_j, num_k))))
                #    Covered when num_i > 0
                elif num_k == 0 and zero_count > 0:
                    return_set.add(tuple(sorted((num_i, num_j, 0))))
        elif num_i > 0:
            for num_j in less_than_target:
                num_k = -num_i - num_j
                if num_k in less_than_target and (num_k != num_j or less_than_target[num_j] >= 2):
                    return_set.add(tuple(sorted((num_i, num_j, num_k))))
                # elif num_k in more_than_target and (num_k != num_i or more_than_target[num_i] >= 2):
                #     return_set.add(tuple(sorted((num_i, num_j, num_k))))
                #     Covered when num_i < 0
                elif num_k == 0 and zero_count > 0:
                    return_set.add(tuple(sorted((num_i, num_j, 0))))
        elif zero_count >= 3:
            return_set.add((0, 0, 0))

    return [list(s) for s in return_set]


test_cases = [([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0], [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]),
              ([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]),
              ([0,0,0], [[0,0,0]]),
              ([0,0],[]),
              ([-1, 0, 1], [[-1, 0, 1]])
              ]

for input, output in test_cases:
    assert sorted(threeSum(input)) == sorted(output)
