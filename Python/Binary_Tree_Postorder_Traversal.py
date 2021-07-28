# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
# 这个没法不用单独的函数了，必须得有个参数res
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return []
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res += [root.val]
        
# Iterative solution
# 顺着记录每一个节点，最后reverse
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            root = node
        res.reverse()
        return res
