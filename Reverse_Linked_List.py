# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = None
        while head:
            n = ListNode(head.val)
            n.next = node
            head = head.next
            node = n
        return n
