# 求最小值问题，需要用到dp
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n]*n
        dp[0] = 0
        for i in range(1,n):
            for j in range(i+1):
                # print(s[j:i+1])
                if s[j:i+1] == s[j:i+1][::-1]:
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)
                    # print(dp)
        return dp[-1]
