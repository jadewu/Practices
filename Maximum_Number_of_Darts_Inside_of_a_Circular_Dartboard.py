# 两点+半径确定圆心，对任意两点，根据半径得到圆心，计算所有点到圆心的距离，得到距离小于半径的点的个数，找出最大的点的个数，O(n^3)
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        res = 0
        def find_d(a,b):
            return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
        for i in points:
            for j in points:
                if i == j:
                    continue
                d = find_d(i,j)
                if d <= 2*r:
                    mid = [(i[0]+j[0])/2, (i[1]+j[1])/2]
                    l = (r**2 - (d/2)**2)**0.5
                    if i[1]-j[1] == 0:
                        c1 = [mid[0], i[1]+l]
                        c2 = [mid[0], i[1]-l]
                    else:
                        # (c[0] - mid[0])**2 + (c[1]-mid[1])**2 = l**2
                        # (c[1] - mid[1])/(c[0] - mid[0]) = k
                        # c[1] = k*(c[0]+mid[0])+mid[1]
                        k = -(i[0]-j[0])/(i[1]-j[1])
                        c1 = [mid[0]+(l**2/(k**2+1))**0.5, (l**2/(k**2+1))**0.5*k+mid[1]]
                        c2 = [mid[0]-(l**2/(k**2+1))**0.5, -(l**2/(k**2+1))**0.5*k+mid[1]]
                    # print(c1)
                    num = 0
                    for p in points:
                        if find_d(p,c1) <= r:
                            num += 1
                    res = max(num,res)
                    num = 0
                    for p in points:
                        if find_d(p,c2) <= r:
                            num += 1
                    res = max(num,res)
                    # print(res)
        if res == 0:
            res = 1
        return res 
