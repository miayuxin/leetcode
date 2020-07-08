class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) == 0:
            return False
        
        appeardSet = set()
        
        for i in nums:
            if i in appeardSet:
                return True
            else:
                appeardSet.add(i)
        return False