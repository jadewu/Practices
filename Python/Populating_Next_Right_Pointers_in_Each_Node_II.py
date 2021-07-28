"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 自己的做法，bfs+层数记录
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = [root]
        f = [0]
        while q:
            node = q.pop(0)
            floor = f.pop(0)
            if q:
                if f[0] == floor:
                    node.next = q[0]
            if node.left:
                q.append(node.left)
                f.append(floor+1)
            if node.right:
                q.append(node.right)
                f.append(floor+1)                
        return root
        
# 记录每一行的最左，在next == None的时候，跳转到下一行的最左
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tail = temp = Node(0)
        node = root
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = temp
                node = temp.next
        return root
