# 2D DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 
        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    last = dp[i-1][0]
                elif i == 0:
                    last = dp[0][j-1]
                else:
                    last = min(dp[i-1][j], dp[i][j-1])
                dp[i][j] = last + grid[i][j]
        return dp[-1][-1]
