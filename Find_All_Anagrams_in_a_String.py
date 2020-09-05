# 找到一个短字符串在一个长字符串里的异位构词的位置
# 比如短字符串"ab"和长字符串“abcbadacb”，得到的结果是[0, 3]
# 和找短字符串的permutation的位置那道题一样的，先建两个字母表，然后一段一段判断是否字母种类和个数一样，一样就记下首字母角标
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        if n > m:
            return []
        ls = [0]*26
        lp = [0]*26
        for i in range(n):
            ls[ord(s[i])-ord("a")] += 1
            lp[ord(p[i])-ord("a")] += 1
        res = []
        for j in range(n, m):
            if ls == lp:
                res.append(j-n)
            ls[ord(s[j])-ord("a")] += 1
            ls[ord(s[j-n])-ord("a")] -= 1
        if ls == lp:
            res.append(m-n)
        return res
