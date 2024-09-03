from collections import defaultdict
from collections import deque

class Solution:
    def topological_sort(self, n, graph):
        indegree = [0 for _ in range(n)]
        
        for i in range(n):
            for vertex in graph[i]:
                indegree[vertex] += 1
        
        queue = deque()
        for j in range(n):
            if indegree[j] == 0:
                queue.append(j)
                
        res = []

        while queue:
            cur_vertex = queue.popleft()
            res.append(cur_vertex)
            
            for vertex in graph[cur_vertex]:
                indegree[vertex] -= 1
                if indegree[vertex] == 0:
                    queue.append(vertex)
        
        return res
        
            
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        if numCourses == 1:
            return [0]
        
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        result = self.topological_sort(numCourses,graph)
         
        return result if len(result) == numCourses else []
        