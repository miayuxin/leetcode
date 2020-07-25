class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        nums_Dict = {}
        
        for index, num in enumerate(nums):
            if num in nums_Dict:
                prev = nums_Dict[num]
                nums_Dict[num] = index
                if index - prev <= k:
                    return True
            else:
                nums_Dict[num] = index
        return False

s = Solution()
nums =  [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))
