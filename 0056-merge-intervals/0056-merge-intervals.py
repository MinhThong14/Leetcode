class Solution:
    def isOverlap(self, interval1, interval2):
        return max(interval1[0], interval2[0]) - min(interval1[1], interval2[1]) <= 0
    
    def mergeInterval(self, interval1, interval2):
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        result = []
        i = 0

        while i < len(intervals):
            curInterval = intervals[i]
            k = i

            while k < len(intervals)-1 and self.isOverlap(curInterval, intervals[k+1]):
                curInterval = self.mergeInterval(curInterval, intervals[k+1])
                k += 1
            
            if i == k:
                i += 1
            else:
                i = k + 1
            
            result.append(curInterval)
        
        return result