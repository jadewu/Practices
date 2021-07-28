# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution according to inorder 
# 先左，加上中间root.val，后右
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res

# Iterative solution using STACK
# 如果是root空的，直接return；
# stack先放进root，再放入当前root.left的所有节点
# 结果加上当前节点的值
# 如果root.right不是None，右移root
# 以上循环，直到stack是空的为止
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        s = [root]
        while s:
            while root.left:
                root = root.left
                s.append(root)
            node = s.pop()
            res.append(node.val)
            if node.right:
                root = node.right
                s.append(root)
        return res
        
# Morris solution
# 利用空余的Null指针，来记录每次root的位置，避免使用stack，空间复杂度O(1)
# 用root的左节点下面最右节点的右节点指向root，这样遍历到最右下面的时候，可以马上回到原来root的地方
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        lst = []
        while root:
            if root.left:
                right_most = self.find_right_most(root.left)
                right_most.right = root
                root.left, root = None, root.left
                print(root)
            else:
                lst.append(root.val)
                root = root.right
        return lst
    
    def find_right_most(self, node):
        while node.right:
            node = node.right
        return node
