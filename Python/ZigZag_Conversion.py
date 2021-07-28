class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows -1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr

# 答案的做法：找规律逐行填入
# 比如：第一行和最后一行，只有numRows长度的列里有数，每两个数之间间隔是cycle = 2(numRows-1)
# 第二行到倒数第二行，numRows长度的列和相隔cycle-2i的地方有数字
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        n = len(s)
        cycle = 2*(numRows-1)
        for i in range(numRows):
            j = 0
            while i+j < n:
                res += s[i+j]
                if (i != 0) and (i != numRows-1) and (j+cycle-i < n):
                    res += s[j+cycle-i]
                j += cycle
        return res
