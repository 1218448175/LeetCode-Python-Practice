# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([root])
        ans = list()
        while queue:
            total = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                total += node.val
                l, r = node.left, node.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)
            ans.append(total / size)
        return ans
        