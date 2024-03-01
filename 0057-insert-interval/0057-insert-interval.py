class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals.sort(key=lambda v:v[0])
        
        res = []
        
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(len(intervals)-1):
            if end < intervals[i+1][0]:
                res.append([start, end])
                start, end = intervals[i+1][0], intervals[i+1][1]
            elif end < intervals[i+1][1]:
                end = intervals[i+1][1]                
            
        res.append([start, end])
        
        return res