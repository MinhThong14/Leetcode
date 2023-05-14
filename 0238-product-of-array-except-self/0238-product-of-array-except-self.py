class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # count preffix product from left except the first one
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        

        # count suffix product from right except the last one
        suffix_prod = 1
        for j in range(len(nums)-2, -1, -1):
            suffix_prod *= nums[j+1]
            res[j] *= suffix_prod
        
        return res