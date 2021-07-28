# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 比较这个树和这个树的镜像对称树，也就是说，当成两个树来比较
# 第一个树的左节点对应第二个树的右节点，第一个树的右节点对应第二个树的左节点
# Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1, root2):
            if (not root1) and (not root2):
                return True
            if (not root1) or (not root2):
                return False
            if root1.val != root2.val:
                return False
            else:
                if check(root1.left, root2.right) and check(root1.right, root2.left):
                    return True
                else:
                    return False
        return check(root, root)

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 自己想的，标坐标的方法，BFS遍历
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        d = {}
        queue = [(pRoot, 0, 0)]
        while queue:
            cur = queue.pop(0)
            node, row, col = cur[0], cur[1], cur[2]
            d[(row, col)] = node.val
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        for k, v in d.items():
            if (k[0], -k[1]) in d:
                if d[k[0], -k[1]] != v:
                    return False
            else:
                return False
        return True
