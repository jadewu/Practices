# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 要考虑到左子节点数值比父节点小，父节点数值比右节点小，作为binary SEARCH tree的特性
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
            
# 没有考虑到binary SEARCH tree的做法，单纯的dfs寻找
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if root.val == val:
            return root
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        if left or right:
            return left or right
        else:
            return None
