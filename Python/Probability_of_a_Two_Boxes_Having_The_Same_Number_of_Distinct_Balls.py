# 把所有单个盒子放2n个球的情况列出来，叉乘得到两个盒子的情况
# 遍历并判断是否满足两个条件：两个盒子里球的总数相同，球的种类数相同
# [1,2,2,3]的所有排列的总数是4!/(1!*2!*!)
class Solution:
    # 题目里的分母，其实就是所有球的排列可能的总数；分子是所有满足条件的情况下，排列总数
    def multinomial(self, n):
        above = factorial(sum(n)) # 所有球的排列个数
        a = []
        for i in n:
            a += [factorial(i)] # n里的每一项的阶乘，可以排除重复
        below = prod(a) # a里所有项相乘
        return above/below # 得到的结果就是balls放进两个盒子的可能数
    
    def getProbability(self, balls: List[int]) -> float:
        # print(self.multinomial([1,2,3]))
        k = len(balls) # 颜色总数
        n = sum(balls)//2 # 每个盒子里球的个数
        q = 0 # 分子
        # 一个盒子里可能有的每种颜色的个数，分别是0~该颜色的总个数
        l = [] 
        for i in balls:
            l += [range(0,i+1)]
        # l x l就是没有限制的情况下，2n个球放在1个盒子里所有可能的情况
        # 比如balls = [1,1,2], l = [[0,1], [0,1], [0,1,2]]
        # l x l = [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2]...[1,1,1], [1,1,2]]
        # 第i项和第len-i-1项的和就是balls，所以需要判断第i项满足两个条件，就可以得到(i，len-i-1)是满足条件的一种方法
        t = list(product(*l)) # 
        # 满足条件的方法需要每个盒子里球的总数是n，两个盒子里球的种类数相同
        for i in range(len(t)):
            # 判断种类数相同的方法是，判断0的个数
            # 如果某个颜色的个数是>0，那么盒子里就有这个种类的球，否则没有
            if sum(t[i]) == n and t[i].count(0) == t[-i-1].count(0):
                q += self.multinomial(t[i]) * self.multinomial(t[-1-i])
        return q/self.multinomial(balls)

# DFS
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        self.total = 0 # 成功的分盒的总数
        self.good = 0 # 满足条件的分盒的总数
        self.sum = sum(balls) # 球的总个数
        first, second = [0]*len(balls), [0]*len(balls)
        print(first, second)
        def dfs(i): # i其实代表的是颜色，balls[i]就是颜色i的球的个数
            if i == len(balls): # 如果所有颜色的个数都写上了
                if sum(first) != sum(second): # 如果两个盒子的球的总数不同，不满足条件
                    return
                # 两个盒子的球的总数相同，分别是n，求每个盒子里的球的所有排序的个数
                prod1 = 1
                for i in first:
                    prod1 *= factorial(i)
                perm1 = factorial(sum(first))/prod1
                prod2 = 1
                for i in second:
                    prod2 *= factorial(i)
                perm2 = factorial(sum(second))/prod2
                # 更新成功分盒的总数
                self.total += perm1*perm2
                # 更新满足条件的分盒的总数
                if first.count(0) == second.count(0):
                    self.good += perm1*perm2
            else: # 如果还没有分配完所有的球, i和i之后的球还没有分进盒子(first/second)里
                for j in range(balls[i]+1): # 一个盒子里可能有0~balls[i]个颜色i的球
                    first[i], second[i] = j, balls[i]-j
                    dfs(i+1)
                    first[i], second[i] = 0, 0

        dfs(0)
        print(self.good, self.total)
        return self.good/self.total

# 剪枝recursion，用组合数求解
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        # 组合公式，比如c(5,3) = (5*4*3)/(3*2*1)
        def c(a,b):
            c = 1
            for i in range(int(b)):
                c *= (a-i)/(b-i)
            return c
        # an, bm分别是两个盒子里现有的球的个数，ak, bk分别是两个盒子里球的颜色种类数
        # rem是还没有放进盒子里的球的个数的数列(开始是balls)
        def rec(an, ak, bn, bk, rem): 
            total = (an + bn + sum(rem)) // 2 # 每个盒子里球的个数均分
            # 如果两个盒子里球的个数不相等
            if an > total or bn > total:
                return 0
            # 如果两个盒子里球的颜色的种类差大于剩下的球的颜色种类数
            # 比如：balls = [1,1,2], 所有球[A, B, C, C]现在两个盒子都是空的，差=0
            # 现在两个盒子里分别是[A], [] 差值=1 < len(rem)==2  继续
            # 现在两个盒子里分别是[A,B], [] 差值=2 > len(rem)==1    不满足条件，因为剩下的球无法得到最后满足条件的结果
            # 现在两个盒子里分别是[A], [B] 差值=0 < len(rem)==1 继续
            # 现在两个盒子里分别是[A,C,C], [B] 差值=1 > len(rem)==0 不满足条件
            # 现在两个盒子里分别是[A,C], [B,C] 差值=0 == len(rem)==0 满足条件
            # 所以当剩下的球的种类数还可以弥补两个盒子里现有种类数的差值的时候，可以继续recursion
            if abs(ak-bk) > len(rem):
                return 0
            # 因为每次recursion都会排除不可能得到满足条件的结果的放置方法，所以如果rem==0，得到的一定是满足条件的方法
            if not rem:
                return 1
            # 取出剩下的球里的第一种颜色的球，把它们放进两个盒子里
            cur, res = rem[0], 0
            # 比如rem[0] = 3, 颜色D，放法有：c(3,0), c(3,1), c(3,2), c(3,3)
            # 如果第一个盒子加上D的个数是c(3,0)，得到的就是an, ak, bn+3, bk+1, rem
            # 如果第一个盒子加上D的个数是c(3,1)，得到的就是an+1, ak+1, bn+2, bk+1, rem
            # 以此类推，满足条件的结果个数会加上这次分配D的种类*之后rec的结果
            for i in range(1,cur):
                res += c(cur,i) * rec(an+i, ak+1, bn+cur-i, bk+1, rem[1:])
            res += rec(an+cur, ak+1, bn, bk, rem[1:])
            res += rec(an, ak, bn+cur, bk+1, rem[1:])
            return res
        
        # 分母是两个盒子均分所有球的所有可能的情况
        below = c(sum(balls), sum(balls)/2)
        # 分子是通过上面recursion得到的满足均分、颜色种类相等的情况
        above = rec(0,0,0,0,balls)
        return above/below
