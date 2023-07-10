class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -10**9
        
        left, right = 0, len(height) - 1

        while left < right:
            cur_height = min(height[left], height[right])
            max_area = max(max_area,  cur_height * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
