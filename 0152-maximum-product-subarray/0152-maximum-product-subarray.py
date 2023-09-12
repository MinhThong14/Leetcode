class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max(nums)
        
        min_num, max_num = 1, 1
        
        for num in nums:
            
            if num == 0:
                min_num, max_num = 1, 1
                continue
            
            temp_min = min_num * num
            temp_max = max_num * num
            
            min_num = min(num, temp_min, temp_max)
            max_num = max(num, temp_min, temp_max)
            
            max_prod = max(max_prod, max_num)
            
        return max_prod