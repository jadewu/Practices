# 令人迷惑的题，DFS，建树的过程有点神奇，因为是无方向的边，按照dfs遍历才能分清楚谁是谁的子节点
# counter，defaultdict，set()，这三个都不能换成普通的list，不然就超时
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        subs = collections.defaultdict(list)
        res = [0] * n
        visited = set()
        for a, b in edges:
            subs[a] += [b]
            subs[b] += [a]
        def dfs(node):
            cnt = Counter()
            if node not in visited:
                cnt[labels[node]] += 1 
                visited.add(node)
                for child in subs[node]:
                    cnt += dfs(child)
                res[node] = cnt[labels[node]]
            return cnt
        dfs(0)
        return res
