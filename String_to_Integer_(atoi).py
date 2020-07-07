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
