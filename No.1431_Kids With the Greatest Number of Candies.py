from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        retList = []
        for i in candies:
            if i > maxCandies:
                maxCandies = i
            
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                retList.append(True)
            else:
                retList.append(False)
        return retList

s = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(s.kidsWithCandies(candies, extraCandies))
print(candies)