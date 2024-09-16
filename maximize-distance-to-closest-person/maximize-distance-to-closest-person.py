"""
1. [1, 0, 0, 0] -> num_one = 1 -> nums[0] = 1 -> n-1-0
2. [0, 0, 0, 1] -> num_one = 1 -> nums[n-1] = 1 -> n-1-0
3. [1, 0, 1, 0] -> num_one > 1 -> nums[0] = 1, nums[2] = 1 -> (2-0)/2 = 1
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        
        l, r = 0, 0
        max_dist = float('-inf')
        res = 0
        
        while r < n:
            if seats[r] == 1:
                if l == 0 and seats[l] != 1 and r - l > max_dist:
                    res = r - l
                    max_dist = r - l
                elif (r-l) // 2 > max_dist:
                    res = (r-l) // 2
                    max_dist = (r-l) // 2

                l = r
            r += 1
        if r - l - 1 > max_dist:
            res = r-l-1
        
        return res
        
                    
                        
                
                

                    
        