# DP，两个字符串能否交叉得到第三个字符串，前两个长度和需要==第三个的长度，中间排序保持跟原字符串一致
# dp[i][j]指的是s1[:i+1]和s2[:j+1]能否组成s3[:i+j+1]
# 如果s3[i+j]等于s1[i]那么就看dp[i-1][j]，如果s3[i+j]等于s2[j]那么就看dp[i][j-1]
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
        for j in range(n+1):
            if s2[:j] == s3[:j]:
                dp[0][j] = True
        for i in range(m+1):
            for j in range(n+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]
