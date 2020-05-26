# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root.val]
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res

# Iterative solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root.val]
        stack = [root]
        while stack:
            while root.left:
                root = root.left
                res.append(root.val)
                stack.append(root)
            node = stack.pop()
            if node.right:
                root = node.right
                res.append(root.val)
                stack.append(root)
        return res
        
# Simple iterative solution
# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
