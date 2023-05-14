class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = (i, num)
        
        nums.sort(key=lambda nums: nums[1])

        l, r = 0, len(nums)-1

        while l <= r:
            cur_sum = nums[l][1] + nums[r][1]
            if cur_sum == target:
                return [nums[l][0], nums[r][0]]
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
        

