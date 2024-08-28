class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        l, r = 0, n-1
        
        while l < r:
            max_water = max(max_water, min(height[l], height[r]) * (r-l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water