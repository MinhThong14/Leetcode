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
        
        queue = [root]

        while queue:
            node = queue.pop(0)
            if self.isMatch(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False