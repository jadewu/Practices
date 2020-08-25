# 典型dp题
# 为什么会形成回文？因为这个此时的字母和它对称位的字母相同，它的对称位可以是0~i-1的任一个，对应不同起始点的回文subsequence
# 注意，如果i是从前往后，那么对应位j从i往前遍历；如果i从后往前，j从i+1往后遍历
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1] + 2
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
        # print(dp)
        return dp[-1][0]
                    
