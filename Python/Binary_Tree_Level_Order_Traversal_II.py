# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, level):
            if not root:
                return
            # 倒着插入，倒着加上values
            if len(res) < level + 1:
                res.insert(0, [root.val])
            else:
                res[-(level+1)].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return res
