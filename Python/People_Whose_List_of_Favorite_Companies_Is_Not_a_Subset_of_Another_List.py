# 先换成数字，方便sort，再判断是否是子集O(n^3)
# 可以直接用set里的issubset()，也可以手写
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        m = len(favoriteCompanies)
        res = []
        cur = []
        l = {}
        t = -1
        for i in favoriteCompanies:
            s = []
            for j in i:
                if j not in l:
                    t += 1
                    s.append(t)
                    l[j] = t
                else:
                    s.append(l[j])
            s.sort()
            cur.append(s)

        for i in range(m):
            f = 1
            for j in range(m):
                if len(cur[i]) >= len(cur[j]):
                    continue
                # if set(cur[i]).issubset(set(cur[j])):
                # 判断是否是子集的O(n)方法，设定两个pivot，遍历一遍
                k, p = 0, 0
                while k < len(cur[i]) and p < len(cur[j]):
                    if cur[i][k] == cur[j][p]:
                        k += 1
                    p += 1
                if k == len(cur[i]):
                    f = 0
                    break
                    
            if f:
                res.append(i)
                        
                
        # print(res)
        return res
                
