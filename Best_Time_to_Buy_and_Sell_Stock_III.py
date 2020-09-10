# 重新投资的想法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price-buy1)
            buy2 = min(buy2, price-profit1)
            profit2 = max(profit2, price-buy2)
            # print(buy1, buy2)
        return profit2

# 双向DP
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit