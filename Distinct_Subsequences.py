# 两个字符串找t作为subsequence在s里出现的次数，DP
# dp[i][j]代表t[:j]在s[:i]里重复的次数，如果s[i] == t[j]那么s[i]可以和它前面的所有t[:j-1]加起来组成t[:j]，总共是dp[i-1][j-1]个
# 而还没有到s[i]的时候，t[:j]出现此时是dp[i-1][j]
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for j in range(1, n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]
