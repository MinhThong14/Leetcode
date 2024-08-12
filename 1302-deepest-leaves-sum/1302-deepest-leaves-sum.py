# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        
        deepest_sum, deepest = 0, 0
        
        while queue:
            cur_node, cur_deep = queue.popleft()
            
            if not cur_node.left and not cur_node.right:
                if deepest < cur_deep:
                    deepest_sum = cur_node.val
                    deepest = cur_deep
                elif deepest == cur_deep:
                    deepest_sum += cur_node.val
                    
            else:
                if cur_node.left:
                    queue.append((cur_node.left, cur_deep+1))
                if cur_node.right:
                    queue.append((cur_node.right, cur_deep+1))
        
        return deepest_sum