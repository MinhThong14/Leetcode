class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda v:v[0])
        
        prev = float('-inf')
        count = 0
        
        for i in range(len(intervals)):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                count += 1
                prev = min(prev, intervals[i][1])
        
        return count
                