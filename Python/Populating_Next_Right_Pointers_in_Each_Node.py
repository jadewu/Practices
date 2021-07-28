"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(1) in place iteration，这个题的关键点是，node.next在definition里已经设定是None了，所以最右node的next不需要更改
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root
        nxt = root.left # 记录每一行的最左node
        # 有下一行就iterate，如果没有下一行了，就停住
        while cur.left:
            cur.left.next = cur.right
            if cur.next: # 如果还没有到这一行的最右边
                # 连好下一行的next
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                # 换到下一行，并储存下下行的最左node为nxt
                cur = nxt
                nxt = cur.left
        return root
# Recursion
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
        
# 自己的做法，bfs
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = [root]
        f = [0]
        while q:
            node, floor = q.pop(0), f.pop(0)
            if (not q) or (floor < f[0]):
                node.next = None
            else:
                node.next = q[0]
            if node.left:
                q.append(node.left)
                f.append(floor+1)
            if node.right:
                q.append(node.right)
                f.append(floor+1)
        return root
