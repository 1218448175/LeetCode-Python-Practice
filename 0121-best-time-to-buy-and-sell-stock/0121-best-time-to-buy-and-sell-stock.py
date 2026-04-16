class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0             # 一直不买
        dp1 = - prices[0]   # 只买了一次
        dp2 = float('-inf') # 买了一次，卖了一次

        for i in range(1, len(prices)):
            dp1 = max(dp1, dp0 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
        return max(dp0, dp2)


                



