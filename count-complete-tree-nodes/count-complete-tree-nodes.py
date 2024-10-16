# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        count = 0
        
        queue = deque()
        
        queue.append(root)
        
        while queue:
            cur_node = queue.popleft()
            count += 1
            
            if cur_node.left:
                queue.append(cur_node.left)
            
            if cur_node.right:
                queue.append(cur_node.right)
            
        return count