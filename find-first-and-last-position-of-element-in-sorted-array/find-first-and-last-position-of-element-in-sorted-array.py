class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l+r+1)// 2
            
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        
        start, end = -1, -1
        if l >= 0 and nums[l] == target:
            start, end = l, l
            
            while start >= 0 and nums[start] == target:
                start -= 1
            start += 1
            
            while end < len(nums) and nums[end] == target:
                end += 1
            end -= 1
            
        return [start, end]