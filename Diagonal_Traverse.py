# 用一个字典把行列和相同的数放在一起，得到的就是斜着打印的列表
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                d[i+j].append(matrix[i][j])
        # print(d)
        res= []
        for k, v in d.items():
            if k%2 == 0:
                res += v[::-1]
            else:
                res += v
        return res

# 找到每一个打印的第一个数的位置，然后斜着添加
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        for d in range(m+n-1):
            line = []
            if d < n:
                r = 0
                c = d
            else:
                r = d-n+1
                c = n-1
            while r < m and c > -1:
                line.append(matrix[r][c])
                r += 1
                c -= 1
            res.append(line)
        out = []
        for i in range(len(res)):
            if i%2 == 0:
                out += res[i][::-1]
            else:
                out += res[i]
        return out
