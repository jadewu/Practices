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
