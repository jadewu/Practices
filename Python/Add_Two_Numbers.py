# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res
        h = 0
        while l1 or l2:
            if l1 and l2:
                nval = h + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                nval = h + l2.val
                l2 = l2.next
            else:
                nval = h + l1.val
                l1 = l1.next
            if nval > 9:
                nval = nval - 10
                h = 1
            else:
                h = 0
            n = ListNode(nval)
            res.next = n
            res = res.next
            
        if h:
            n = ListNode(1)
            res.next = n
        return head.next
