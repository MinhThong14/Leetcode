class Solution:
    
    def dfs(self, graph, informTime, cur_id):
        ans = 0
        
        for u in graph[cur_id]:
            ans = max(self.dfs(graph, informTime, u) + informTime[cur_id], ans)
        
        return ans
            
        
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)    
            
        return self.dfs(graph, informTime, headID)
        