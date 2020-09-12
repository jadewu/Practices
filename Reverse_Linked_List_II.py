# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 线性做法，前m-1个不需要操作，中间n-m个反转，后面的也不需要操作
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n: 
            return head
        prev = dummy = ListNode(0)
        dummy.next = head
        for i in range(m-1): 
            prev = prev.next
        tail = prev.next

        for i in range(n-m):
            tmp = prev.next                  
            prev.next = tail.next            
            tail.next = tail.next.next       
            prev.next.next = tmp             
        return dummy.next

# 自己的线性做法
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        if m == n:
            return head
        prev = ListNode(0)
        dummy = ListNode(0)
        dummy.next = prev
        prev.next = head
        ct = 1
        while head:
            if ct == m:
                start = prev
                end = head
                tmp = head.next
                head.next = None
                prev = head
                head = tmp
            elif ct > m and ct < n:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            elif ct == n:
                tmp = head.next
                head.next = prev
                start.next = head
                end.next = tmp
                head = tmp
            else:
                prev = head
                head = head.next
            # print(prev)
            ct += 1
        return dummy.next.next
