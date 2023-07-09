class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for j in range(n-2, -1, -1):
            suffix[j] = nums[j+1] * suffix[j+1]
        
        for w in range(n):
            nums[w] = prefix[w] * suffix[w]

        return nums

