class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            ans.insert(index[i], nums[i])
            i += 1
        return ans