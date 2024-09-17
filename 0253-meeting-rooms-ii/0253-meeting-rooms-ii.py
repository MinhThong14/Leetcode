import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        heapq.heapify(rooms)
        
        intervals.sort(key=lambda interval:interval[0])
        
        heapq.heappush(rooms, intervals[0][1])
        
        n = len(intervals)
        
        for i in range(1, n):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        
        return len(rooms)
        
        