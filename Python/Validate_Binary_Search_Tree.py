# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        # 设立较小值，验证inorder traversal的时候是否下一个都比上一个要大
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            # 从最左开始，进行inorder traversal
            root = stack.pop()
            # 如果新拿出的node的值比上一个node的值小，则不对
            if root.val <= inorder:
                return False
            # 将较小值更新为当前的值
            inorder = root.val
            root = root.right
        return True
