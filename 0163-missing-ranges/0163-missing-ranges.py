class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        res = []
        
        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        
        i = 0
        
        while i < n:
            if i == 0 and nums[i] > lower:
                res.append([lower, nums[i]-1])
            
            if i < n- 1 and nums[i+1] - nums[i] > 1:
                res.append([nums[i]+1, nums[i+1]-1])
            
            i += 1
        
        if nums[i-1] < upper:
            res.append([nums[i-1] +1, upper])
        
        return res
            