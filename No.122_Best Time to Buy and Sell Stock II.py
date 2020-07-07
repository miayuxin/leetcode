class Solution:
    def maxProfit(self, prices):
        
        if len(prices) == 0:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price > minPrice:
                maxProfit += price - minPrice
                minPrice = price
            else:
                minPrice = price
        return maxProfit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))