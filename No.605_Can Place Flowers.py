class Solution:        
    
    def canPlot(self, flowerbed, pos):
        if pos != 0 and flowerbed[pos-1] == 1:
            return False
        if flowerbed[pos] == 1:
            return False
        if pos != len(flowerbed) - 1 and flowerbed[pos + 1] == 1:
            return False
        return True
        
    def canPlaceFlowers(self, flowerbed, n):

        plot = 0

        for i in range(len(flowerbed)):
            if self.canPlot(flowerbed, i):
                flowerbed[i] = 1
                plot += 1

        if plot >= n:
            return True
        elif plot < n:
            return False

s = Solution()
flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
print(s.canPlaceFlowers(flowerbed, n))

