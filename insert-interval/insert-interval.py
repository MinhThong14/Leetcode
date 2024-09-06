class Solution:
    def mergeInterval(self, intervals):
        n = len(intervals)
        res = []
        
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(1, n):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
        
        res.append([start, end])
        return res
                
                
            
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals.sort(key=lambda interval:interval[0])
        
        return self.mergeInterval(intervals)
        
        