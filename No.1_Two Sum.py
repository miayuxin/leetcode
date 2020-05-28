from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> int:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in num_dict and num_dict[temp] != i:
                return i, num_dict[temp]


s = Solution()
print(s.twoSum([2,7,11,15],9))
