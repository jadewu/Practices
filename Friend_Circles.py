# DFS, recursive，记得要建一个visited列表来避免重复，并把它放到dfs函数的参数里，O(n^2)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        def dfs(visited, i):
            for j in range(n):
                if (M[i][j] == 1) and (visited[j] == 0):
                    visited[j] = 1
                    dfs(visited, j)
        visited = [0]* n
        res = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(visited, i)
                res += 1
        return res

# 自己的做法，应该算是DFS，用stack存储和拿出遍历寻找，circle相当于visited，不过如果写成matrix的形式也可以做每个circle的记录，O(n^2)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        stack = []
        res = 0
        circle = []
        for i in range(n):
            if i in circle:
                continue
            stack.append(i)
            circle.append(i)
            while stack:
                root = stack.pop()
                for j in range(n):
                    if (j not in circle) and (M[root][j] == 1):
                        circle.append(j)
                        stack.append(j)
            # print(circle)
            res += 1
        return res
            
