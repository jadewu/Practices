# DFS, 先画图记录关系，然后写dfs
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ne = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            for email in acc[1:]:
                # 这个画图处理的过程，其实是把acc[1]也就是每一项里的第一个email作为头，其他的都与他连接
                # 不用把所有两两对都画出来，因为接下来做dfs的时候，会处理
                # 比如某次dfs的对象是acc[2]，假设acc[2]只与acc[1]相连，那么下次dfs的对象就会是acc[1]，这样就能得到acc[3,4,...]了
                graph[acc[1]].add(email) 
                graph[email].add(acc[1])
                ne[email] = acc[0]
        def dfs(graph, email, group, visited):
            if email in visited:
                return group
            group.append(email)
            visited.append(email)
            for nxt in graph[email]:
                if nxt not in visited:
                    ngroup = dfs(graph, nxt, group, visited)
                    if len(ngroup) > len(group):
                        group = ngroup
            return group
        done = set()
        res = []
        for email, name in ne.items():
            if email not in done:
                group = dfs(graph, email, [], [])
                done = done | set(group)
                res.append([name]+sorted(group))
        return res

# Union Find 
class DSU:
    def __init__(self):
        self.p = range(10001)
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]
