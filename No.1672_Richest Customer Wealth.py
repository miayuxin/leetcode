from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        initialSum = 0
        maxSum = 0
        
        for i in range(0, len(accounts), 1):
            for j in range(0, len(accounts[i]), 1):
                initialSum += accounts[i][j]
            maxSum = max(initialSum, maxSum)
            initialSum = 0
        return maxSum
            
            

s = Solution()
accounts = [[1,2,3],[3,2,1]]
print(s.maximumWealth(accounts))