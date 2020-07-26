class Solution:
    def findMaxAverage(self, nums, k):
        
        if len(nums) == 0:
            return 0
        if k > len(nums):
            return -1
        
        largest = curSum = sum(nums[0:k])
        end = len(nums) - k + 1
        
        for i in range(1, end):
            prevSum = curSum
            curSum = prevSum - nums[i - 1] + nums[i + k - 1]
            largest = max(largest, curSum)
        
        return largest / k

s = Solution()
nums =  [1,12,-5,-6,50,3]
k = 4
print(s.findMaxAverage(nums, k))