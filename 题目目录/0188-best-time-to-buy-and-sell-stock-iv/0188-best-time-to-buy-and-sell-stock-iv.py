class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (2 * k + 1)
        for j in range(1, k + 1):
            dp[2 * j - 1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[2 * j - 1] = max(dp[2 * j - 2] - prices[i], dp[2 * j - 1])
                dp[2 * j] = max(dp[2 * j - 1] + prices[i], dp[2 * j])

        return dp[-1]
        