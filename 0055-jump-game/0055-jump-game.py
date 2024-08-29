class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n == 1:
            return True
        
        need_steps = 1
        
        for i in range(n-2, -1, -1):
            if nums[i] >= need_steps:
                need_steps = 1
            else:
                need_steps += 1
        print(need_steps)
        return True if need_steps == 1 else False