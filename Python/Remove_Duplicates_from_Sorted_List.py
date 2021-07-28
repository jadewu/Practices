# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 链表去重
# 只要是相同value的节点，就把next移到下一个，当遇到value不同的节点的时候，在把current移到next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pt = head
        while pt and pt.next:
            if pt.val == pt.next.val:
                pt.next = pt.next.next
            else:
                pt = pt.next
        return head
            
                
