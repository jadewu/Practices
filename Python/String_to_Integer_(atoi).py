class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0: 
            return 0
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        if ls[0] == '-':
            sign = -1
        else:
            sign = 1
        if ls[0] in ('-','+'):
            del ls[0]

        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            res = res*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res,2**31-1))

# 有一点点不一样的思路
class Solution:
    def myAtoi(self, str: str) -> int:
        flg = 0
        res = ""
        digits = ['0','1','2','3','4','5','6','7','8','9']
        for i in str:
            if flg == 0:
                if (i in digits) or (i == "-") or (i == "+"):
                    flg = 1
                    res += i
                elif i == " ":
                    continue
                else:
                    return 0
                # print(i)
            else:
                if i in digits:
                    res += i
                else:
                    break
        if res in ("+", "-", ""):
            return 0
        r = int(res)
        if r < -2**31:
            return -2**31
        elif r > 2**31-1:
            return 2**31-1
        else:
            return int(res)
