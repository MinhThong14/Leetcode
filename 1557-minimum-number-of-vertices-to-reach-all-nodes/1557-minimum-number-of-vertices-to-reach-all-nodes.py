"""
1. 0-1, 0-2, 2-5, 4-2, 3-4
[0, 3]
0-> 1->2->5
3-> 4->2->5

We need to find the total number of 0-indegree vetices
1. Buil a graph
2. Calculate indegree value of each node
3. If a node have 0 indegree, then adding to the result set

Time:0(n)
Space: O(n)


"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = {}
        
        for i, j in edges:
            if i not in graph:
                graph[i] = []
            graph[i].append(j)
            
        indegree = [0 for _ in range(n)]
        
        for values in graph.values():
            for value in values:
                indegree[value] += 1
        
        res = set()
        
        for i in range(n):
            if indegree[i] == 0:
                res.add(i)
                
        return res
        
        