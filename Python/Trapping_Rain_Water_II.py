# PriorityQueue + BFS
# 先把边界点放进min heap，然后看它们四周的点有没有更小的点，如果有，差值就是雨水量，再把更小的点放进min heap里
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        h = []
        # 需要给每个点标记是否被查看并计算过
        visited = [[0]*n for _ in range(m)]
        res = 0
        # 把所有边界点放进min heap，并标记为visited
        # 因为边界点是必不可能接到雨水的，可以把它们作为root开始BFS
        for i in range(m):
            for j in range(n):
                if (i in (0, m-1)) or (j in (0, n-1)):
                    heapq.heappush(h, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        # BFS的过程，每次取出最小的点，看它四周有没有比它小的，计算高度差
        # 因为每次都是取heap里最小值的点来查看四周，所以计算得到的高度差一定是这个点四周比它大的最小值
        #       [1, 2, 3, 2]
        #       [0, 1, 2, 1]
        #       [3, 4, 5, 1]
        # 边界点中最小的是(1,0)，然后是(0,0), (1,3), (2,3)，再是(0,1), 到这里的时候，(1,1)比(0,0)要小
        # 计算雨水量2-1=1，(1,1)标记为visited，放进min heap里，所以接下来是(1,1)
        # 再然后是(0,3), (0,2), 雨水量3-2=1，(1,2)标记为visited，放进min heap，接下来是(1,2)
        # 此时(1,1)已经是visited，所以不会再重复计算雨水量
        while h:
            height, i, j = heapq.heappop(h)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if (0 <= x < m) and (0 <= y < n) and (not visited[x][y]):
                    res += max(0, height - heightMap[x][y])
                    heapq.heappush(h, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
                # print(res)
        return res
