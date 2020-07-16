class Solution:
    def findLeftSwapPoint(self, nums):
        #Phase 1
        left = 0
        for i in range(1, len(nums)):
            if (nums[i] < nums[i-1]):
                left = (i-1)
                break
        #Phase 2
        for i in range(left + 1, len(nums)):
            while (left >=0 and nums[left] > nums[i]):
                left -= 1
        return left
    
    def findRightSwapPoint(self, nums):    
        #Phase 1
        right = 0
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] > nums[i+1]):
                right = (i+1)
                break
        #Phase 2
        for i in range(right - 1, -1, -1):
            while (right < len(nums) and nums[right] < nums[i]):
                right += 1
        return right
    
    def findUnsortedSubarray(self, nums):
        left = self.findLeftSwapPoint(nums)
        right = self.findRightSwapPoint(nums)
        if (right == 0):
            return 0
        return (right - left - 1)

s = Solution()
nums = [2, 1]
print(s.findUnsortedSubarray(nums))