# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        pre = -1
        def inorder(node):
            nonlocal pre, ans
            if not node:
                return
            inorder(node.left)
            if pre != -1 and node.val - pre < ans: ans = node.val - pre
            pre = node.val
            inorder(node.right)
        inorder(root)
        return ans
        