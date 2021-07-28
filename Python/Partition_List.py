# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 遍历一遍，O(1)空间的做法
# 不需要专门用list来放所有节点，只需要新建两个头节点，把原来的linked list里的节点接在小的头或者大的头的后面
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = lh = ListNode(0)
        right = rh = ListNode(0)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = rh.next
        return lh.next

# 自己想的做法，遍历两遍，O(n)空间
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        pt = head
        left = []
        right = []
        while pt:
            if pt.val < x:
                left.append(pt)
            else:
                right.append(pt)
            pt = pt.next
        l = left + right
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]
