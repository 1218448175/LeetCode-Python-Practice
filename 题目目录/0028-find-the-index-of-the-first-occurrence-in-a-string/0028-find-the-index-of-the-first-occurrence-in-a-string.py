class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        # 1. 构建 next 数组
        next_arr = [0] * m
        j = 0 # j 指向模式串的前缀末尾
        for i in range(1, m): # i 指向模式串的后缀末尾
            while j > 0 and needle[i] != needle[j]:
                j = next_arr[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next_arr[i] = j

        # 2. 匹配过程
        j = 0 # j 指向 needle
        for i in range(n): # i 指向 haystack，从 0 开始
            while j > 0 and haystack[i] != needle[j]:
                j = next_arr[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            
            # 如果匹配长度等于模式串长度
            if j == m:
                return i - m + 1
                
        return -1