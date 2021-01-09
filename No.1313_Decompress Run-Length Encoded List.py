class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        fre = 0
        val = 1
        
        while fre < len(nums) and val < len(nums):
            output = [nums[val]] * nums[fre]
            ans.extend(output)
            fre += 2
            val += 2
        return ans
    