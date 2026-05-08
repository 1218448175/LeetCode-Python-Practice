# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and self.check(l.left, r.right) and self.check(l.right, r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.check(root.left, root.right)
        