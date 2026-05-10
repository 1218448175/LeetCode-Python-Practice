# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -1001, -1001
            l_max, l_tail_max = dfs(root.left)
            r_max, r_tail_max = dfs(root.right)
            root_tail_max = max(l_tail_max + root.val, r_tail_max + root.val, root.val)
            root_max = max(l_max, r_max, root_tail_max, l_tail_max + r_tail_max + root.val)
            
            return root_max, root_tail_max
        return max(dfs(root))
        