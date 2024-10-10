class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, is_sell, holding):
            if i == len(prices):
                return 0
            
            if is_sell:
                return dp(i+1, 0, holding)

            do_nothing = dp(i+1, is_sell, holding)
            do_something = 0
            if holding:
                do_something = prices[i] + dp(i+1, 1, 0)
            else:
                do_something = -prices[i] + dp(i+1, 0, 1)
                
            return max(do_nothing, do_something)
                
        return dp(0, 0, 0)