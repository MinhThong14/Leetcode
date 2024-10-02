# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        toDeleteSet = set(to_delete)
        
        forest = []
        
        queue = deque([root])
        
        while queue:
            cur_node = queue.popleft()
            
            if cur_node.left:
                queue.append(cur_node.left)
                
                if cur_node.left.val in toDeleteSet:
                    cur_node.left = None
            
            if cur_node.right:
                queue.append(cur_node.right)
                
                if cur_node.right.val in toDeleteSet:
                    cur_node.right = None
            
            if cur_node.val in toDeleteSet:
                if cur_node.left:
                    forest.append(cur_node.left)
                if cur_node.right:
                    forest.append(cur_node.right)
            
        if root.val not in toDeleteSet:
            forest.append(root)
        
        
        return forest