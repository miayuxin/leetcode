class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        appeardSet = set(nums)
        i = 0
        
        while i >= 0:
            if i not in appeardSet:
                return i
            i += 1