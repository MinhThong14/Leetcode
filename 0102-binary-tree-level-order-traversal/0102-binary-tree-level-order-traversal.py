# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        
        
        queue.append((root, 0))
        
        level = 0
        
        res = []
        
        while queue:
            node, cur_level = queue.popleft()
            level = cur_level + 1
            if node:
                if cur_level == len(res):
                    res.append([node.val])
                else:
                    res[-1].append(node.val)

                queue.append((node.left, level))
                queue.append((node.right, level))


            
        return res
                
        
        
        
        