# Greedy，用一个array记录每一行最后有多少连续的0，遇到1就停下，换下一行
# 从上到下，安排出最后矩阵的排布，应该是从n-1个0到0个0，需要将满足条件的行放到相应的位子
# 每次选取需要交换次数最靠上面的、且满足对应条件(末尾多少个连续0)的行移到上面去
# 每次记录交换次数后，删除这一行在ending里的记录，防止下次重复
# 因为条件是从大到小的，所以不会出现剩下的行不满足以后的条件的情况
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ending = [0] * n
        res = 0
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    ending[i] += 1
                else:
                    break
        print(ending)
        for i in range(n-1, -1, -1):
            flag = 0
            for j in range(len(ending)):
                if ending[j] >= i:
                    res += j 
                    flag = 1
                    del(ending[j])
                    break
            if not flag:
                ret
