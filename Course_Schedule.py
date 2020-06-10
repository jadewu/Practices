# BFS, 先把所有点指向的点记在list里，记录是否需要prerequisites
# 把不需要prerequisites的点放进stack（作为root）
# graph[stack.pop()]得到将当前课作为prerequisite的所有课（下一层），把它们的prerequisites数量-1，之后如果数量为0，就加入stack（新的root）
# 最后如果没有prerequisites了，就说明没有back的边，没有cycle
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        pre = [0]*numCourses
        for e in prerequisites:
            graph[e[0]].append(e[1])
            pre[e[1]] += 1
        stack = []
        for n in range(numCourses):
            if pre[n] == 0:
                stack.append(n)
        while stack:
            l = graph[stack.pop()]
            for n in l:
                pre[n] -= 1
                if pre[n] == 0:
                    stack.append(n)
        return sum(pre) == 0

# DFS 方法一
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        res = []
        # 存放每个点的adjacent list，e[i]: a, b, c ...表示从e[i]有edge到a, b, c...
        for e in prerequisites:
            graph[e[1]].append(e[0])
        # 各个点的访问情况
        visit = [0 for n in range(numCourses)
        def dfs(node):
            # 如果是已经访问完的，这次访问就直接返回false
            if visit[node] == -1:
                return False
            # 如果是正在访问，返回true
            if visit[node] == 1:
                return True
            # 不可以回头
            visit[node] = -1
            # 查看这个点的相邻点
            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            visit[node] = 1
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
            
# DFS 方法二
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 用两个dict来存储路径，key是点，list是相邻的点
        # forward是向外的路径，back是到这个点的路径
        forward = collections.defaultdict(list)
        back = collections.defaultdict(list)
        # 把所有路径记录进两个dict里，正反都记录
        for e in prerequisites:
            forward[e[1]].append(e[0])
            back[e[0]].append(e[1])
        stack = [] # 用来存放没有相邻的回的路径的点
        for node in range(numCourses):
            if not back[node]:
                stack.append(node)
        # DFS
        while stack:
            node = stack.pop()
            # 找到 n 出去的路径里相邻的点，从back里减去
            for n in forward[node]:
                back[n].remove(node)
                if not back[n]:
                    stack.append(n)
            back.pop(node)
        return not back
