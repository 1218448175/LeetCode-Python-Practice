class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [1 if i == 0 else 0 for i in obstacleGrid[0]]
        if dp[0] == 0:
            return 0

        for i in range(m):
            for j in range(n):
                if j == 0 and i == 0:
                    continue
                elif i != 0 and j == 0:
                    dp[j] = 0 if obstacleGrid[i][j] else dp[j]
                elif j != 0 and i == 0:
                    dp[j] = 0 if obstacleGrid[i][j] else dp[j - 1]
                else:
                    dp[j] = 0 if obstacleGrid[i][j] else (dp[j - 1] + dp[j])
        return dp[-1]
        