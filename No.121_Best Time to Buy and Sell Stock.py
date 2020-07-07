class Solution:
    def maxProfit(self, prices):
        
        if len(prices) == 0:
            return 0

        maxProfit = 0 
        minPrice = prices[0]

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit

s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))