# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isMatch(self, root, subRoot):
        if not root or not subRoot:
            return root == subRoot
        
        return root.val == subRoot.val and self.isMatch(root.left, subRoot.left) and self.isMatch(root.right, subRoot.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = []
        
        queue.append(root)
        
        while queue:
            cur_node = queue.pop(0)
            
            if self.isMatch(cur_node, subRoot):
                return True
            
            if cur_node.left:
                queue.append(cur_node.left)
            
            if cur_node.right:
                queue.append(cur_node.right)
        
        return False