# BFS，建两个list分别存放fresh和rotten，每次rotten换成上一轮刚rotten的橙子，发展下一轮
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotten = []
        fresh = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh.append((i, j))
        res = 0
        while fresh:
            if not rotten:
                return -1
            new_rotten = []
            for i, j in rotten:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (i+di, j+dj) in fresh:
                        new_rotten.append((i+di, j+dj))
                        fresh.remove((i+di, j+dj))
            rotten = new_rotten
            res += 1
        return res
