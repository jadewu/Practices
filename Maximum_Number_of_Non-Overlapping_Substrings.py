# 先找出所有满足条件的substrings，储存它们的起始点和终点
# 然后用greedy找出数量最多的而且最短的
# greedy需要首先把substrings按照终点位置从小到大排列，尽量选终点小的，这样剩下的string能有更多的substrings
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        dur = {}
        for i in range(len(s)):
            if s[i] not in dur:
                dur[s[i]] = [i, i+1]
            else:
                dur[s[i]][1] = i+1
        # print(dur)
        pairs = []
        for k, v in dur.items():
            flag = 0
            occ = set()
            for i in range(v[0], len(s)):
                if s[i] not in occ:
                    occ.add(s[i])
                    if dur[s[i]][0] < v[0]:
                        break
                    else:
                        flag += 1
                if i == dur[s[i]][1]-1:
                    flag -= 1
                if not flag:
                    pairs.append((v[0], i+1))
        # print(pairs)
        pairs.sort(key = lambda x: x[1])
        res = []
        last = 0
        for start, end in pairs:
            if start >= last:
                res.append(s[start:end])
                last = end
        return res
