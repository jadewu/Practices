"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 用字典存储每个原节点和对应的新节点，d中的key是原节点，value是新节点，d[node] = new_node，这样可以很方便地找到next和random
# 核心：d[node].random = d[node.random] 
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        d[None] = None
        while cur:
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
