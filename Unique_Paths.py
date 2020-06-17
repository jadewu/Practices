# 这一格的路线数 = 左边路线数 + 上面路线数，O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m]*n
        for i in range(n):
            for j in range(m):
                if (i == 0) and (j == 0):
                    dp[i][j] = 1
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

# O(n) space, O(mn) time
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
