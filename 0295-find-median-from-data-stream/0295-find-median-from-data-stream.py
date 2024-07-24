from heapq import *

class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        
    def addNum(self, num: int) -> None:
        if len(self.smaller) == len(self.larger):
            heappush(self.larger, -heappushpop(self.smaller, -num))
        else:
            heappush(self.smaller, -heappushpop(self.larger, num))

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2
        
        return self.larger[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()