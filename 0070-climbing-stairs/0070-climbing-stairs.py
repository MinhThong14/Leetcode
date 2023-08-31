class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        
        if not n:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
        
        