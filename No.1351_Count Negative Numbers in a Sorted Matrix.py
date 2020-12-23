from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[i]), 1):
                if grid[i][j] < 0:
                    count += 1
        return count


s = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(s.countNegatives(grid))