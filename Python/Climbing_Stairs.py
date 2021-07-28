# 用DP比较快，用recursion会超时
class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0] * n
        for i in range(n):
            if i == 0:
                stairs[i] = 1
            elif i == 1:
                stairs[i] = 2
            else:
                stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[n-1]
