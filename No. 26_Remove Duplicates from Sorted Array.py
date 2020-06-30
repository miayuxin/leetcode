class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1

s = Solution()
l1 = [0, 0, 1, 1, 2, 3, 4]
print(s.removeDuplicates(l1))