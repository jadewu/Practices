# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 两种解法的时间复杂度都是O(nklogk), nk = N，n是list的数量，k是list的长度，N是lists的大小
# 用分治法，Divide and Conquer: Partition into 2 halves and merge 2
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l,r):
            res = ListNode(0, None)
            cur = ListNode(0, None)
            res.next = cur
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    cur = cur.next
                    l = l.next
                else:
                    cur.next = r
                    cur = cur.next
                    r = r.next
                # print(cur)
            if l:
                cur.next = l
            else:
                cur.next = r
            return res.next.next
        
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        mid = (len(lists))//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return merge(l,r)

# 用priorityQueue，用heapq构建min heap
# 把所有nodes放入pq里，pop()出的连在res后面，最后就能得到从小到大的结果
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = cur = ListNode(0)
        h = []
        for i, li in enumerate(lists):
            # 当输入不是单纯的可以比较的数字时，需要每一项是(priority, count, task)
            if li is not None:
                heapq.heappush(h, (li.val, i, li))
        while h:
            val, idx, nxt = h[0]
            if not nxt.next:
                heapq.heappop(h)
            else:
                # pop smallest and push new
                heapq.heapreplace(h, (nxt.next.val, idx, nxt.next))
            cur.next = nxt
            cur = cur.next
        return res.next
