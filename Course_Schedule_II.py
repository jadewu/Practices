# BFS，做法和Course Schedule里的一样，记录遍历的顺序，如果不存在cycle就输出结果
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        pre = [0]*numCourses
        res = []
        for e in prerequisites:
            graph[e[1]].append(e[0])
            pre[e[0]] += 1
        stack = []
        for n in range(numCourses):
            if pre[n] == 0:
                stack.append(n)
        while stack:
            cur = stack.pop()
            res.append(cur)
            l = graph[cur]
            for n in l:
                pre[n] -= 1
                if pre[n] == 0:
                    stack.append(n)
        if sum(pre) == 0:
            return res
        return []

# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        res = []
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        visited = [0 for x in range(numCourses)]
        def dfs(node):
            if visited[node] == -1: # cycle
                return False
            if visited[node] == 1: #
                return True
            visited[node] = -1
            for x in graph[node]:
                if not dfs(x):
                    return False
            visited[node] = 1
            res.append(node)
            return True

        for x in range(numCourses):
            if not dfs(x):
                return []
        return res
