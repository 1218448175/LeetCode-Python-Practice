# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l, r = root.left, root.right
        h_l, h_r = 1, 1
        while l:
            h_l += 1
            l = l.left
        while r:
            h_r += 1
            r = r.right
        
        if h_l == h_r:
            return pow(2, h_l) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        