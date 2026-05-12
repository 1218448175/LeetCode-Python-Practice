# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        queue.append([root])
        res_list = []
        direciton = 1

        while queue[0]:
            ls = queue.popleft()
            sub_list = []
            tmp_list = []
            for t in ls:
                if not t:
                    continue
                sub_list.append(t.left)
                sub_list.append(t.right)
                tmp_list.append(t.val)
            if tmp_list:
                if direciton == -1:
                    tmp_list.reverse()
                res_list.append(tmp_list)
            queue.append(sub_list)

            direciton *= -1

        return res_list
        