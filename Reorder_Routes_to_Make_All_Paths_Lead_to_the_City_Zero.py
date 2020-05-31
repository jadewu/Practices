# 因为输入是一个Tree，而且没有环，按从小到大的顺序，所以不需要复杂的处理
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        dic = {0:1}
        for c in connections:
            if c[1] in dic:
                dic[c[0]] = 1
            else:
                res += 1
                dic[c[1]] = 1
        return res
# 考虑复杂的处理
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        l = [0]
        s = []
        for c in connections:
            s.append(c[:])
        print(s)
        while len(l) < n:
            for i in range(len(connections)):
                if connections[i][1] in l:
                    l.append(connections[i][0])
                    continue
                r = connections[i][:]
                r.reverse()
                if (connections[i][0] in l) and (r not in connections):
                    res += 1
                    l.append(connections[i][1])
                    connections[i] = r
        print(connections)
        return res  
