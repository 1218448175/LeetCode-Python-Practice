# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = list()
        if not root:
            return []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            ans.append(list())
            for i in range(size):
                node = queue.popleft()
                ans[-1].append(node.val)
                l, r = node.left, node.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)
        return ans
        