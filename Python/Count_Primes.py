# 埃拉托斯特尼筛法，计算比n小的质数个数
# 得到n的平方，对2~i，如果i^2比n大，就停止
# 如果i是质数，就剔除所有i的倍数；如果i不是质数，就跳过
# 可以每次从i^2开始剔除，直到大于n^2，因为i(i-1)肯定在判断i-1的时候被剔除过
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        li = [0, 0] + [1]*(n-2)
        i = 2
        while i**2 < n:
            if li[i]:
                mult = i*i
                while mult < n:
                    li[mult] = 0
                    mult += i
            i += 1
        return sum(li)
                    
