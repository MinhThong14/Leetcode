class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        
        while l < r:
            mid = (r+l+1) // 2
            
            if mid == 0:
                if arr[mid] > arr[mid+1]:
                    return mid
                l = mid + 1
            elif mid == n-1:
                if arr[mid] > arr[mid-1]:
                    return mid
                r = mid - 1
            elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
                l = mid + 1
            elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
                r = mid - 1
                
        return r
        