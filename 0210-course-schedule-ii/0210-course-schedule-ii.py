

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

from collections import defaultdict
from collections import deque

class Solution:
    
    def topologicalSort(self, n, graph):
        indegree = [0] * n
        
        for values in graph.values():
            for value in values:
                indegree[value] += 1
        
        visited = []
        
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                visited.append(i)
                
        while queue:
            cur_course = queue.popleft()
            for course in graph[cur_course]:
                indegree[course] -= 1
                
                if indegree[course] == 0 and course not in visited:
                    queue.append(course)
                    visited.append(course)
        
        return visited if len(visited) == n else []
            
     
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        return self.topologicalSort(numCourses, graph)
        
        