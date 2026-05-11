# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.size = 0
        def DFS(root, level):
            if not root:
                return
            if level == self.size:
                self.ans.append(root.val)
                self.size += 1
            DFS(root.right, level + 1)
            DFS(root.left, level + 1)
        
        DFS(root, 0)
        return self.ans
