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
        
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        
        self.max_sum = max(self.max_sum, left + root.val + right)
        
        return max(left + root.val, right + root.val)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        
        self.dfs(root)
        
        return self.max_sum