class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        l = len(s)
        if l == 0:
            return True
        ans = False
        for j in t:
            if s[i] == j:
                i += 1 
            if i == l:
                ans = True
                break
        return ans
        