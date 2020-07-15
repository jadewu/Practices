# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS，这道题是求binary tree的垂直遍历，同横坐标x的nodes，y较小的在前，同(x, y)的nodes，数值较小的在前
# 一层层遍历并按x记录在dictionary里，这样保证y较小的node会在dic[x]对应的list的前部，y较大的node会放在后面
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        # 需要记录node和它的横坐标x
        q = [(root, 0)]
        # 用dic更容易查找
        dic = collections.defaultdict(list)
        # BFS
        while q:
            # 新建下一层列表
            l = []
            # 把这一层的node.val放进dic里，并构建下一层列表
            for node, x in q:
                dic[x].append(node.val)
                if node.left:
                    l.append((node.left, x-1))
                if node.right:
                    l.append((node.right, x+1))
            # 同y值的nodes按数值从小到大排列，这样当x相同时，数值小的将先放入dic[x]
            l.sort(key = lambda n: n[0].val)
            q = l
        # 按x值从小到大输出每一列
        for key in sorted(dic):
            res.append(dic[key])
        return res
