from collections import Counter
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return_list = set()
        available_nums = Counter(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                if -nums[i] - nums[j] in available_nums:
                    num_k = -nums[i] - nums[j]
                    minus_k = 1 if num_k == nums[i] else 0
                    if num_k == nums[j]:
                        minus_k += 1
                    if available_nums[num_k] > minus_k:
                        min_tuple = min(nums[i], num_k)
                        max_tuple = max(nums[j], num_k)
                        return_list.add((min_tuple, -min_tuple-max_tuple, max_tuple))
        return return_list

test_obj = Solution()
test_obj.threeSum([-1,0,1,2,-1,-4])