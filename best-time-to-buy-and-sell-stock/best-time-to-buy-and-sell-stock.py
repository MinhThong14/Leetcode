class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        buy, sale = prices[0], prices[0]
        
        n = len(prices)
        
        for i in range(1, n):
            if prices[i] <= prices[i-1]:
                buy = min(buy, prices[i])
            else:
                sale = prices[i]
                max_profit = max(max_profit, sale-buy)
        
        return max_profit
        
        