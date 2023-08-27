"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        graph, visited, stack = {}, set(), [node]
        
        while stack:
            cur_node = stack.pop()
            
            if cur_node in visited:
                continue
                
            if cur_node not in graph:
                graph[cur_node] = Node(cur_node.val)
            
            visited.add(cur_node)
            
            for neighbor in cur_node.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val)
                
                graph[cur_node].neighbors.append(graph[neighbor])
                stack.append(neighbor)
        
        return graph[node]
                    
            
            
        
        
        
        
            
            