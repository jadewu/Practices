# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with stack, 存放root、sum和[root.val]，需要记录离目标值还差多少
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [[root, sum, [root.val]]]
        while stack:
            node, d, val = stack.pop()
            if not (node.left or node.right):
                if d == node.val:
                    res.append(val)
            if node.right:
                stack.append([node.right, d-node.val, val+[node.right.val]])
            if node.left:
                stack.append([node.left, d-node.val, val+[node.left.val]])
        return res
        
# DFS with stack，存放root和[root.val]，需要每次到leaf的时候对[root.val]求和，时间复杂度会比O(n)高一些
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [[root, [root.val]]]
        while stack:
            node, val = stack.pop()
            # print(node)
            # print(val)
            # print(res)
            if not (node.left or node.right):
                val_sum = 0
                for i in val:
                    val_sum += i
                if val_sum == sum:
                    res.append(val)
            if node.right:
                stack.append([node.right, val+[node.right.val]])
            if node.left:
                stack.append([node.left, val+[node.left.val]])
        return res
 # Recursive solution, 注意在sums那里会得到[[],[]...]，所以在return的时候要把最外层的括号拆开
 class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not (root.left or root.right):
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        sums = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val] + i for i in sums]                   
