from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        prev = nums[0]
        
        for i in range(1, len(nums), 1):
            nums[i] += prev
            prev = nums[i]
        return nums

s = Solution()
nums = [1,2,3,4]
print(s.runningSum(nums))