class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 5 for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][0] = 0
            dp[i][1] = max(dp[i][0] - prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i][1] + prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i][2] - prices[i], dp[i - 1][3])
            dp[i][4] = max(dp[i][3] + prices[i], dp[i - 1][4])
        return max(dp[n - 1])
        