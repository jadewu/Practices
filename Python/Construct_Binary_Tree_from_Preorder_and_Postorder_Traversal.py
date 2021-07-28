# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# pre是中左右，post是左右中，所以pre的第一个是root，第二个是左子树的根节点
# 在post里找到pre[1]的位置，它和它前边的所有点就是左子树，它后面的点是右子树
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre)==1:
            return root
        idx = post.index(pre[1])+1
        root.left = self.constructFromPrePost(pre[1:idx+1], post[:idx])
        root.right = self.constructFromPrePost(pre[idx+1:], post[idx:])
        return root
