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
        
        queue = deque()
        queue.append(root)
        
        count = 1
        
        while queue:
            cur_node = queue.popleft()
            
            if cur_node.left:
                count += 1
                queue.append(cur_node.left)
            
            if cur_node.right:
                count += 1
                queue.append(cur_node.right)
        
        return count
