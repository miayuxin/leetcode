class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set()
        for i in jewels:
            jewelSet.add(i)
            
        count = 0    
        for i in stones:
            if i in jewelSet:
                count += 1
        return count