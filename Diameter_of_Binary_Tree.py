# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# diameter是最长的两node间距离的计算
# 对于一个root，选取左右里较长的一边+root到其父节点的一段：max(left, right)+1，传递到上层
# 在root处的diameter是左子节点传递的长度+右子节点传递的长度
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left+right)
            return max(left, right) + 1
        dfs(root)
        return self.res
