class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * 2 * n
        def backtrack(left: int, right: int):
            if right == n:
                ans.append("".join(path))
            if left < n:
                path[left + right] = '('
                backtrack(left + 1, right)
            if right < left:
                path[left + right] = ')'
                backtrack(left, right + 1)
        backtrack(0, 0)
        return ans
        