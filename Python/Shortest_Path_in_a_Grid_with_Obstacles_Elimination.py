# 常规BFS做法，存放的是（横坐标，纵坐标，剩余可用障碍数，当前步数）
# 对于每个点，往四周探寻，如果有一条线到达右下角，立即返回步数，就一定是最小步数，因为每个while cycle所有路线都是step+1
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = [(0, 0, 0, 0)]
        visited = {(0, 0): 0}
        step = 0
        
        while q:
            row, col, obs, step = q.pop(0)
            if obs > k:
                continue
            if row == m - 1 and col == n - 1:
                return step
            for nrow, ncol in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= nrow < m and 0 <= ncol < n:
                    if grid[nrow][ncol]:
                        nobs = obs + 1
                    else:
                        nobs = obs
                    if (nrow, ncol) not in visited or visited[(nrow, ncol)] > nobs:
                        visited[(nrow, ncol)] = nobs
                        q.append((nrow, ncol, nobs, step+1))
        return -1
