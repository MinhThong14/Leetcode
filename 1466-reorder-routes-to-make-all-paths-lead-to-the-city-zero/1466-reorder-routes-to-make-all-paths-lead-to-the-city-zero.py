from collections import deque
class Solution:
    def bfs(self, node, n, graph):
        queue = deque()
        visited = [False for _ in range(n)]
        queue.append(node)
        visited[node] = True
        count = 0
        
        while queue:
            cur_node = queue.popleft()
            
            for neighbor, sign in graph[cur_node]:
                if not visited[neighbor]:
                    count += sign
                    visited[neighbor] = True
                    queue.append(neighbor)
        return count
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for connection in connections:
            a, b = connection[0], connection[1]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        
        res = self.bfs(0, n, graph)
        return res
        
            
            
        