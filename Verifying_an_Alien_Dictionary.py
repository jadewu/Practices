# 比较每两个相邻的词的顺序，顺序不对就return False
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for l in range(len(order)):
            d[order[l]] = l
        # print(d)
        for i in range(len(words)-1):
            print(words[i])
            for j in range(len(words[i])):
                if j == len(words[i+1]):
                    return False
                if d[words[i][j]] > d[words[i+1][j]]:
                    return False
                elif d[words[i][j]] < d[words[i+1][j]]:
                    break
        return True
