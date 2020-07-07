class Solution:
    def majorityElement(self, nums):
        
        candidate = None
        count = 0
        
        for i in nums:
            if count == 0:
                candidate = i
                count += 1
            elif i == candidate:
                count += 1
            else:
                count -= 1
        return candidate

s = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(s.majorityElement(nums))