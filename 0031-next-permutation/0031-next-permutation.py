class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            self.swap(nums, l, r)
            l += 1
            r -= 1
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i > 0:
            j = n-1
            while j > i-1 and nums[j] <= nums[i-1]:
                j -= 1

            self.swap(nums, i-1, j)

        self.reverse(nums, i, n-1)
         
        return None
        