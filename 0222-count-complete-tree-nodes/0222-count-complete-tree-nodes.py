# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
        
    def compute_depth(self, root):
        d = 0
        while root.left:
            root = root.left
            d += 1
        
        return d
    
    def exists(self, indx, d, node):
        l, r = 0, 2**d - 1
        
        for _ in range(d):
            mid = (r + l + 1) // 2
            if indx < mid:
                node = node.left
                r = mid - 1
            else:
                node = node.right
                l = mid + 1
        
        return node is not None
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        d = self.compute_depth(root)
        if d == 0:
            return 1
        
        l, r = 0, 2**d-1
        
        while l <= r:
            mid = (r + l + 1) // 2
            
            if self.exists(mid, d, root):
                l = mid + 1
            else:
                r = mid - 1
        
        return (2**d-1) + l
        