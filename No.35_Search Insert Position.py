class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        numsDict = {}
        for i in range(len(nums)):
            numsDict[nums[i]] = i
        
        if target in numsDict:
            return numsDict[target]
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

