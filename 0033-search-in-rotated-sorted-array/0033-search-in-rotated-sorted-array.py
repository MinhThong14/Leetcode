class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1


        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid
                else:
                    left = mid + 1

        return -1
            