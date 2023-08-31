class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        
        if not n:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0 for _ in range(n+1)]
        
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
        
        
        