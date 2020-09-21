# 会超时，还没想到更好的解法
# 三种queries：[1]找active的最小值，[1, i]把第i行全换成不active，[2, j]把第j列全换成不active
# 主要是找active最小值这里，应该能优化一下
def matrixQueries(n, m, queries):
    status = [[1]*m for _ in range(n)]
    print(status)
    def mini(status, n, m):
        res = n*m
        for i in range(n):
            for j in range(m):
                if status[i][j] and (i+1)*(j+1) < res:
                    res = (i+1)*(j+1)
        return res
    out = []
    for q in queries:
        if len(q) == 1:
            out.append(mini(status, n, m))
        else:
            if q[0] == 1:
                for i in range(m):
                    status[q[1]-1][i] = 0
            else:
                for j in range(n):
                    status[j][q[1]-1] = 0
            print
    return out
