class Solution:
    def findLengthOfLCIS(self, nums):
        
        if len(nums) == 0:
            return 0
        
        longest = 1
        cur = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
                longest = max(longest, cur)
            else:
                cur = 1
        return longest

s = Solution()
nums = [1, 3, 5, 4, 7, 8, 9]
print(s.findLengthOfLCIS(nums))
