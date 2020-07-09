class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        
        count = 0
        res = 0
        
        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0     
        return res

s = Solution()
nums = [0, 1, 0, 1, 1, 1]
print(s.findMaxConsecutiveOnes(nums))