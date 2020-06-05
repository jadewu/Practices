class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        l = []
        i = 1
        while n >= i*i:
            l.append(i*i)
            i += 1
        c = 0
        check = {n}
        while check:
            c += 1
            temp = []
            for i in check:
                for j in l:
                    if i == j:
                        return c
                    if i < j:
                        break
                    temp.append(i-j)
            check = temp
        return c
