# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 快慢指针，fast和slow在同一位置的时候停下，假设从head到cycle的起始点有K步，当slow达到cycle的时候，slow和fast差K步
# 假设slow和fast在同一位置的时候，slow走了X步，cycle的长度是C，那么 X mod C = (K + 2X) mod C
# 也就是 (K + X) mod C = 0，那就是slow需要走K步就是cycle的起点，而且head走K步也是cycle的起点
# 所以找到起点的方法是，此时的slow和head同时开始一次一步地走，它们相遇就是cycle的起点
# 因为写的时候fast起始位置是head.next，所以停下的时候fast实际走了 (K + 2X + 1)，得到的算式是 (K + X + 1) mod C = 0
# 所以slow需要在和head一起走之前，先提前多走一步
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast, slow = head.next, head
        while fast and fast.next:
            if fast == slow:
                slow = slow.next
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head
            fast = fast.next.next
            slow = slow.next
        return None
        
# 用dictionary/hashmap，存放head，碰到重复的就输出，时间空间都是O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = {}
        while head:
            if head in d:
                return head
            d[head] = 1
            head = head.next
        return None
