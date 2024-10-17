# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        self.result = max(self.result, left + 1 + right)
        
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        self.dfs(root)
        return self.result - 1
        