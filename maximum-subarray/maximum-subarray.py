class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        l, r = 1, 1
        
        l_max, r_max = 0, 0
        max_value = nums[0]
        while r < n:
            if nums[r] + nums[r-1] > nums[r]:
                nums[r] = nums[r-1] + nums[r]
            else:
                l = r
            max_value = max(max_value, nums[r])
            r += 1
            
        return max_value