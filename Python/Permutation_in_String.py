# Sliding Window，O(l1 + 26*(l2-l1))
# 建两个记录字母表，表明这一段字符串里有哪几个字母，因为是permutation，所以不需要顺序一样，只需要字母种类和个数一样
# 这道题不用dictionary和counter，因为碰到不一样的，就需要复原字典，增加复杂度
# 每次对比两段相同长度的字符串对应的字母表是否相同，如果相同，就说明其中一个是另一个的permutation
# 如果不相同，就复原最左边的，然后添加下一位，每次只用改两个位子的数字
# 字母表的角标用ord(s[i]) - ord("a")表示
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        l1 = [0]*26
        l2 = [0]*26
        for i in range(m):
            idx1 = ord(s1[i])-ord("a")
            idx2 = ord(s2[i])-ord("a")
            l1[idx1] += 1
            l2[idx2] += 1
        for i in range(n-m):
            if l1 == l2:
                return True
            pidx = ord(s2[i])-ord("a")
            nidx = ord(s2[i+m])-ord("a")
            l2[pidx] -= 1
            l2[nidx] += 1
        if l1 == l2:
            return True
        return False
