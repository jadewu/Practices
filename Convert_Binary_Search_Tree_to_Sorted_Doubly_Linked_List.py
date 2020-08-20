"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# In-order traversal，对二叉查找树做中序遍历，即可得到从小到大排列的nodes
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        if not root:
            return None
        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root
        l = inorder(root)
        for i in range(len(l)-1):
            l[i].right = l[i+1]
            l[i].left = l[i-1]
        l[-1].left = l[-2]
        l[-1].right = l[0]
        return l[0]
