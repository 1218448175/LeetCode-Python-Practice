class Solution:
    def isValid(self, s: str) -> bool:
        ans = True
        n = len(s)
        patch_dict = {'}': '{', ')': '(', ']': '['}
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            elif stack:
                left = stack.pop()
                if patch_dict[char] != left:
                    ans = False
                    break
            else:
                ans = False
                break
        if stack:
            ans = False
        return ans
        