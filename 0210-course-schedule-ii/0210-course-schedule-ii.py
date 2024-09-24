from collections import defaultdict
from collections import deque

"""
Ex1: [[1, 0]] -> 0-1
Ex2: [[1,0], [2, 0], [3, 1], [3, 2]] -> 0-1-2-3

1. Build graph
2. Topological sort to find correct order
    a. Creating indegree array
    b. If indegree == 0 then add to queue
    c. Pop node in queue then add to res
    d. Traverse adjacent nodes of curnode, then decrease indegree value by 1
    e. If indegree value == 0 then add to queue
    f. Repeat the steps until queue is empty
3. If len res == numCourses then return res, otherwise return empty array
"""

class Solution:
    def topologicalSort(self, n, graph):
        indegree = [0 for _ in range(n)]
        
        for values in graph.values():
            for value in values:
                indegree[value] += 1
        
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = [0 for _ in range(n)]
        
        res = []
        
        while queue:
            cur_node = queue.popleft()
            res.append(cur_node)
            visited[cur_node] = 1
            
            for neighboor in graph[cur_node]:
                indegree[neighboor] -= 1
                if not visited[neighboor] and indegree[neighboor] == 0:
                    queue.append(neighboor)
        
        return res if len(res) == n else []
            
            
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
            
        return self.topologicalSort(numCourses, graph)
        
        