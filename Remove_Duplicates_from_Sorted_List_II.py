# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 遍历一次的做法，设置两个pointer，dummy和pre，dummy.next永远是指向第一个不重复的head
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

# 自己的做法，第一次遍历用dictionary记录每个值的重复次数，第二次遍历遇到d[next.val]大于1的，就跳过
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        d = {}
        pt = head
        while pt:
            if pt.val not in d:
                d[pt.val] = 1
            else:
                d[pt.val] += 1
            pt = pt.next
        pt = ListNode(0)
        dummy = pt
        pt.next = head
        while pt.next:
            if d[pt.next.val] > 1:
                pt.next = pt.next.next
            else:
                pt = pt.next
        return dummy.next
