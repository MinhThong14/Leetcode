class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        
        first, second = -1, -1
        n = len(seats)
        
        for i in range(n):
            if seats[i] == 1:
                if first == -1:
                    first = i
                    max_dist = max(max_dist, first)
                else:
                    second = i
                    max_dist = max(max_dist, (second - first)//2)
                    first = second
    
        
        if second == -1:
            mid = n//2
            if first == mid:
                return mid
            elif first < mid:
                return n-first-1
            elif first > mid:
                return first
        
        max_dist = max(max_dist, n-second-1)
        
        return max_dist
            
                    