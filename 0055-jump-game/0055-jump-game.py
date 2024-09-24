class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step_need = 1
        
        n = len(nums)
        if n == 1:
            return True
        
        for i in range(n-2, -1, -1):
            if nums[i] >= step_need:
                step_need = 1
            else:
                step_need += 1
        
        return True if nums[0] >= step_need else False