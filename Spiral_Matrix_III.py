# 一个一个填进每条边里，标记上下左右边界a, b, c, d，每完成一条边，就把标记往中间挪动一格
# 注意在填数字的for loop里要随时检查是否到了n**2
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ct = 1
        a, b, c, d = 0, n, 0, n
        matrix = [[0]*n for _ in range(n)]
        while ct <= n**2:
            for i in range(c, d):
                matrix[a][i] = ct
                ct += 1
                if ct == n**2+1:
                    return matrix
            a += 1
            for i in range(a, b):
                matrix[i][d-1] = ct
                ct += 1
                if ct == n**2+1:
                    return matrix
            d -= 1
            for i in range(d-1, c-1, -1):
                matrix[b-1][i] = ct
                ct += 1
                if ct == n**2+1:
                    return matrix
            b -= 1
            for i in range(b-1, a-1, -1):
                matrix[i][c] = ct
                ct += 1
                if ct == n**2+1:
                    return matrix
            c += 1
        return matrix
