class Solution:
    def removeElement(self, nums, val):
        
        if len(nums) == 0:
            return 0
        
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            else:
                count += 1
            i += 1
        return count


s = Solution()
l1 = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(s.removeElement(l1, val))