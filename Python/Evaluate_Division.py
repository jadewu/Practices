# 做除法运算，可以DFS/BFS/Union-find
# 这里是自己写的dfs，先画图再计算，并记得要建visited列表
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(set)
        for i in range(len(equations)):
            eq = equations[i]
            graph[eq[0]].add((eq[1], values[i]))
            graph[eq[1]].add((eq[0], 1.0/values[i]))
        def dfs(i, j, visited, ans):
            if i in visited:
                return -1.0
            visited.add(i)
            cur = ans
            for le in graph[i]:
                if le[0] == j:
                    return ans*le[1]
                else:
                    ans = dfs(le[0], j, visited, ans*le[1])
                if ans > 0:
                    return ans
                else:
                    ans = cur
            return -1.0
        res = []
        for q in queries:
            ans = dfs(q[0], q[1], set(), 1.0)
            res.append(ans)
        return res
