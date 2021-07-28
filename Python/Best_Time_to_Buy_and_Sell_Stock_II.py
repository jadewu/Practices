# 基于买股票I，加上一个res记录结果，再就是如果不acending了就重新开始记low和差价
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        dp = [0]*m
        low = prices[0]
        res = 0
        for i in range(1,m):
            if prices[i] < low:
                low = prices[i]
            if prices[i]-low > dp[i-1]:
                dp[i] = prices[i]-low
                res -= dp[i-1]
                res += dp[i]
            else:
                low = prices[i]
        return res
