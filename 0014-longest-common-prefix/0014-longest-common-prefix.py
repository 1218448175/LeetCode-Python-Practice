class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = len(strs[0])
        n = len(strs)
        temp = strs[0]

        if n == 1:
            return temp
        for i in range(1, n):
            s = strs[i]
            j = 0
            while j < ans and j < len(s):
                if temp[j] != s[j]:
                    break
                j += 1
            ans = j
        return temp[:ans]
        