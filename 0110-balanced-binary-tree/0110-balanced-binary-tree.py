# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # Compute height of left subtree.
        lh = self.isBalanced(root.left)
        if lh == 0:
            # If left subtree is not balanced, return 0.
            return 0

        # Compute height of right subtree.
        rh = self.isBalanced(root.right)
        if rh == 0:
            # If right subtree is not balanced, return 0.
            return 0

        # Allowed values for (lh - rh) are 1, -1, 0.
        if (abs(lh - rh) > 1):
            return 0

        # If we reach here means tree is height-balanced tree, 
        # so return height.
        else:
            return max(lh, rh) + 1