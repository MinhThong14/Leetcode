class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval:interval[0])
        
        res = []
        
        cur_min, cur_max = intervals[0][0], intervals[0][1]
        
        n = len(intervals)
        
        for i in range(1, n):
            if intervals[i][0] > cur_max:
                res.append([cur_min, cur_max])
                cur_min, cur_max = intervals[i][0], intervals[i][1]
            else:
                cur_max = max(cur_max, intervals[i][1])
  
        res.append([cur_min, cur_max])
        
        return res