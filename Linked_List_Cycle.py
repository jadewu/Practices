# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 快慢指针，O(n) time，O(1) space，一个一次跳一下，一个一次跳两下
# 要注意的地方是，最开始的时候，不能直接fast=slow=head，两者会成为同一个指针
# 两种解决方法：一个指head，一个指head.next；或者重新建两个ListNode复制head的属性
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast is slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

# 用hash，直接看有没有遍历过（hash查找还算快），O(n) time & space
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = {}
        while head:
            if head.next in d:
                return True
            d[head] = 1
            head = head.next
        return False
