class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max, local_min, global_max = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            cur_local_max = local_max
            local_max = max(nums[i], local_max * nums[i], local_min * nums[i])
            local_min = min(nums[i], cur_local_max * nums[i], local_min * nums[i])
            global_max = max(local_max, global_max)
            
        return global_max
            