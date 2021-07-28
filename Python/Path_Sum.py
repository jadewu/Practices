# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            if sum == root.val:
                return True
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        
# Iterative with stack, root和root.val都需要各存入一个stack（或者一起存进一个stack里），每次同时pop
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [root]
        value = [root.val]
        while stack:
            node = stack.pop()
            val = value.pop()
            if not (node.left or node.right):
                if val == sum:
                    return True

            if node.right:
                stack.append(node.right)
                value.append(val+node.right.val)
            if node.left:
                stack.append(node.left)
                value.append(val+node.left.val)
        return False
        
                
