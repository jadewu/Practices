# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 在一个dfs里完成，如果满足回文return 1，否则return 0
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, count):
            if not node:
                return 0
            count[node.val] += 1
            if not (node.left or node.right):
                s = 0
                for c in count:
                    s += c % 2
                if s < 2:
                    return 1
                else:
                    return 0
            # [:] copy of the whole array
            return dfs(node.left, count[:]) + dfs(node.right, count[:])
        return dfs(root, [0]*10)

# 自己的做法，找到每条path，判断是否能构成回文
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        path = []
        p = []
        def findp(rt, p, l):
            if not rt:
                return
            if len(p) > l:
                p[l] = rt.val
            else:
                p.append(rt.val)
            l += 1
            if not (rt.left or rt.right):
                q = []
                for i in range(l):
                    q.append(p[i])
                path.append(q)
            else:
                findp(rt.left, p, l)
                findp(rt.right, p, l)
        findp(root, p, 0)
        res = 0
        for p in path:
            dic = {}
            for w in p:
                if w not in dic:
                    dic[w] = 1
                else:
                    dic[w] += 1
            flag = -1
            for key, value in dic.items():
                if value % 2:
                    flag += 1
            if flag <= 0:
                res += 1
        return res            
