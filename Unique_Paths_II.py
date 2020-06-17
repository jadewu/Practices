# 在uique paths的基础上加obstacleGrid == 0时，dp = 0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0]*m]*n
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                    continue
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                        continue
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
