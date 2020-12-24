# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Preorder是中左右，Inorder是左中右，preorder的首位数一定是root
# 得到在inorder中的位置idx，idx的左边是它左子树的所有节点，idx右边是它右子树的所有节点
# 同时在preorder中，1：idx+1是它左子树所有节点，idx+1和之后是它右子树的所有节点
# 如果idx > 0，它的左子节点就是pre[1]，如果idx < (len(inorder)-1)，它的右子节点就是pre[idx+1]
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

# 另一种写法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            pre = preorder.pop(0)
            ind = inorder.index(pre)
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
