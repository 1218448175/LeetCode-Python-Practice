class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [[0 for j in range(i + 1)] for i in range(n)]
        
        if n == 1:
            return triangle[0][0]

        for i in range(n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif i == j:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1])
        