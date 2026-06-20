class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True for _ in range(n)] for _ in range(n)]
        max_len_l = 0
        max_len_r = 0
        for i in range(1, n):
            for l in range(n):
                r = l + i
                if r >= n:
                    break
                if (r - l) == 1:
                    dp[l][r] = (s[l] == s[r])
                else:
                    dp[l][r] = dp[l+1][r-1] and s[l] == s[r]
                if dp[l][r] and r - l > max_len_l - max_len_r:
                    max_len_l = l
                    max_len_r = r

        return s[max_len_l: max_len_r+1]
                
            