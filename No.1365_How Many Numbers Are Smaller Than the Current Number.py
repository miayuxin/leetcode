from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:    
        res = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        return res


s = Solution()
nums = [8,1,2,2,3]
print(s.smallerNumbersThanCurrent(nums))