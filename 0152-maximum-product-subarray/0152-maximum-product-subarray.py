class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max(nums)
        cur_max, cur_min = 1, 1

        for num in nums:
            if num == 0:
                cur_max, cur_min = 1, 1
                continue
            
            temp_min = cur_min * num
            temp_max = cur_max * num
            cur_min = min(num, temp_min, temp_max)
            cur_max = max(num, temp_min, temp_max)

            max_prod = max(cur_max, max_prod)
        return max_prod