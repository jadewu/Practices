# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 简单Recursion, DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        
# 用stack和while，DFS，这个运行速度比用上面的recursion快        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        res = 0
        while stack:
            node, level = stack.pop()
            if not node:
                res = max(res, level)
                continue
            level += 1
            stack.append((node.left, level))
            stack.append((node.right, level))
        return res
# 写成recursive function
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def findd(root, d):
            if not root:
                return d
            d += 1
            d = max(findd(root.left, d), findd(root.right,d))
            return d
        res = findd(root,0)
        return res
