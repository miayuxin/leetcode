from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        x = points[0][0]
        y = points[0][1]
        count = 0
        
        for i in range(1, len(points), 1):
            x1 = points[i][0]
            y1 = points[i][1]
            while x != x1 or y!= y1:
                moveX = abs(x1 - x)
                moveY = abs(y1 - y)
                count += max(moveX, moveY)
                x = points[i][0]
                y = points[i][1]
        return count

s = Solution()
points = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints(points))