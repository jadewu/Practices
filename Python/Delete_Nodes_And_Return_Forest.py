# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS建立新树
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        # 需要传递两个参数：现在遍历到的node和它是否是一个新树的root
        def dfs(node, is_root):
            if not node: 
                return None
            # 如果在delete列表里，就表明它的两个子节点将成为新树的root
            # 如果不在delete列表里，它的两个子节点保持原样
            if node.val in to_delete:
                root_deleted = True
            else:
                root_deleted = False
            # 如果这个节点是新树的root且不在delete列表里，就在res里重新加一个list
            if is_root and not root_deleted:
                res.append(node)
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            if root_deleted:
                return None
            else:
                return node
            
        dfs(root, True)
        return res
