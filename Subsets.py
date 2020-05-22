# 一个特别巧妙的方法
# 流程：以[1, 2, 3]为例
# num = 1; res = [[]], len=1; res = [[], [1]]
# num = 2; res = [[], [1]], len=2; i=[], res=[[], [1], [2]]; i=[1], res=[[], [1], [2], [1,2]]
# num = 3; res = [[], [1], [2], [1,2]], len=4; i=[], res=[[], [1], [2], [1,2], [3]]; i=[1], res=[[], [1], [2], [1,2], [3], [1,3]]
# i=[2], res=[[], [1], [2], [1,2], [3], [1,3], [2,3]]; i=[1,2], res=[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])
        return res
