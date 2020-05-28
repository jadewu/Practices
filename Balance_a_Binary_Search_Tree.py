# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder Traversal + Re-create BST
# 重建BST只需要找到一个最简单的解法就行了：把遍历得到的list的中间项作为root，左边的作为left tree，右边的作为right tree
# 如果要求不能用extra space for BST，用DSW Algorithm，具体怎么做还没看
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 直接用recursive的方法做inorder traversal比较简单
        # def dfs(node):
        #     if node:
        #         dfs(node.left)
        #         value.append(node.val)
        #         dfs(node.right)
        # dfs(root)
        
        # 也可以用iterative的方法
        stack = [root]
        value = []
        node = root
        while stack:
            while node.left:
                stack.append(node.left)
                node = node.left
            n = stack.pop()
            value.append(n.val)
            if n.right:
                stack.append(n.right)
                node = n.right
        # print(value)
        
        def bst(v):
            if not v:
                return None
            mid = len(v) // 2   # Floor division
            root = TreeNode(v[mid])
            root.left = bst(v[:mid])
            root.right = bst(v[mid+1:])
            return root
        return bst(value)
    
