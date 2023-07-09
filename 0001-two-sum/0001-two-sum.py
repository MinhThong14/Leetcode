class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = []
        for i, num in enumerate(nums):
            new_nums.append((num, i))

        new_nums.sort(key=lambda num: num[0])
        
        left, right = 0, len(nums)-1
        while left < right:
            if new_nums[left][0] + new_nums[right][0] == target:
                return [new_nums[left][1], new_nums[right][1]]
            if new_nums[left][0] + new_nums[right][0] < target:
                left += 1
            else:
                right -= 1
            

