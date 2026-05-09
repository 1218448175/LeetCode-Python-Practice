# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        nxt_target = targetSum - root.val
        if not root.left and not root.right:
            return nxt_target == 0
        return self.hasPathSum(root.left, nxt_target) or self.hasPathSum(root.right, nxt_target)
        