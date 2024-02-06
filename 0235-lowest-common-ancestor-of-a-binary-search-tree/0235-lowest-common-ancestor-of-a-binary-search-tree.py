# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > max(p.val, q.val):
            # If the current node has a value greater than both p and q, it must be on the left of the BST.
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < min(p.val, q.val):
            # If the current node has a value lesser than both p and q, it must be on the right of the BST.
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If neither, we are on the parent node.
        return root