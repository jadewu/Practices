# 先排序，然后只用比对第一个和最后一个，它们相同的prefix就是整个list相同的
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        res = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                res += x
            else:
                break
        return res

# 直接逐个比对的方法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        res = strs[0]
        for i in range(1, len(strs)):
            long = min(len(res), len(strs[i]))
            for j in range(long):
                if strs[i][j] != res[j]:
                    res = res[:j]
                    break
            if len(res) > len(strs[i]):
                res = strs[i]
        return res
       
