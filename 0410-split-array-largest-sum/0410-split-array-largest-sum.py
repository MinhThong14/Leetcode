class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        
        def canSplit(mid):
            count = 0
            cur_sum = 0
            for i in range(len(nums)):
                cur_sum += nums[i]
                if cur_sum > mid:
                    cur_sum = nums[i]
                    count += 1
            return count + 1 <= k
        
        while l <= r:
            mid = (r+l+1)//2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res