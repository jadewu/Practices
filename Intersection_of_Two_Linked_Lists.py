# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 双指针，同时从两个list的起点开始，遍历到终点的时候从另一条list的起点再开始，O(n) time, O(1) space
# 假设list1，list2在交叉部分之前的长度分别是m，n，那么p走完list1需要m+c步，q走完list2需要n+c步
# p再从list2开始的时候，q还差n-m步到终点，所以当q到终点是，p已经提前走了n-m步
# 所以当q从list1起点开始的时候，q离交叉部分的起始点差m，p离交叉部分的起始点差n-(n-m)=m，他们会相遇在交叉部分的起始点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (not headA) or (not headB):
            return None
        p, q = headA, headB
        while p != q:
            if not p:
                p = headB
            else:
                p = p.next
            if not q:
                q = headA
            else:
                q = q.next
        return p

# 直接hashmap记录list1的所有节点，O(n)
