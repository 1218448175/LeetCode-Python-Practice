# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, prevTotal):
            if not root:
                return 0
            if not root.left and not root.right:
                return prevTotal * 10 + root.val
            prevTotal = prevTotal * 10 + root.val
            return dfs(root.left, prevTotal) + dfs(root.right, prevTotal)
        return dfs(root, 0)
        