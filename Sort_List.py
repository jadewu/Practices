# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 比较简短的写法，在做partition的时候，用fast&slow pointers，可以找到中点节点
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            dummy = tail = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next

            tail.next = h1 or h2
            return dummy.next

        def sortll(head):
            if not head or not head.next:
                return head

            pre, slow, fast = None, head, head
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None
            return merge(sortll(head), sortll(slow))

        return sortll(head)

# 自己的写法，Partition and Merge，分成两段，把sort好的两段用merge 2 linked list的方法合并
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(left, right):
            dummy = head = ListNode(0)
            while left and right:
                if left.val < right.val:
                    head.next = left
                    left = left.next
                else:
                    head.next = right
                    right = right.next
                head = head.next
            if left:
                head.next = left
            elif right:
                head.next = right
            return dummy.next
        def sortll(head, n):
            if n <= 1:
                return head
            dummy = ListNode(0)
            dummy.next = head
            ct = 0
            # print(head, n)
            while ct < n//2-1:
                head = head.next
                ct += 1
            tmp = head.next
            head.next = None
            left = sortll(dummy.next, n//2)
            right = sortll(tmp, n-n//2)
            return merge(left, right)
        pt = head
        n = 0
        while pt:
            pt = pt.next
            n += 1
        return sortll(head, n)
