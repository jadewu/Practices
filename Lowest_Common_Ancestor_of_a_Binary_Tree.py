# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
# 首先如果找到了p/q，就会返回p/q，如果到了None（这条线没有找到p/q），会返回None
# 如果只有左/右有值返回，则p/q/p&q在左边或右边；如果两边都有值返回，则p和q分居这个节点的两侧，那么这个节点就是最低公共ancestor
# 只有一边返回值不为None，可能是p和q在同一边，保持返回值不变，也可能是还有p/q没找到，在之后的recursion里能得到公共ancestor
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (p, q, None):
            return root
        
        left = self.lowestCommonAncestor(root.left, p ,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            return left or right

# Iterative
# 建一个dictionary来记录每个节点的parent，在记录完后，可以得到p/q的所有ancestor的list
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while (p not in parent) or (q not in parent):
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        parr = []
        while p:
            parr.append(p)
            p = parent[p]
        while q not in parr:
            q = parent[q]
        return q

# 自己的做法，分别找到从root到p/q的path arr，两个arr的最后一个相同的node就是lowest common node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findpath(rt, t, res):
            if rt == t:
                return True
            if not rt:
                return False
            res.append(rt)
            if findpath(rt.left, t, res):
                return True
            if findpath(rt.right, t, res):
                return True
            res.pop()
            return False
        parr = []
        qarr = []
        findpath(root, p, parr)
        findpath(root, q, qarr)
        parr.append(p)
        qarr.append(q)

        i = 0
        while i < len(parr) and i < len(qarr):
            if parr[i] != qarr[i]:
                return res
            res = parr[i]
            i += 1
        return res
