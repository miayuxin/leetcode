class Solution:
    def findPairs(self, nums, k):
        
        res = 0
        
        if k < 0:
            return 0
        
        # Create a dictionary, key: each element, 
        # value: frequency of appearance of each element 
        
        numsDict = {}
        
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        
        if k == 0:
            for key, value in numsDict.items():
                if value >= 2:
                    res += 1
            
        if k > 0:
            for num in set(nums):
                if k > 0:
                    temp = k + num
                    if temp in numsDict:
                        res += 1
        return res

s = Solution()
nums = [1, 3, 1, 5, 4]
k = 0
print(s.findPairs(nums, k))