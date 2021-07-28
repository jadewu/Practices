# DP，记录最大差价和目前的最低价，每次对比前一天的最大差价和今天可以得到的差价
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        m = len(prices)
        dp = [0]*m
        low = prices[0]
        for i in range(m):
            if prices[i] < low:
                low = prices[i]
            dp[i] = max(dp[i-1], prices[i]-low)
        return dp[-1]
