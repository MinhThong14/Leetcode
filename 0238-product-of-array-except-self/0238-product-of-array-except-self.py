class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        prefix, suffix = [1], [1]
        
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i-1])
        
        for j in range(n-2, -1, -1):
            suffix.append(suffix[-1] * nums[j+1])
        
        for w in range(n):
            nums[w] = prefix[w] * suffix[n-w-1]
        
        return nums