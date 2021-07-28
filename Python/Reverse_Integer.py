# 题目要求结果不可以overflow，所以要判断是否在32位以内
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        s = str(x)
        res = 1
        if s[0] == "-":
            res = -1
            s = s[1:]
        s = s[::-1]
        zero = 0
        for i in range(len(s)):
            if s[i] == "0":
                zero += 1
            else:
                break
        s = s[zero:]
        res = res * int(s)
        if res > 2**31-1 or res < -2**31:
            return 0
        return res
