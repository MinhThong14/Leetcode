class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            nums[i] = (num, i)
        
        nums.sort(key=lambda num:num[0])
        
        l, r = 0, len(nums)-1
        
        while l < r:
            if nums[l][0] + nums[r][0] == target:
                return [nums[l][1], nums[r][1]]
            elif nums[l][0] + nums[r][0] > target:
                r -= 1
            else:
                l += 1
            