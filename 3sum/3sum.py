class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        
        res = []
        
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return res