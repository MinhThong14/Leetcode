from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        heap = []
        
        res = []
        
        for key, value in freq.items():
            heappush(heap, (-value, key))
            
        for _ in range(k):
            val, key = heappop(heap)
            res.append(key)
    
        return res