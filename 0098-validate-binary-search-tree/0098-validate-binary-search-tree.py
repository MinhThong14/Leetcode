# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidate(self, root, low = float('-inf'), high = float('inf')):
        if not root:
            return True
        
        if root.val <= low or root.val >= high:
            return False
        
        return self.isValidate(root.left, low, root.val) and self.isValidate(root.right, root.val, high)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValidate(root)