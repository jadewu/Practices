# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 快慢指针解法，一个一次跑一个，一个一次跑两个，中间的if区分奇偶
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = head
        while head.next:
            head = head.next.next
            i = i.next
            if not head:
                break
        return i      
 # Dictionary解法，记下来每个节点
 class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        d = {}
        i = 0
        while head:
            if i not in d:
                d[i] = head
            head = head.next
            i += 1
        return d[int(i/2)]
