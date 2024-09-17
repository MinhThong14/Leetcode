class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [[w/q, q] for q, w in zip(quality, wage)]
        workers.sort()
        
        maxHeap = []
        totalQuality = 0
        minCost = math.inf
        for r, q in workers:
            heappush(maxHeap, -q)
            totalQuality += q
            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)
            if len(maxHeap) == k:
                minCost = min(minCost, totalQuality * r)
        
        return minCost