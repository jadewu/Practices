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
