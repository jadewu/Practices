# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Post-order是左右中，也就是说，最后一位是root
# In-order是左中右，也就是说，root的左边是左子树，root的右边是右子树
# 因此可以用recursion来做
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            idx = inorder.index(val)
            root.right = helper(idx+1, right)
            root.left = helper(left, idx-1)
            return root
        return helper(0, len(inorder)-1)
