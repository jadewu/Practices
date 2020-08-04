# DFS, O(N^N + ElogE), E is length of times
# d[n]记录所有路径起点、终点、距离，dist[node]记录原点到所有点的距离，初始都是inf
# 按照距离这点由近到远做dfs，如果新算出的时间elapsed比以前算出的时间dist[node]要长，就返回上一步
# 如果新算出的时间比以前的要短，就替换
# 如果最后有dist[node]是inf，就说明从原点无法到这点，因为这是有向图
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        d = collections.defaultdict(list)
        for n, nei, t in times:
            d[n].append((t, nei))
        dist = {node: float('inf') for node in range(1, N+1)}
            
        def dfs(node, elapsed):
            if elapsed >= dist[node]: 
                return
            dist[node] = elapsed
            for t, nei in sorted(d[node]):
                dfs(nei, elapsed + t)
        
        dfs(K, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1

# Dijkstra's Algorithm的heapq做法，每次都选出距离原点最短的点，更新它周围的点的距离数据
# O(ElogE) in the heap implementation, as potentially every edge gets added to the heap.
# 每次heappop出来的都是它里面距离原点最短的点，如果走过了，就continue，没走过就记录长度并放进heapq里
# 为什么记录在dist里的是原点到这一点最短的距离？因为heapq是按照距离原点的距离pop出，与路径无关，单纯看长度数值
# 如果有点不在dist里，就说明没走到那个点；如果都走到了，return max就行
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nei, t in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+t, nei))
        if len(dist) == N:
            return max(dist.values())
        return -1
