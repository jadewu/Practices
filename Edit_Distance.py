# DP，典型的两个字符串比较
# 为了使两个单词相同，可能需要进行加/减/改，三种操作，求需要的最少操作数
# 不是很懂为什么这道题的名字是这个
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "" or word2 == "":
            return max(len(word1), len(word2))
        m = len(word1)
        n = len(word2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if word1[i] == word2[j] or dp[i][j-1] == j-1:
                        dp[i][j] = j
                    else:
                        dp[i][j] = j + 1
                elif j == 0:
                    if word1[i] == word2[j] or dp[i-1][j] == i-1:
                        dp[i][j] = i
                    else:
                        dp[i][j] = i + 1
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        print(dp)
        return dp[-1][-1]
                    
