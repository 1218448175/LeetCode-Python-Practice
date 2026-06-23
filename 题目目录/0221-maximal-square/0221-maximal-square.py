class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        s = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                num = int(matrix[i][j])
                if i > 0 and j > 0:
                    s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + num
                elif i == 0 and j != 0:
                    s[i][j] = s[i][j - 1] + num
                elif i != 0 and j == 0:
                    s[i][j] = s[i - 1][j] + num
                else:
                    s[i][j] = num
        dp = [[int(matrix_k[v]) for v in range(n)] for matrix_k in matrix]
        ans = 0 if s[-1][-1] == 0 else 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 if int(matrix[i][j]) else 0
                ans = max(dp[i][j], ans)
        return ans * ans
        