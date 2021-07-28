# 如果i在d里，找到最小x使得i(x)不在d里，然后d[i]更新到x，同时在d里加上i(x)
# 那么下次遇到i时，输出为i(x+n)，遇到i(x)的时候就会判断为存在，输出为i(x)(1)
# 还有就是比如i(1), i(3)存在，那么再遇到i时，d[i] = 1，d[i(1)] = 1, d[i(3)] = 1
# 会得到i(2)，d[i] = 2, d[i(2)] = 1
# 再下次遇到i时，会得到i(4), d[i] = 4, d[i(4)] = 1
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        res = []
        for i in names:           
            if i in d:
                c = d[i] + 1
                while i+"("+str(c)+")" in d:
                    c += 1
                d[i] = c    
                i += "("+str(c)+")"
            d[i] = 0
            res.append(i)
        return res
